import json
from datetime import datetime, timezone

MEMORY_FILE = "memory_db.json"
EXPORT_FILE = "memory_export.md"

def export_memories_to_md():
    try:
        with open(MEMORY_FILE, 'r') as f:
            memories = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No memories found or invalid JSON.")
        return

    with open(EXPORT_FILE, 'w') as f:
        f.write(f"# Memory Export - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n")
        for m in memories:
            f.write(f"## Memory ID: {m['id']}\n")
            f.write(f"- **Agent:** {m['agent']}\n")
            f.write(f"- **Timestamp:** {m['timestamp']}\n")
            f.write(f"- **Tags:** {', '.join(m['tags'])}\n\n")
            f.write(f"{m['content']}\n\n")
            f.write("---\n\n")

    print(f"Exported {len(memories)} memories to {EXPORT_FILE}")

if __name__ == "__main__":
    export_memories_to_md()
