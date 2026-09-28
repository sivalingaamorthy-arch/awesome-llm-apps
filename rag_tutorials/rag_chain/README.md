# PharmaQuery

## Overview
PharmaQuery is an advanced Pharmaceutical Insight Retrieval System designed to help users gain meaningful insights from research papers and documents in the pharmaceutical domain.

## Demo
https://github.com/user-attachments/assets/c12ee305-86fe-4f71-9219-57c7f438f291

## Features
- **Natural Language Querying**: Ask complex questions about the pharmaceutical industry and get concise, accurate answers.
- **Custom Database**: Upload your own research documents to enhance the retrieval system's knowledge base.
- **Similarity Search**: Retrieves the most relevant documents for your query using AI embeddings.
- **Streamlit Interface**: User-friendly interface for queries and document uploads.

## Technologies Used
- **Programming Language**: [Python 3.10+](https://www.python.org/downloads/release/python-31011/)
- **Framework**: [LangChain](https://www.langchain.com/)
- **Database**: [ChromaDB](https://www.trychroma.com/)
- **Models**:
  - Embeddings: [Google Gemini API (gemini-embedding-001)](https://ai.google.dev/gemini-api/docs/embeddings)
  - Chat: [Google Gemini API (gemini-3.5-flash)](https://ai.google.dev/gemini-api/docs/models)
- **PDF Processing**: [PyPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/)
- **Document Splitter**: [SentenceTransformersTokenTextSplitter](https://python.langchain.com/api_reference/text_splitters/sentence_transformers/langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter.html)

## Requirements
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your Gemini API Key**: copy `.env.example` to `.env` and add your key ([get one here](https://aistudio.google.com/apikey)):
   ```bash
   GEMINI_API_KEY=your-gemini-api-key
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **Use the Application**:
   - If `GEMINI_API_KEY` isn't set in `.env`, paste your key in the sidebar (a key entered there overrides the env value).
   - Enter your query in the main interface.
   - Optionally, upload research papers in the sidebar to enhance the database.

## Example Documents
Don't have pharma PDFs handy? Download any of these publicly available documents and upload them in the sidebar:

| Document | Source | Sample question |
|----------|--------|-----------------|
| [Keytruda (pembrolizumab) Prescribing Information](https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/125514s142lbl.pdf) | U.S. FDA | What are the common adverse reactions of pembrolizumab? |
| [Keytruda EPAR Product Information](https://www.ema.europa.eu/en/documents/product-information/keytruda-epar-product-information_en.pdf) | EMA | How should Keytruda be stored? |
| [ICH E6(R3) Good Clinical Practice](https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf) | ICH | What are the sponsor's responsibilities in a clinical trial? |
| [ICH Q1A(R2) Stability Testing of New Drug Substances and Products](https://database.ich.org/sites/default/files/Q1A%28R2%29%20Guideline.pdf) | ICH | What storage conditions are used for accelerated stability testing? |
| [ICH E2A Clinical Safety Data Management](https://database.ich.org/sites/default/files/E2A_Guideline.pdf) | ICH | How is a serious adverse event defined? |
| [Principles of early drug discovery (research paper)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3058157/) | PubMed Central (open access) | What are the main stages of early drug discovery? |

## :mailbox: Connect With Me
<img align="right" src="https://media.giphy.com/media/2HtWpp60NQ9CU/giphy.gif" alt="handshake gif" width="150">

<p align="left">
  <a href="https://linkedin.com/in/codewithcharan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
  <a href="https://instagram.com/joyboy._.ig" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="__mr.__.unique" height="30" width="40" /></a>
  <a href="https://twitter.com/Joyboy_x_" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="codewithcharan" height="30" width="40" style="margin-right: 10px" /></a>
</p>