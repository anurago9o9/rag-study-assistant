# RAG Study Assistant

A small command-line project for learning Retrieval-Augmented Generation
(RAG). It answers questions using local Markdown notes and cites the
retrieved passages.

## How it works

Ingestion:
Markdown notes → chunks → embeddings → local Chroma database

Answering:
Question → retrieve relevant chunks → Groq chat model → cited answer

The application also prints the retrieved passages so retrieval and
generation can be inspected separately.

## Stack

- Python
- LangChain
- Sentence Transformers: `all-MiniLM-L6-v2`
- Chroma for local vector storage
- Groq for answer generation

Embeddings run locally. During answer generation, the question and
retrieved passages are sent to Groq.

## Project structure

```text
rag-study-assistant/
├── data/                # Markdown source documents
├── ingest.py            # Load, split, embed, and store documents
├── vector_store.py      # Shared embedding and database configuration
├── search.py            # Retrieve passages and generate answers
├── questions.md         # Manual evaluation questions
├── requirements.txt
├── .env.example
└── .gitignore
```

The local `.env` file and generated `chroma_db/` directory are excluded
from Git.

## Setup

Run these commands from the project folder.

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

The embedding model downloads on its first use.

### 3. Configure Groq

Copy the example configuration:

```powershell
Copy-Item .env.example .env
```

Edit `.env`:

```dotenv
GROQ_API_KEY=your_key_here
GROQ_MODEL=openai/gpt-oss-20b
```

Use a model available to your Groq account. API usage is subject to
your account's limits and pricing.

### 4. Build the index

Add Markdown files to `data/`, then run:

```powershell
python ingest.py
```

### 5. Ask a question

```powershell
python search.py
```

Example questions:

- What is chunk overlap?
- Can an application's knowledge change without model retraining?
- What is the exact pricing of text-embedding-3-small?

For the pricing question, the assistant should acknowledge that the
provided notes do not contain pricing information.

## Evaluation

Use `questions.md` to check:

- Whether retrieval finds supporting passages.
- Whether answers accurately reflect those passages.
- Whether citations support the claims.
- Whether unsupported questions receive an insufficient-information response.

## Updating notes and rebuilding the index

The current ingestion script does not remove outdated chunks.

Re-ingesting unchanged notes uses the same chunk IDs. However, editing
or deleting notes, or changing chunking settings, can leave old chunks
in the database.

For this small project, rebuild the index after those changes.

Stop any running ingestion or search process. From the project folder,
verify the database path:

```powershell
Get-Location
Resolve-Path -LiteralPath .\chroma_db
```

Confirm that it points to this project's generated `chroma_db` folder.
Then remove that folder and ingest again:

```powershell
Remove-Item -LiteralPath .\chroma_db -Recurse -Force
python ingest.py
```

This deletes the generated local index. Source notes in `data/` remain
available for rebuilding it.

Also rebuild the index if the embedding model or its configuration changes.

## Limitations

- Processes Markdown files directly inside `data/`.
- Retrieves the top three chunks for each question.
- Handles one question per run.
- Does not support conversation memory or incremental document cleanup.
- LLM instructions encourage grounded answers but do not guarantee accuracy.
- Dependencies are not pinned to exact versions.