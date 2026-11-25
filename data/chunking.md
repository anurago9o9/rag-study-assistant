# Document Chunking in RAG

## What Is Chunking?

Chunking is the process of dividing large documents into smaller, manageable pieces of text called chunks.

In a Retrieval-Augmented Generation (RAG) system, documents are usually split into chunks before generating embeddings and storing them in a vector database.

Each chunk acts as an independent unit of information that can be retrieved when a user submits a relevant question.

## Why Is Chunking Necessary?

Large documents often contain multiple topics. Creating a single embedding for an entire document may dilute the semantic meaning of individual sections.

Chunking solves several problems:

- Embedding models have maximum input token limits.
- Smaller chunks allow more precise information retrieval.
- LLMs have limited context windows.
- Retrieving relevant sections reduces unnecessary token consumption.
- Smaller units of information make source attribution easier.

For example, a 50-page technical document might contain information about authentication, database indexing, caching, and deployment.

If a user asks about authentication, retrieving only the relevant authentication chunks is more efficient than passing the entire document to the LLM.

## Chunk Size

Chunk size determines the maximum or target amount of text included in each chunk.

Chunk size can be measured in characters, words, or tokens, depending on the text splitting implementation.

Small chunks generally provide more precise retrieval but may lose important surrounding context.

Large chunks preserve more context but may contain multiple unrelated topics, reducing retrieval precision.

A reasonable starting point for general technical documents is approximately 300 to 500 tokens per chunk. However, the optimal chunk size depends on the document structure, embedding model, and application requirements.

## Chunk Overlap

Chunk overlap is the amount of text shared between consecutive chunks.

Overlap helps preserve information that might otherwise be lost at chunk boundaries.

For example, consider a document containing 1200 characters with a chunk size of 500 characters and an overlap of 100 characters.

The chunks would approximately cover:

- Chunk 1: Characters 0 to 499.
- Chunk 2: Characters 400 to 899.
- Chunk 3: Characters 800 to 1199.

Each consecutive chunk shares 100 characters with the previous chunk.

A common starting point is an overlap of 10 to 20 percent of the chunk size.

Excessive overlap increases storage requirements and may cause the retriever to return duplicate information.

## Common Chunking Strategies

### Fixed-Size Chunking

Fixed-size chunking divides text into chunks containing a predefined number of characters or tokens.

It is simple and computationally inexpensive but may split sentences or paragraphs at inappropriate positions.

### Recursive Character Chunking

Recursive character chunking attempts to split text using a hierarchy of separators.

Common separators include:

1. Double newline.
2. Single newline.
3. Space.
4. Individual characters.

This approach attempts to preserve paragraphs and sentences while respecting the configured chunk size.

LangChain provides a RecursiveCharacterTextSplitter for this purpose.

### Semantic Chunking

Semantic chunking divides text based on changes in meaning rather than relying only on fixed text lengths.

It can use embedding similarity between consecutive sentences to identify topic boundaries.

Semantic chunking can preserve meaningful information but generally requires additional computation.

### Document Structure-Based Chunking

This strategy splits documents according to their natural structure, such as Markdown headings, HTML sections, or chapters.

It is particularly useful for technical documentation and structured knowledge bases.

## Chunk Metadata

Each chunk should contain metadata that identifies its source.

Useful metadata includes:

- Source filename.
- Document identifier.
- Chunk index.
- Section heading.
- Page number, if applicable.

Metadata supports filtering, debugging, source attribution, and document updates.

## Chunking Example Using LangChain

Install the required package:

pip install langchain-text-splitters

Python example:

    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(document_text)

By default, this configuration measures chunk size using character length rather than token count.

## Evaluating Chunking Quality

There is no universally optimal chunk size.

Experiment with different chunk sizes and overlap values, then evaluate whether relevant information is retrieved for representative questions.

Good chunking should balance retrieval precision, context preservation, storage cost, and LLM token consumption.
