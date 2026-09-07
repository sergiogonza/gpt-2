# Production Deploy

## Architecture

Netlify frontend/functions

```
/api/chat
    |
    v
GPT2_API_URL
    |
    v
FastAPI RAG GPT-2 service
    |
    +-- FAISS
    +-- Embeddings
    +-- GPT-2 weights
```

## Netlify environment variable

Create:

```
GPT2_API_URL=https://your-python-api-domain.com
```

The value must point to the deployed FastAPI service.

## Test endpoint

POST:

```
/chat
```

Body:

```json
{
  "message": "Explica qué es RAG"
}
```
