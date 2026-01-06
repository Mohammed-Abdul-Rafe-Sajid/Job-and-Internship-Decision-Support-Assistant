# backend/retrieval.py
import math
from backend.embeddings import build_job_embeddings

JOB_TEXTS, JOB_EMBEDDINGS = build_job_embeddings()

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)

def retrieve_relevant_jobs(query_embedding, top_k=3):
    scored = []
    for i, emb in enumerate(JOB_EMBEDDINGS):
        score = cosine_similarity(query_embedding, emb)
        scored.append((score, JOB_TEXTS[i]))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [text for _, text in scored[:top_k]]
