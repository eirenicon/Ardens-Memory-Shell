import json
import uuid
import hashlib
from datetime import datetime, timezone
from typing import List, Dict

MEMORY_FILE = "memory_db.json"

class MemoryEntry:
    def __init__(self, agent: str, content: str, tags: List[str], version: str = "0.2"):
        self.id = str(uuid.uuid4())
        self.agent = agent
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.content = content
        self.tags = tags
        self.version = version
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        hash_input = f"{self.agent}{self.timestamp}{self.content}{','.join(self.tags)}{self.version}"
        return hashlib.sha256(hash_input.encode()).hexdigest()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "agent": self.agent,
            "timestamp": self.timestamp,
            "content": self.content,
            "tags": self.tags,
            "hash": self.hash,
            "version": self.version
        }

class MemoryShell:
    def __init__(self, filepath: str = MEMORY_FILE):
        self.filepath = filepath
        self.memories = self.load_memories()

    def load_memories(self) -> List[Dict]:
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_memories(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.memories, f, indent=2)

    def add_memory(self, entry: MemoryEntry):
        self.memories.append(entry.to_dict())
        self.save_memories()

    def list_all(self) -> List[Dict]:
        return self.memories

    def get_by_tag(self, tag: str) -> List[Dict]:
        return [m for m in self.memories if tag in m['tags']]

    def search_content(self, query: str) -> List[Dict]:
        return [m for m in self.memories if query.lower() in m['content'].lower()]

if __name__ == "__main__":
    shell = MemoryShell()
    import argparse

    parser = argparse.ArgumentParser(description="Memory Shell CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("agent")
    add_parser.add_argument("content")
    add_parser.add_argument("tags", nargs='+')

    list_parser = subparsers.add_parser("list")

    tag_parser = subparsers.add_parser("tag")
    tag_parser.add_argument("tag")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")

    args = parser.parse_args()

    if args.command == "add":
        entry = MemoryEntry(agent=args.agent, content=args.content, tags=args.tags)
        shell.add_memory(entry)
        print("Memory added.")

    elif args.command == "list":
        for m in shell.list_all():
            print(json.dumps(m, indent=2))

    elif args.command == "tag":
        results = shell.get_by_tag(args.tag)
        print(f"Found {len(results)} entries with tag '{args.tag}':")
        for m in results:
            print(json.dumps(m, indent=2))

    elif args.command == "search":
        results = shell.search_content(args.query)
        print(f"Found {len(results)} entries matching '{args.query}':")
        for m in results:
            print(json.dumps(m, indent=2))
