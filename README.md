# Job & Internship Decision Support Assistant

This project is an LLM-powered decision support chatbot designed to help students and early-career professionals make informed choices about jobs and internships. Instead of providing generic career advice, the assistant grounds its responses in structured career data and explains its recommendations transparently.

The system is built using Azure OpenAI via Microsoft Foundry and follows a Retrieval-Augmented Generation (RAG) approach. User queries are matched against a curated dataset of job roles and internships, and the retrieved information is used to generate context-aware, realistic, and balanced recommendations.

The focus of this project is not UI polish or feature breadth, but clear problem definition, correct use of AI services, and explainable decision-making. The chatbot is exposed as a REST API using FastAPI and tested via Swagger UI for simplicity and clarity.

## Problem Statement

In India, students and early-career professionals often struggle to make informed decisions about jobs and internships due to limited transparency around roles, required skills, salary expectations, and long-term growth. Many career decisions are influenced by peer opinions, social media trends, or incomplete information rather than structured analysis.

This problem is especially visible when students must choose between options such as unpaid internships versus paid roles, data analyst versus machine learning paths, or short-term opportunities versus long-term career growth. While information exists online, it is scattered, inconsistent, and rarely contextualized to an individual’s background or goals.

The goal of this project is to address this gap by building an AI-powered decision support assistant that provides grounded, explainable, and India-specific career guidance. Instead of offering generic advice, the chatbot uses curated job and internship data (including skills, salary ranges in INR, and growth outlook) to help users evaluate trade-offs and make more rational decisions.

### Target Users
- Undergraduate and final-year students in India
- Early-career professionals exploring data, software, or AI roles
- Individuals comparing internships, entry-level jobs, or career transitions

### Why This Problem Was Chosen
Career decisions have long-term consequences, yet many students make them with incomplete or biased information. By combining structured career data with large language models, this project demonstrates how AI can be used responsibly as a decision-support tool rather than a replacement for human judgment.


## System Design & Architecture

This project follows a simple and modular Retrieval-Augmented Generation (RAG) architecture to ensure clarity, correctness, and explainability. The system is designed to be lightweight, easy to understand, and aligned with real-world usage rather than over-engineered complexity.

### High-Level Flow

1. The user sends a career-related query (e.g., job choice, internship decision).
2. The query is converted into an embedding using an Azure OpenAI embedding model.
3. Relevant career data is retrieved from a structured dataset using vector similarity.
4. The retrieved data is injected into the system prompt as grounded context.
5. An Azure OpenAI chat model generates a structured, explainable response.
6. The response is returned via a REST API endpoint.

### Architecture Diagram (Logical)

User Query
↓
FastAPI (/chat endpoint)
↓
Embedding Model (Azure OpenAI)
↓
Vector Similarity Search (in-memory)
↓
Relevant Career Context
↓
LLM (Azure OpenAI Chat Model)
↓
Structured Career Recommendation


### Key Design Principles

- **Simplicity over complexity**: The system uses in-memory retrieval instead of heavy databases to keep the design transparent and easy to evaluate.
- **Explainability**: Responses are structured into summaries, pros/cons, risks, and recommendations.
- **Grounded responses**: The LLM is instructed to rely only on retrieved career data when making recommendations.
- **Modular design**: Each component (API, embeddings, retrieval, prompting) is isolated and easy to reason about.

### Project Structure Overview

- `backend/app.py`  
  Exposes the FastAPI endpoint and handles request/response flow.

- `backend/chatbot.py`  
  Orchestrates the RAG pipeline: embedding → retrieval → prompt construction → LLM call.

- `backend/embeddings.py`  
  Loads career data and generates embeddings using Azure OpenAI.

- `backend/retrieval.py`  
  Performs cosine similarity search to retrieve the most relevant roles.

- `data/job_roles.csv`  
  Structured career dataset containing roles, skills, salary (INR), and growth outlook.

- `docs/`  
  Contains step-by-step documentation explaining problem definition, design, data, embeddings, retrieval, and prompting.

This architecture demonstrates a practical, production-inspired RAG workflow while remaining easy to understand, test, and extend.


## AI & Cloud Services Used

This project is built entirely using modern cloud-based AI services, with Azure AI Foundry and Azure OpenAI as the core platform. The focus is on practical usage of large language models, embeddings, and retrieval mechanisms rather than experimental features.

### Azure AI Foundry / Azure OpenAI

Azure OpenAI is used for both language understanding and embedding generation. The project uses two deployed models:

- **Chat Model**  
  Used to generate structured, explainable career recommendations based on user input and retrieved context.

- **Embedding Model**  
  Used to convert user queries and career data into vector representations for similarity-based retrieval.

Both models are deployed under an Azure OpenAI resource and accessed securely via API keys and environment variables.

### Large Language Model (LLM)

The chat model is responsible for:
- Understanding user career-related questions
- Reasoning over retrieved career data
- Producing structured outputs (summary, pros, cons, risks, recommendation)
- Asking clarifying questions when information is insufficient

The LLM is guided using a carefully designed system prompt that enforces realism, transparency, and non-generic responses.

### Embedding Model

An embedding model is used to:
- Convert structured career role descriptions into numerical vectors
- Embed incoming user queries at runtime
- Enable semantic matching between user intent and available career data

This allows the chatbot to retrieve relevant roles even when the user’s wording does not exactly match the dataset.

### Retrieval Mechanism (RAG)

A simple but effective Retrieval-Augmented Generation (RAG) pipeline is implemented:

- Career data is stored in a structured CSV file
- Embeddings are generated once at startup
- Cosine similarity is used to retrieve the most relevant roles
- Retrieved data is injected into the system prompt as grounded context

This ensures the model’s responses are based on real data rather than hallucinated knowledge.

### Backend Framework

- **FastAPI** is used to expose the chatbot as a REST API
- Provides automatic request validation and Swagger UI for testing
- Keeps the system easy to run, test, and review

### Environment & Configuration

- All secrets and configuration values are stored in environment variables
- The project follows best practices for API key handling and deployment flexibility

Overall, the system demonstrates a clean, end-to-end integration of cloud-hosted LLMs, embeddings, and retrieval techniques using Azure AI services.



## Bonus: External / Real-World Data Integration

As part of the optional bonus requirement, this project integrates an external data source to ground the chatbot’s recommendations in real-world career information.

### Data Source

The chatbot uses a structured **CSV dataset** containing information about job roles and internships relevant to students and early-career professionals in India.

The dataset includes:
- Job role name
- Required skills
- Average salary (INR)
- Growth outlook
- Additional notes about the role

This data represents realistic career options commonly seen in the Indian job market and is designed to reflect practical decision-making scenarios faced by students.

### Why CSV Was Chosen

A CSV-based data source was chosen because:
- It is simple, transparent, and easy to audit
- It closely mirrors real-world datasets used in early-stage systems
- It avoids unnecessary infrastructure complexity while still enabling RAG
- It aligns with the assessment’s emphasis on clarity over scale

This approach allows the system to focus on reasoning quality rather than data engineering overhead.

### How Data Flows Through the System

1. Career data is stored in a CSV file inside the project repository
2. Each row is converted into a descriptive text representation
3. Embeddings are generated for each role using Azure OpenAI
4. User queries are embedded at runtime
5. Cosine similarity is used to retrieve the most relevant roles
6. Retrieved data is injected into the LLM prompt as verified context
7. The LLM produces grounded, explainable recommendations

### Meaningful Use of External Data

The chatbot does not answer questions in isolation.  
All recommendations are explicitly based on retrieved career data, including salary, skills, and growth outlook.

If the available data is insufficient for a confident recommendation, the chatbot clearly states this and asks follow-up questions instead of hallucinating.

This ensures:
- Transparency
- Trustworthy responses
- Real-world relevance

This bonus integration demonstrates how even lightweight external data sources can significantly improve the reliability and usefulness of LLM-powered systems.


## Prompting Strategy

The chatbot uses a structured system prompt designed to enforce realism, transparency, and grounded reasoning. Rather than generating free-form advice, the model is guided to behave as a decision-support assistant.

### Core Prompt Design Principles

- Responses must be grounded in retrieved career data
- If information is insufficient, the model must ask clarifying questions
- Recommendations must be conditional and explicit about assumptions
- Generic motivational language is avoided
- Trade-offs and risks are always highlighted

### Response Structure Enforced

Every recommendation follows a fixed structure:

1) Brief summary of the situation  
2) Assumptions made (if any)  
3) Key factors considered  
4) Pros  
5) Cons  
6) Risks or trade-offs  
7) Tentative recommendation with confidence level

This structure ensures consistency, explainability, and makes it easier for users to understand *why* a recommendation was given.

### Grounding with Retrieved Context

Retrieved career data is injected directly into the system prompt.  
The model is explicitly instructed to base its reasoning only on this data and to state clearly when the data is insufficient.

This reduces hallucination and encourages disciplined reasoning.

#### For example interactions, see docs/06_prompting



## Setup and Run Instructions

### Prerequisites
- Python 3.9+
- Azure OpenAI access (free trial is sufficient)

### Installation

1. Clone the repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file based on .env.example and fill in:
- Azure OpenAI endpoint
- API key
- Deployment names
- Running the Application

4. Start the FastAPI server:

``` bash
uvicorn backend.app:app --reload
```

5. Open the Swagger UI at:


http://127.0.0.1:8000/docs

6. Use the /chat endpoint to test the chatbot.


## Design Decisions and Trade-offs

- CSV-based data storage was chosen over databases to keep the system simple and transparent
- In-memory vector retrieval was preferred to avoid unnecessary infrastructure
- The system prioritizes explainability over aggressive optimization
- The chatbot acts as a decision-support tool, not a decision-maker

These choices align with the assessment’s emphasis on clarity, correctness, and learning over complexity.



## Limitations

- The dataset is intentionally small and curated
- Recommendations are limited to the roles present in the dataset
- The system does not currently support long-term user memory

These limitations were accepted to keep the project focused and easy to evaluate.


