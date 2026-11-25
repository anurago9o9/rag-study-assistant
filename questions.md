# RAG Study Assistant - Evaluation Questions

## 1. Direct Questions

Question: What is Retrieval-Augmented Generation (RAG)?
Expected answer: An AI architecture that combines information retrieval with the text generation capabilities of Large Language Models.
Source: rag-basics.md

---

Question: What is chunk overlap?
Expected answer: The amount of text shared between consecutive chunks to preserve context across chunk boundaries.
Source: chunking.md

---

Question: What is the theoretical range of cosine similarity?
Expected answer: -1 to 1.
Source: embeddings.md

---

Question: What is the default embedding dimension of text-embedding-3-small?
Expected answer: 1536 dimensions.
Source: embeddings.md

---

Question: What is top-K retrieval?
Expected answer: A retrieval technique that returns the K most relevant results for a given query.
Source: embeddings.md

---

## 2. Paraphrased Questions

Question: How do we keep context when splitting text into smaller pieces?
Expected answer: By introducing overlap between consecutive chunks so that important information is preserved across chunk boundaries.
Source: chunking.md

---

Question: How can an AI chatbot access information that it was not trained on?
Expected answer: By using RAG to retrieve relevant information from external knowledge sources and providing it to the LLM as context.
Source: rag-basics.md

---

Question: How can we find relevant documents without matching the exact words in a search query?
Expected answer: By using semantic search, which compares embedding vectors based on their meaning rather than exact keyword matches.
Source: embeddings.md

---

Question: Why shouldn't we convert an entire large document into a single vector?
Expected answer: Large documents may contain multiple topics, which can dilute the semantic meaning of individual sections and reduce retrieval precision.
Source: chunking.md

---

Question: Can we update an AI application's knowledge without retraining its underlying model?
Expected answer: Yes. RAG allows external knowledge sources to be updated and retrieved without modifying the LLM's parameters.
Source: rag-basics.md

---

## 3. Multi-Passage and Cross-Document Questions

Question: What happens to a document from the moment it is loaded until it becomes searchable?
Expected answer: The document is loaded, split into smaller chunks, converted into embedding vectors, and stored in a vector database alongside its original text and metadata.
Source: rag-basics.md, chunking.md, embeddings.md

---

Question: How does chunk size affect the quality of semantic search?
Expected answer: Smaller chunks can improve retrieval precision but may lose context. Larger chunks preserve more context but may contain unrelated topics, reducing retrieval precision.
Source: chunking.md, embeddings.md

---

Question: How does a RAG application identify and retrieve relevant information for a user's question?
Expected answer: The question is converted into an embedding vector using a compatible embedding model. The vector is compared against stored document embeddings using a similarity metric, and the top-K relevant chunks are retrieved.
Source: rag-basics.md, embeddings.md

---

Question: Why might a RAG application generate an incorrect answer even when it uses a vector database?
Expected answer: Incorrect answers may result from poor document quality, inappropriate chunk sizes, weak embedding models, irrelevant retrieval results, or outdated and incomplete information.
Source: rag-basics.md, embeddings.md, chunking.md

---

Question: How can we reduce unnecessary LLM token consumption while maintaining answer quality?
Expected answer: Use appropriate chunk sizes and top-K retrieval to provide only relevant document sections to the LLM while preserving sufficient context.
Source: rag-basics.md, embeddings.md, chunking.md

---

## 4. Out-of-Context Questions

Question: What is the capital of Japan?
Expected behavior: Report that the documents do not contain the answer.
Source: None

---

Question: Who invented the Python programming language?
Expected behavior: Report that the documents do not contain the answer.
Source: None

---

Question: How does Kubernetes schedule pods across worker nodes?
Expected behavior: Report that the documents do not contain the answer.
Source: None

---

Question: What is the current price of Bitcoin?
Expected behavior: Report that the documents do not contain the answer.
Source: None

---

Question: What is the exact pricing of the OpenAI text-embedding-3-small model?
Expected behavior: Acknowledge that the documents mention the embedding model and its dimensions but do not provide pricing information.
Source: None
