# backend/embeddings.py
import os
import csv
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")

def embed_text(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=text
    )
    return response.data[0].embedding


def load_job_data(csv_path="data/job_roles.csv"):
    records = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(
                f"Role: {row['role']}. "
                f"Skills: {row['required_skills']}. "
                f"Average salary: {row['average_salary_inr']} INR. "
                f"Growth outlook: {row['growth_outlook']}. "
                f"Notes: {row['notes']}."
            )
    return records


def build_job_embeddings():
    texts = load_job_data()
    embeddings = [embed_text(t) for t in texts]
    return texts, embeddings
