import os
import re
from datetime import datetime, timedelta
from textwrap import dedent

import streamlit as st
from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.run.agent import RunOutput
from agno.tools.serpapi import SerpApiTools
from icalendar import Calendar, Event

load_dotenv()


def generate_ics_content(plan_text:str, start_date: datetime = None) -> bytes:
    """
        Generate an ICS calendar file from a travel itinerary text.

        Args:
            plan_text: The travel itinerary text
            start_date: Optional start date for the itinerary (defaults to today)

        Returns:
            bytes: The ICS file content as bytes
        """
    cal = Calendar()
    cal.add('prodid','-//AI Travel Planner//github.com//' )
    cal.add('version', '2.0')

    if start_date is None:
        start_date = datetime.today()

    # Split the plan into days
    day_pattern = re.compile(r'Day (\d+)[:\s]+(.*?)(?=Day \d+|$)', re.DOTALL)
    days = day_pattern.findall(plan_text)

    if not days: # If no day pattern found, create a single all-day event with the entire content
        event = Event()
        event.add('summary', "Travel Itinerary")
        event.add('description', plan_text)
        event.add('dtstart', start_date.date())
        event.add('dtend', start_date.date())
        event.add("dtstamp", datetime.now())
        cal.add_component(event)  
    else:
        # Process each day
        for day_num, day_content in days:
            day_num = int(day_num)
            current_date = start_date + timedelta(days=day_num - 1)
            
            # Create a single event for the entire day
            event = Event()
            event.add('summary', f"Day {day_num} Itinerary")
            event.add('description', day_content.strip())
            
            # Make it an all-day event
            event.add('dtstart', current_date.date())
            event.add('dtend', current_date.date())
            event.add("dtstamp", datetime.now())
            cal.add_component(event)

    return cal.to_ical()


# Set up the Streamlit app
st.title("AI Travel Planner using Gemini")
st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary on autopilot using Gemini")

# Initialize session state to store the generated itinerary
if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

use_vertex_ai = os.getenv("USE_VERTEX_AI", "false").strip().lower() in {"1", "true", "yes"}
DEFAULT_GEMINI_MODEL_ID = os.getenv("GOOGLE_MODEL_ID", "gemini-3.8-flash")
st.caption("Vertex AI auth is optional. Leave it disabled to use a Google API key directly.")

# Debug auth state for troubleshooting
print(f"DEBUG: USE_VERTEX_AI={use_vertex_ai}")
print(f"DEBUG: GOOGLE_API_KEY present={bool(os.getenv('GOOGLE_API_KEY'))}")
print(f"DEBUG: GOOGLE_CLOUD_PROJECT present={bool(os.getenv('GOOGLE_CLOUD_PROJECT'))}")
print(f"DEBUG: GOOGLE_MODEL_ID={DEFAULT_GEMINI_MODEL_ID}")

# Get API keys from the environment or the user
google_api_key = st.text_input(
    "Enter Google AI API Key",
    type="password",
    value=os.getenv("GOOGLE_API_KEY", ""),
    help="Use the account-bound key restricted to Agent Platform API.",
)
google_project = st.text_input(
    "Enter Google Cloud Project ID",
    value=os.getenv("GOOGLE_CLOUD_PROJECT", ""),
    help="Use the project that owns the account-bound API key when Vertex AI is enabled.",
)
google_location = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
serp_api_key = st.text_input(
    "Enter Serp API Key for Search functionality",
    type="password",
    value=os.getenv("SERPAPI_API_KEY", ""),
)


def make_gemini_model():
    if use_vertex_ai:
        if not google_project:
            raise ValueError("GOOGLE_CLOUD_PROJECT is required when USE_VERTEX_AI=true")
        print("DEBUG: Creating Gemini model with Vertex AI auth")
        return Gemini(
            id=DEFAULT_GEMINI_MODEL_ID,
            api_key=google_api_key,
            vertexai=True,
            project_id=google_project,
            location=google_location,
        )
    print(f"DEBUG: Creating Gemini model with direct API key auth. API key length={len(google_api_key) if google_api_key else 0}")
    return Gemini(
        id=DEFAULT_GEMINI_MODEL_ID,
        api_key=google_api_key,
    )


if google_api_key and serp_api_key:
    researcher = Agent(
        name="Researcher",
        role="Searches for travel destinations, activities, and accommodations based on user preferences",
        model=make_gemini_model(),
        description=dedent(
            """\
        You are a world-class travel researcher. Given a travel destination and the number of days the user wants to travel for,
        generate a list of search terms for finding relevant travel activities and accommodations.
        Then search the web for each term, analyze the results, and return the 10 most relevant results.
        """
        ),
        instructions=[
            "Given a travel destination and the number of days the user wants to travel for, first generate a list of 3 search terms related to that destination and the number of days.",
            "For each search term, `search_google` and analyze the results.",
            "From the results of all searches, return the 10 most relevant results to the user's preferences.",
            "Remember: the quality of the results is important.",
        ],
        tools=[SerpApiTools(api_key=serp_api_key)],
        add_datetime_to_context=True,
    )
    planner = Agent(
        name="Planner",
        role="Generates a draft itinerary based on user preferences and research results",
        model=make_gemini_model(),
        description=dedent(
            """\
        You are a senior travel planner. Given a travel destination, the number of days the user wants to travel for, and a list of research results,
        your goal is to generate a draft itinerary that meets the user's needs and preferences.
        """
        ),
        instructions=[
            "Given a travel destination, the number of days the user wants to travel for, and a list of research results, generate a draft itinerary that includes suggested activities and accommodations.",
            "Ensure the itinerary is well-structured, informative, and engaging.",
            "Ensure you provide a nuanced and balanced itinerary, quoting facts where possible.",
            "Remember: the quality of the itinerary is important.",
            "Focus on clarity, coherence, and overall quality.",
            "Never make up facts or plagiarize. Always provide proper attribution.",
        ],
        add_datetime_to_context=True,
    )

    # Input fields for the user's destination and the number of days they want to travel for
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Generate Itinerary"):
            with st.spinner("Researching your destination..."):
                research_results: RunOutput = researcher.run(
                    f"Research {destination} for a {num_days} day trip", stream=False
                )
                st.write("Research completed")

            with st.spinner("Creating your personalized itinerary..."):
                prompt = f"""
                Destination: {destination}
                Duration: {num_days} days
                Research Results: {research_results.content}

                Please create a detailed itinerary based on this research.
                """
                response: RunOutput = planner.run(prompt, stream=False)
                # Store the response in session state
                st.session_state.itinerary = response.content
                st.write(response.content)
    
    # Only show download button if there's an itinerary
    with col2:
        if st.session_state.itinerary:
            # Generate the ICS file
            ics_content = generate_ics_content(st.session_state.itinerary)
            
            # Provide the file for download
            st.download_button(
                label="Download Itinerary as Calendar (.ics)",
                data=ics_content,
                file_name="travel_itinerary.ics",
                mime="text/calendar"
            )