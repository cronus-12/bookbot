from stats import word_count, character_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    text = get_book_text()
    word_result = word_count(text)
    print(word_result)

    char_result = character_count(text)
    print(char_result)

main()