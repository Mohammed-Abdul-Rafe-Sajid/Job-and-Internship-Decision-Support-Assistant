## Retrieval Mechanism

The chatbot retrieves relevant career information by computing cosine
similarity between the user query embedding and stored job role
embeddings.

The top-k most similar job descriptions are selected and passed to the
LLM as contextual grounding, enabling accurate and explainable
responses.
