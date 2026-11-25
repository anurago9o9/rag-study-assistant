# Text Embeddings and Semantic Search

## What Are Embeddings?

Embeddings are numerical vector representations of data such as text, images, or audio. In natural language processing, text embeddings represent the semantic meaning of words, sentences, paragraphs, or documents.

An embedding model converts input text into a fixed-length array of floating-point numbers.

For example, a simplified text embedding might look like:

[0.12, -0.45, 0.78, 0.23, -0.16]

Real embedding models typically produce vectors containing hundreds or thousands of dimensions.

Individual dimensions generally do not have directly interpretable meanings. Instead, the overall position of a vector in the embedding space represents information learned by the model.

## Semantic Search vs Keyword Search

Traditional keyword search retrieves documents based on exact or related word matches.

Semantic search retrieves documents based on their meaning, even when they do not contain the exact words used in the query.

For example, consider the following query:

"How can I reduce API response time?"

A semantic search system might retrieve a document titled:

"Improving backend performance using Redis caching."

Although the query and document use different words, their meanings are related.

Keyword search remains useful for exact identifiers, error codes, product names, and technical terms. Hybrid search combines keyword search with semantic search to improve retrieval quality.

## How Embeddings Are Used in RAG

During document ingestion, each text chunk is passed to an embedding model. The resulting vector is stored alongside the original text and metadata.

When a user submits a question, the same compatible embedding model converts the question into a vector.

The system compares the question vector against stored document vectors and retrieves the most relevant chunks.

Using compatible embedding models for documents and queries is important because their vectors must belong to the same embedding space.

## Vector Similarity Metrics

Similarity metrics determine how closely two vectors are related.

### Cosine Similarity

Cosine similarity measures the cosine of the angle between two vectors.

Formula:

cosine_similarity(A, B) = dot(A, B) / (norm(A) * norm(B))

Its theoretical range is -1 to 1.

- A value of 1 indicates identical vector direction.
- A value of 0 indicates orthogonal vectors.
- A value of -1 indicates opposite vector direction.

Higher cosine similarity generally indicates greater semantic similarity for text embeddings.

### Euclidean Distance

Euclidean distance measures the straight-line distance between two vectors. Smaller distances indicate closer vectors.

### Dot Product

The dot product measures vector alignment while also considering vector magnitude. For unit-normalized vectors, the dot product equals cosine similarity.

## Popular Embedding Models

Common embedding models include:

- OpenAI text-embedding-3-small: Produces 1536-dimensional vectors by default.
- OpenAI text-embedding-3-large: Produces 3072-dimensional vectors by default.
- Sentence Transformers all-MiniLM-L6-v2: Produces 384-dimensional vectors and can run locally.

Model selection depends on retrieval quality, computational requirements, cost, and privacy constraints.

## Vector Databases

Vector databases store embeddings and support efficient similarity searches.

Each stored record can contain:

- A unique identifier.
- The embedding vector.
- Original document text.
- Metadata such as filename, section, and document ID.

Vector databases may use approximate nearest neighbor algorithms to search large collections efficiently.

## What Is Top-K Retrieval?

Top-K retrieval returns the K most relevant results for a query.

For example, setting K to 3 retrieves the three highest-ranked document chunks.

A small K may miss important information, while a large K may introduce irrelevant context and increase LLM token consumption.

## Limitations of Embeddings

Embeddings do not guarantee factual correctness. Similar vectors may represent related but factually different statements.

Similarity scores are also model-dependent. A score of 0.8 should not automatically be interpreted as 80 percent confidence in an answer.

Retrieval quality should be evaluated using representative questions and expected relevant documents.
