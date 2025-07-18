#!/usr/bin/env python3

import json
import uuid
import hashlib
import datetime
from pathlib import Path

def compute_hash(data):
    relevant_fields = {
        k: data[k]
        for k in ['agent', 'content', 'tags', 'timestamp', 'version']
    }
    json_str = json.dumps(relevant_fields, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(json_str.encode('utf-8')).hexdigest()

def create_entry(agent, content, tags, version="1.0"):
    now = datetime.datetime.utcnow().isoformat()
    entry = {
        "id": str(uuid.uuid4()),
        "agent": agent,
        "content": content,
        "tags": tags,
        "timestamp": now,
        "version": version,
    }
    entry["hash"] = compute_hash(entry)
    return entry

def write_entry(entry):
    ts = datetime.datetime.fromisoformat(entry["timestamp"])
    path = Path(f"entries/{ts.year}/{ts.month:02d}/")
    path.mkdir(parents=True, exist_ok=True)
    filename = path / f"{entry['id']}.json"
    with open(filename, 'w') as f:
        json.dump(entry, f, indent=2)
    print(f"✅ Entry written to {filename}")

if __name__ == "__main__":
    agent = input("Agent name: ")
    content = input("Content: ")
    tags = input("Tags (comma separated): ").split(',')
    entry = create_entry(agent, content, [t.strip() for t in tags])
    write_entry(entry)
