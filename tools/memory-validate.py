#!/usr/bin/env python3

import json
import os
import sys
import uuid
from datetime import datetime

REQUIRED_FIELDS = {
    "id": str,
    "agent": str,
    "timestamp": str,
    "content": str,
    "tags": list,
    "hash": str,
    "version": str
}

def validate_entry(entry):
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in entry:
            print(f"Missing field: {field}")
            return False
        if not isinstance(entry[field], field_type):
            print(f"Field '{field}' should be of type {field_type.__name__}")
            return False
    try:
        uuid.UUID(entry["id"])
        datetime.fromisoformat(entry["timestamp"])
    except Exception as e:
        print(f"Invalid id or timestamp: {e}")
        return False
    return True

def validate_file(filepath):
    with open(filepath, 'r') as f:
        try:
            data = json.load(f)
            if validate_entry(data):
                print(f"{filepath}: ✅ Valid")
            else:
                print(f"{filepath}: ❌ Invalid")
        except json.JSONDecodeError as e:
            print(f"{filepath}: ❌ JSON Decode Error - {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: memory-validate.py path/to/entry.json")
        sys.exit(1)
    for path in sys.argv[1:]:
        validate_file(path)
