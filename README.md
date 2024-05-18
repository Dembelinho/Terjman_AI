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
# Project: Context & Limitations
The project will be a multilingual question-answering (Q/A) system that specifically handles queries in "Darija" (Moroccan Local Arabic).
## Context: Source of the Idea
- In the current time many LLMs can do some great tasks with a big knowledge of different fields but the problem for "Moroccan people" is the query should be in French or English language(The most Popular Languages)
- So we got the idea to develop a comprehensive multilingual question-answering (Q/A) platform that allows Moroccan users to interact with advanced Large Language Models (LLMs) using their native languages, such as Darija (Moroccan Arabic), ensuring accessibility and inclusivity in leveraging cutting-edge AI technologies for various informational needs.
- And also the possibility of uploading some documents to extract knowledge from them.

## Limitations of our Solution
- But the limitations of our solution are reflected in expressions with a metaphorical meaning such as proverbs.
- For more clarity, I will give some examples :
- 1. "Ta7 l7ok wssab ghtah"
  2. "F9ih li ntsenaw barakto dkhal jame3 b baleghto"
  3. "Drebni w bka, sbe9ni w chka" ,etc....
  
# Project Global Schema

<img src="https://github.com/Dembelinho/Terjman_AI/assets/110602716/102c14fb-e89a-4c1d-8e1d-3b63116afe55" alt="Terjman Schema" width="500" height="500">

   This schema outlines a system for processing queries in **"Darija"** (Moroccan Arabic) and converting them into English for further processing by an LLM (Large Language Model). Then translating back the response into Darija. 

   Here’s a detailed explanation of each component and the workflow:

1. **User Interaction (Streamlit)**
   - **User**: The final user interacts with the system through a user interface (UI) built with Streamlit.
   - **Darija Query**: The user submits a query in Darija through the Streamlit interface.

2. **Translation and Embedding**
   - **tarjam_darija_english**: This component translates the Darija query into English. It likely uses a fine-tuned machine translation model "Helsinki-NLP/opus-mt-ar-en", that has    been trained to convert Darija to English.
   - **English Query**: The translated English query is generated from the Darija query.

3. **Processing with LangChain**
   - **LangChain**: A framework used for prompt engineering and managing interactions with LLMs. It is used to create a structured prompt from the English query.
   - **Prompt Engineering**: This step involves creating an appropriate prompt for the LLM to process based on the English query. It involves formatting and structuring the query to get the best possible response from the LLM.

4. **LLM Interaction**
   - **API LLM**: An external API-based large language model (like OpenAI's GPT) is used to process the structured prompt.
   - **Open Sources LLM**: Alternatively, a public LLM model can be used for processing the query. This might be an in-house model or one hosted on any server.
   - **Response Generation**: The LLM processes the prompt and generates a response in English.

5. **Translation Back to Darija**
   - **tarjam_english_darija**: This component translates the English response back into Darija using **" lachkarsalim/Helsinki-translation-English_Moroccan-Arabic "** model from HuggingFace.
   - **Darija Response**: The translated response in Darija is generated from the English response.

6. **Returning the Response**
   - **Postgres**: The queries and responses are stored in a Postgres database for record-keeping, analytics, or further processing.
   - **Streamlit Interface**: The final response in Darija is displayed to the user through the Streamlit interface.

**Workflow Summary**:
1. The user submits a Darija query via Streamlit UI.
2. The Darija query is translated into English using the `tarjam_darija_english` component.
3. The English query is processed using LangChain for prompt engineering.
4. The structured prompt is sent to either an API-based LLM or a public LLM.
5. The LLM generates a response in English.
6. The English response is translated back into Darija using the `tarjam_english_darija` component.
7. The Darija response is stored in a Postgres database and displayed to the user through Streamlit.

This setup allows for the effective handling of queries in Darija, leveraging advanced language models for processing and translating responses back to the user's native language.

# RAG Schema
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
3. **The dataset** : For fine_tune the model we will use the ''' atlasia/darija_english ''' datasets

