# Corpus Engine

Knowledge ingestion layer for GPT-2 assistant.

Initial supported sources:

- text
- code
- json

Pipeline:

source -> loader -> cleaner -> chunks -> metadata -> embeddings -> RAG
