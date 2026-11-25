from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import hashlib
from vector_store import vector_store

BASE_DIR = Path(__file__).resolve().parent

documents = [
    Document(
        page_content=path.read_text(encoding="utf-8"),
        metadata={"source": path.name},
    )
  for path in sorted((BASE_DIR / "data").glob("*.md"))
]

print(f"Loaded {len(documents)} documents")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

for chunk in chunks[:3]:
    print(chunk.metadata)
    print(chunk.page_content)
    print()

if not chunks:
    raise ValueError("No chunks found. Check your data folder.")

# Identical chunks get identical IDs, preventing duplicate entries
# when you ingest unchanged files again.
ids = [
    hashlib.sha256(
        f"{chunk.metadata['source']}:{chunk.page_content}".encode("utf-8")
    ).hexdigest()
    for chunk in chunks
]

vector_store.add_documents(
    documents=chunks,
    ids=ids,
)

print(f"Saved {len(chunks)} chunks to Chroma.")