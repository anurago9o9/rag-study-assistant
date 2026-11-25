# Retrieval-Augmented Generation (RAG)

## What is RAG?

Retrieval-Augmented Generation (RAG) is an AI architecture that combines information retrieval with the text generation capabilities of Large Language Models (LLMs).

Traditional LLMs generate responses based on the knowledge acquired during their training. However, they may not have access to recent information, private documents, or organization-specific knowledge. RAG addresses this limitation by retrieving relevant information from external knowledge sources before generating a response.

Unlike fine-tuning, RAG does not require modifying the model's parameters whenever new information becomes available.

## How Does RAG Work?

A typical RAG system consists of two major pipelines: the ingestion pipeline and the retrieval-generation pipeline.

### Ingestion Pipeline

The ingestion pipeline prepares documents for future retrieval.

1. Load documents from sources such as Markdown files, PDFs, databases, or APIs.
2. Split large documents into smaller text chunks.
3. Convert each chunk into a numerical vector using an embedding model.
4. Store the vectors, original text, and associated metadata in a vector database.

This process is generally performed before users start asking questions.

### Retrieval and Generation Pipeline

When a user submits a question, the following steps occur:

1. Convert the user's question into an embedding vector.
2. Search the vector database for semantically similar document chunks.
3. Retrieve the top K most relevant chunks.
4. Construct a prompt containing the retrieved context and the user's question.
5. Send the prompt to an LLM to generate an answer.

The retrieved documents provide additional knowledge that helps the LLM generate a more informed response.

## Components of a RAG System

A RAG application typically contains the following components:

- Document Loader: Reads information from external sources.
- Text Splitter: Divides documents into manageable chunks.
- Embedding Model: Converts text into numerical vectors.
- Vector Database: Stores and searches embedding vectors.
- Retriever: Selects relevant document chunks.
- Prompt Template: Combines retrieved context with the question.
- Large Language Model: Generates the final response.

Popular vector storage solutions include ChromaDB, FAISS, Pinecone, Qdrant, and PostgreSQL with pgvector.

## Practical Example

Consider an employee asking an internal company chatbot:

"How many paid leaves am I allowed per year?"

The RAG system retrieves relevant sections from the company's HR policy documents. These sections are passed to the LLM along with the employee's question.

Instead of relying on general knowledge, the LLM can generate an answer based on the company's actual leave policy.

## Advantages of RAG

- Provides access to private and domain-specific information.
- Reduces the likelihood of hallucinations.
- Allows knowledge to be updated without retraining the LLM.
- Supports source attribution and citations.
- Can be more cost-effective than frequent model fine-tuning.

## Limitations of RAG

RAG does not guarantee accurate answers. Poor document quality, inappropriate chunk sizes, weak embedding models, or irrelevant retrieval results can negatively affect response quality.

Retrieved information may also be outdated, contradictory, or incomplete. Therefore, retrieval quality and answer faithfulness should be evaluated separately.

## Common Use Cases

RAG is commonly used in enterprise knowledge assistants, customer support chatbots, technical documentation search, research assistants, and educational applications.

A study assistant that answers questions using locally stored Markdown notes is a simple example of a RAG application.
