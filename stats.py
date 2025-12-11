def word_count():
    total_words = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        total_words += 1
    total_word_count = f"Found {total_words} total words"
    print(total_word_count)