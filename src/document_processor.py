import json
<<<<<<< HEAD

from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class Document(BaseModel): type: ignore
    id: int
    title: str
    tags: Optional[List[str]] = []
    published: Optional[bool] = False
    metadata: Dict[str, Any] = {}
=======
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Document(BaseModel):
 id: int
title: str
tags: Optional[List[str]] = []
published: Optional[bool] = False
metadata: Dict[str, Any] = {}
>>>>>>> bfa5463 (Added new assignment files and updates)

def load_documents(path: str) -> List[Document]:
    with open(path, 'r') as f:
        raw_data = json.load(f)
    return [Document(**item) for item in raw_data]

def display_documents(docs: List[Document]) -> None:
    for doc in docs:
        print(f"ID: {doc.id}")
        print(f"Title: {doc.title}")
        print(f"Tags: {doc.tags}")
        print(f"Published: {doc.published}")
        print(f"Metadata: {doc.metadata}")
        print("-" * 30)
