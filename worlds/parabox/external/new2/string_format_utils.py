def remove_whitespace(text: str):
    return "\n".join(
        (line for line in (line.strip() for line in text.split("\n")) if line)
    )
