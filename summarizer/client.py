"""Summarize notes with Claude."""

import anthropic

from summarizer.notes import chunks

MODEL = "claude-haiku-4-5-20251001"


class Summarizer:
    """Turn long notes into a short summary."""

    def __init__(self, api_key: str, model: str = MODEL) -> None:
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def summarize(self, text: str) -> str:
        """Summarize each piece of the notes, then join the summaries."""
        parts = []
        for piece in chunks(text):
            reply = self.client.messages.create(
                model=self.model,
                max_tokens=300,
                temperature=0.2,
                system="Summarize these meeting notes in two sentences.",
                messages=[{"role": "user", "content": piece}],
            )
            parts.append("".join(block.text for block in reply.content if block.type == "text"))
        return "\n".join(parts)
