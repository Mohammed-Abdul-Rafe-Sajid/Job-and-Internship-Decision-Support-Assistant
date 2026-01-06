# backend/chatbot.py
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from backend.embeddings import embed_text
from backend.retrieval import retrieve_relevant_jobs

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

CHAT_DEPLOYMENT = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

def get_chat_response(user_message, chat_history=None):
    if chat_history is None:
        chat_history = []

    query_embedding = embed_text(user_message)
    relevant_jobs = retrieve_relevant_jobs(query_embedding)

    context_block = "\n".join(relevant_jobs)

    system_prompt = f"""
You are a Job and Internship Decision Support Assistant.

You are given VERIFIED career data below.
Base your reasoning ONLY on this data.
If data is insufficient, clearly say so.

--- Career Data ---
{context_block}
-------------------

Structure responses as:
1) Summary
2) Assumptions
3) Key factors
4) Pros
5) Cons
6) Risks / trade-offs
7) Recommendation + confidence
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history[-6:])
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=messages,
        temperature=0.6,
        max_tokens=600,
    )

    return response.choices[0].message.content
