from stats import word_count, char_count, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = word_count(content)
    print(f"Found {num_words} total words")

    num_char = char_count(content)
    sorted_num_chars = chars_dict_to_sorted_list(num_char)
    print(sorted_num_chars)


main()
