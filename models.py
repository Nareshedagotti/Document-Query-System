from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from groq import Groq

# Initialize Groq client
GROQ_API_KEY = "gsk_un8ZVsPl7VN62OF09JnUWGdyb3F"
groq_client = Groq(api_key=GROQ_API_KEY)

# Function to initialize embeddings
def create_ollama_embeddings(texts):
    embeddings = OllamaEmbeddings(model="llama3.2")
    vectorstore = InMemoryVectorStore.from_texts(texts, embedding=embeddings)
    return vectorstore

# Function to query Ollama model
def query_ollama(vectorstore, user_message):
    retriever = vectorstore.as_retriever()
    template = """Question: {question}
    Answer: Let's think step by step."""
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="llama3.2")
    chain = prompt | model
    qa_chain = RetrievalQA.from_chain_type(llm=chain, chain_type="stuff", retriever=retriever)
    return qa_chain.run(user_message)

def query_groq(user_message, vectorstore):
    # Retrieve relevant data from the vector store
    retrieved_docs = vectorstore.similarity_search(user_message, k=5)  # Retrieve top 5 relevant documents
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    # Combine user message with the retrieved context
    prompt = f"""The following information is extracted from the uploaded document:
{context}

Question: {user_message}
Answer:"""

    # Query the Groq model with the contextual prompt
    try:
        response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error querying Groq model: {e}"
