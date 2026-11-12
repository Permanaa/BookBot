def get_book_text(file_path: str) -> str:
    file_content = ""
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

main()
