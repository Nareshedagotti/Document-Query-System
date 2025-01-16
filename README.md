# Document Query System with Groq & Ollama Models

A powerful system that allows users to upload PDF, DOCX, or TXT files and interact with the document using **Groq** or **Ollama** models. The system extracts text from the document and enables the user to query it for relevant information. This is implemented with a dynamic user interface built using **Gradio**.

## Features

- **File Upload Support**: Upload PDF, DOCX, or TXT files for processing.
- **Model Selection**: Switch between **Groq** or **Ollama** models for querying the document.
- **Text Extraction**: Extracts text from various file formats.
- **Chat Interface**: Interactive chatbot-like interface for querying the document's contents.
- **Real-Time Responses**: Instant answers to user queries based on the uploaded document.

## Project Structure

```
project/
├── app.py              # Main entry point to launch the application
├── utils.py            # Utility functions for text extraction from documents
├── models.py           # Model interaction for Ollama and Groq
├── ui.py               # Gradio UI components and layout
├── requirements.txt    # Dependencies list for Python packages
└── README.md           # Project documentation
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/document-query-system.git
   cd document-query-system
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get Groq API Key**:
   - Sign up at [Groq API](https://groq.com) to obtain an API key.
   - Replace the placeholder in `models.py` with your actual **Groq API key**.

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Web Interface**:
   - Once the app is running, open a browser and visit the Gradio interface at `http://localhost:7860`.

## Usage

1. **Upload a Document**:
   - Click on the **Upload Your Document** section to upload a **PDF**, **DOCX**, or **TXT** file.
   
2. **Select a Model**:
   - Choose between **Groq** and **Ollama** models using the **Model Selection** radio button.

3. **Ask Questions**:
   - Enter your question related to the document in the **Your Question** textbox.
   - The system will retrieve the answer based on the document content.

4. **View Chat History**:
   - All conversations will be displayed in the **Chat History** section.

## Example Screenshots

Here are some sample outputs of the system:

### Example Output 1 ![Screenshot 2025-01-16 182910](https://github.com/user-attachments/assets/024006eb-4bf9-4efa-a6e1-71e3f87fbed2)

*Figure 1: Document Upload and Model Selection*

### Example Output 2![Screenshot 2025-01-16 182952](https://github.com/user-attachments/assets/78225c16-a996-471e-8822-369579a5aaa1)

*Figure 2: Chatbot Interaction with Document*

## Models Used

- **Ollama**: A powerful LLM used for natural language understanding and query processing.
- **Groq**: A robust model for high-performance querying, used as an alternative to Ollama.

## Enhancements and Next Steps

- **Support for More File Formats**: Add support for other document formats like **HTML** or **RTF**.
- **Performance Optimizations**: Improve the processing speed and scalability of large documents.
- **User Authentication**: Add user login functionality to personalize the experience and keep track of previous queries.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. If you find any bugs or issues, please open an issue in the repository.
