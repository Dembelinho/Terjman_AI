# Terjman_AI
This a Hackathon project's Repo
# Getting Started
## 📚Prerequisite
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)

```

* Ollama
* GPT
* Langchain / llama-index
* HuggingFace
* Google-Colab
* Python
* Postgres SGBD

```

## RAG Schema
<img src="https://github.com/Dembelinho/Terjman_AI/assets/110602716/367b441d-a9da-47d8-8323-df98a4182170" alt="RAG Schema" width="400" height="500">

This schema illustrates a workflow involving various components for a document retrieval and processing system using LlamaIndex /or Langchain. Here’s an explanation:

1. **Upload Docs**
   - **Document(s) Upload**: We upload a document(s) in a specific field (For example in health -like first aid instruction-).

2. **Local Processing**
   - **Document Handling**: The uploaded document(s) is processed using Advanced RAG (Retrieval-Augmented Generation) Retrieval Strategies.
   - **LlamaIndex / Langchain**: 
     - The document is divided into chunks for efficient processing depending on a chunk's size.
     - These chunks are then embedded and vectorized using an embedding model.
     - The embeddings are stored in a searchable vector database (like Postgres in this case).

3. **Vector Database (Postgres)**
   - **Storage and Retrieval**:
     - The embedded document(s) chunks are saved in Postgres.
     - When a query is received, the system searches through these embeddings to find relevant chunks.
   - **Prompt Template**: A template that helps in forming the retrieval document(s) context to create prompts for further processing.

4. **Remote Processing (Colab Machine)**
   - **ngrok**: Used for establishing secure tunnels to the local environment, allowing remote interaction.
   - **CO (Colab Machine)**: Represents a remote machine (e.g., Google Colab) where additional processing can take place.
   - **LLM (Large Language Model)**: The system leverages a large language model from providers like Mistral AI, Gemma, or Llama for natural language processing tasks.
   - The LLM processes the prompt created using the retrieved document(s) chunks and sends the response back.

5. **Response Handling**
   - The response from the LLM is sent back to the local environment for traduction into 'Darija'.
   - **Streamlit Interface**: The final response is displayed to the user through the Streamlit interface.

**Workflow Summary**:
1. We upload a document(s).
2. The document is chunked, embedded, and stored in Postgres using LlamaIndex Or Langchain.
3. A query is processed by searching the vectorized chunks in Postgres.
4. Relevant chunks are used to form a prompt, which is sent to a remote LLM (via ngrok and CO).
5. The LLM processes the prompt and returns a response.
6. The generated response needs to be translated to 'Darija' and it is displayed to the user through Streamlit.

This setup allows for efficient document retrieval and processing by combining local and remote computational resources and advanced machine-learning models.

## Fine-tuning 

1. **The model**
   - **Helsinki-NLP/opus-mt-ar-en**: This model can accept as a source language: 'Arabic' and translate it into a target language: 'English'.
2. **The purpose**
3. **The dataset


## User interaction (Streamlit)
1. **User Interaction**
   - The end-user interacts with the system through a user interface built with Streamlit.
