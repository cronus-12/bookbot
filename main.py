from stats import word_count, character_count, sort_character_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    text = get_book_text()

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