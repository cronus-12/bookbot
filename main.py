import sys
from stats import word_count, character_count, sort_character_count

try:
    print(sys.argv[1])
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)

    word_result = word_count(text)
    print(word_result)

    char_result = character_count(text)
    print(char_result)

    sort_result = sort_character_count(char_result)
    for item in sort_result:
        char = item["char"]
        count = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

main()