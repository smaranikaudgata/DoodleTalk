# DoodleTalk

A Streamlit application offering two features:
1. **Chat with Me**: An interactive chatbot using the Gemini API.
2. **Help with Docs**: A PDF reader that processes and answers questions based on uploaded PDF files.

## Features

- **Chat with Me**: Engage in a conversation with a chatbot that uses advanced language generation capabilities.
- **Help with Docs**: Upload PDF files, process them, and ask questions to get answers based on the content of the PDFs.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/smaranikaudgata/DoodleTalk.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd DoodleTalk
   ```

3. **Create a virtual environment and activate it:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following lines with your API keys:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Navigate to `http://localhost:8501` in your browser.**

### Chat with Me

- Select "Chat with me :)" from the sidebar.
- Engage with the chatbot by typing your queries and receive responses powered by the Gemini API.

### Help with Docs

- Select "Help with docs?" from the sidebar.
- Upload your PDF files in the sidebar and click "Submit & Process" to process them.
- Ask questions related to the content of the PDFs, and the system will provide answers based on the processed text.

## Files

- **`app.py`**: Main file that sets up the Streamlit app and manages navigation between the chatbot and PDF reader.

- **`chat.py`**: Contains the logic for the interactive chatbot using the Gemini API.

- **`pdfReader.py`**: Provides functionality to process PDF files and answer questions based on the text extracted from them.

## Privacy and Data Handling

### No Data Storage

- **Chat with Me**: The chatbot functionality does not store previous chat histories. Once the chat session ends or is cleared by the user, the chat history is lost. The application does not retain any user queries or responses beyond the current session. This ensures that your interactions with the chatbot are not stored or tracked.

- **Help with Docs**: Similarly, the PDF reader does not store any of the uploaded PDF files or the questions asked. Once the PDF processing is complete and the session ends, all data is discarded. The system does not retain any information from the uploaded documents or user queries.

### Privacy Assurance

- **No Persistent Storage**: The application is designed to run in a temporary environment where all data is processed in memory and not written to any persistent storage. This design choice aligns with the goal of maintaining user privacy and ensuring that no personal data is stored or misused.

- **Secure Environment**: API keys and sensitive configurations are managed through environment variables, ensuring that such information is not hard-coded or exposed within the codebase. This helps to keep your credentials secure and private.

By using this application, you can be assured that your data is handled with a high level of privacy, with no long-term storage of your interactions or document contents.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the app framework.
- [Gemini API](https://example.com) for chatbot capabilities.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF processing.
- [LangChain](https://www.langchain.com/) for text processing and QA chain.
