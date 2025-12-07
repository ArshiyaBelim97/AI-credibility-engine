# small utilities used across the backend

def safe_truncate_text(text: str, max_len: int = 10000) -> str:
    return text if len(text) <= max_len else text[:max_len]
