import gradio as gr
from utils import process_uploaded_file
from models import create_ollama_embeddings, query_ollama, query_groq

# Chatbot with history
def chatbot_with_history(uploaded_file, chat_history, user_message, model_selection):
    extracted_text = process_uploaded_file(uploaded_file)
    if "Error" in extracted_text:
        return chat_history + [(user_message, extracted_text)]

    # Create vector store using Ollama embeddings
    vectorstore = create_ollama_embeddings([extracted_text])

    # Query based on selected model
    if model_selection == "llama3.2-Ollama":
        response = query_ollama(vectorstore, user_message)
    else:  # Use Groq
        response = query_groq(user_message, vectorstore)  # Pass vectorstore to Groq query function

    chat_history.append((user_message, response))
    return chat_history

def build_ui():
    with gr.Blocks() as interface:
        chat_history = gr.State([])  # State for storing chat history

        with gr.Row():
            gr.Markdown("## Chat With Your Document")
            uploaded_file = gr.File(label="Upload PDF, DOCX, or TXT file", file_types=[".pdf", ".docx", ".txt"])

        with gr.Row():
            # Radio button to select the model with a default value of 'Ollama'
            model_selection = gr.Radio(
                choices=["llama3.2-Ollama", "llama3.3-Groq"], 
                value="llama3.2-Ollama", 
                label="Select Model",
                interactive=True  # Ensure the radio button is interactive
            )

        with gr.Row():
            chatbot = gr.Chatbot(label="Chat History", value=[], height=400)

        with gr.Row():
            user_message = gr.Textbox(label="Your Question", placeholder="Type your question here...")
            submit_btn = gr.Button("Ask")

        # When submit button is clicked, call the chatbot_with_history function
        submit_btn.click(
            chatbot_with_history,
            inputs=[uploaded_file, chat_history, user_message, model_selection],
            outputs=chatbot
        )

        return interface
    
