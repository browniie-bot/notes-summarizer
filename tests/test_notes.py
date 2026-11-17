from summarizer.notes import chunks


def test_short_notes_stay_whole():
    assert chunks("a\n\nb") == ["a\n\nb"]


def test_long_notes_split_on_blank_lines():
    text = "\n\n".join(["x" * 900] * 3)
    assert [len(piece) for piece in chunks(text)] == [1802, 900]
