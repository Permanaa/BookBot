def word_count(text: str) -> int:
    split_text = text.split()
    return len(split_text)

def char_count(text: str) -> dict[str, int]:
    lower_text = text.lower()
    result = {}
    for i in lower_text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
