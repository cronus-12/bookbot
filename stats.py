def word_count(text):
    total_words = 0
    words = text.split()
    for word in words:
        total_words += 1
    total_word_count = f"Found {total_words} total words"
    return total_word_count

def character_count(text):
    characters = {}
    lower_case = text.lower()
    for character in lower_case:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(characters):
    return characters["num"]

def sort_character_count(characters):
    sorted_list = []
    for char, count in characters.items():
        sorting_list = {
            "char": char,
            "num": count,
        }
        sorted_list.append(sorting_list)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list