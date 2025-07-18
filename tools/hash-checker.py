#!/usr/bin/env python3

import json
import hashlib
import sys
from pathlib import Path

def compute_hash(entry):
    relevant_fields = {
        k: entry[k]
        for k in ['agent', 'content', 'tags', 'timestamp', 'version']
        if k in entry
    }
    json_str = json.dumps(relevant_fields, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(json_str.encode('utf-8')).hexdigest()

def main(json_path):
    path = Path(json_path)
    if not path.exists():
        print(f"File not found: {json_path}")
        return

    with open(path, 'r') as f:
        entry = json.load(f)

    stored_hash = entry.get('hash', '')
    computed_hash = compute_hash(entry)

    print(f"Stored Hash  : {stored_hash}")
    print(f"Computed Hash: {computed_hash}")
    if stored_hash == computed_hash:
        print("✅ Hash verified.")
    else:
        print("❌ Hash mismatch!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 hash-checker.py path/to/entry.json")
    else:
        main(sys.argv[1])
