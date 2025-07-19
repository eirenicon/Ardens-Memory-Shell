from memory_shell import MemoryShell, MemoryEntry

sample_memories = [
    {
        "agent": "arthur",
        "content": "Ardens project focuses on resilient, modular AI-human collaboration.",
        "tags": ["ardens", "project", "overview"]
    },
    {
        "agent": "arthur",
        "content": "Memory Shell CLI stores timestamped notes with tags and agent provenance.",
        "tags": ["memory-shell", "cli", "design"]
    },
    {
        "agent": "arthur",
        "content": "Future improvements include search enhancements, pruning, and UI integration.",
        "tags": ["memory-shell", "roadmap", "future"]
    },
    {
        "agent": "arthur",
        "content": "OSINT feeds integration for the Hybrid Attack Panel is under active review.",
        "tags": ["osint", "hap", "security"]
    },
    {
        "agent": "arthur",
        "content": "Maintain rigorous provenance for every memory entry using SHA-256 hashes.",
        "tags": ["memory-shell", "security", "integrity"]
    }
]

def bulk_load():
    shell = MemoryShell()
    for mem in sample_memories:
        entry = MemoryEntry(agent=mem["agent"], content=mem["content"], tags=mem["tags"])
        shell.add_memory(entry)
    print(f"Loaded {len(sample_memories)} sample memories.")

if __name__ == "__main__":
    bulk_load()
