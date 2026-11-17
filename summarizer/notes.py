"""Split meeting notes into pieces short enough to summarize one at a time."""


def chunks(text: str, size: int = 2000) -> list[str]:
    """Split text on blank lines into pieces of at most `size` characters."""
    pieces: list[str] = []
    current = ""
    for paragraph in text.split("\n\n"):
        if current and len(current) + len(paragraph) + 2 > size:
            pieces.append(current)
            current = paragraph
        else:
            current = f"{current}\n\n{paragraph}" if current else paragraph
    if current:
        pieces.append(current)
    return pieces
