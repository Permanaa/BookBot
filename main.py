from stats import word_count, char_count, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def print_report(book_path: str, word_count: int, char_list: list[tuple[str, int]]):
    print("====== BOOKBOT ======")
    print(f"Analyzing book found at {book_path}...")
    print("------ Word Count ------")
    print(f"Found {word_count} total words")
    print("------ Character Count ------")
    for char in char_list:
        if not char[0].isalpha():
            continue
        else:
            print(f"{char[0]}: {char[1]}")
    print("====== END ======")

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    num_words = word_count(content)
    num_char = char_count(content)
    sorted_num_chars = chars_dict_to_sorted_list(num_char)

    print_report(book_path, num_words, sorted_num_chars)


main()
