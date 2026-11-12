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

def sort_on(list: tuple[str, int]) -> int:
    return list[1]

def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str, int]]:
    list_of_tuple_char = []
    for key, val in chars.items():
        list_of_tuple_char.append((key, val))
    sorted_list = sorted(list_of_tuple_char, reverse=True, key=sort_on)
    return sorted_list
