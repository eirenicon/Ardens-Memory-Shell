#!/usr/bin/env python3

import os
import json
import sys

def search_memory(base_dir, tag=None, keyword=None):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    try:
                        entry = json.load(f)
                        if tag and tag in entry.get("tags", []):
                            print(f"Match on tag in: {filepath}")
                        elif keyword and keyword.lower() in entry.get("content", "").lower():
                            print(f"Match on keyword in: {filepath}")
                    except:
                        continue

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: memory-search.py entries/ --tag some_tag")
        print("   or: memory-search.py entries/ --keyword search_term")
        sys.exit(1)
    mode = sys.argv[2]
    value = sys.argv[3]
    if mode == "--tag":
        search_memory(sys.argv[1], tag=value)
    elif mode == "--keyword":
        search_memory(sys.argv[1], keyword=value)
