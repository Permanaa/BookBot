def get_book_text(file_path: str) -> str:
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def word_count(text: str) -> int:
    split_text = text.split()
    return len(split_text)

def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = word_count(content)
    print(f"Found {num_words} total words")

main()
