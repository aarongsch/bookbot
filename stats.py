def count_words(book_text):
    words_in_book = book_text.split()
    count = 0
    for word in words_in_book:
        count += 1
    return count

def count_characters(book_text):
    characters = {}
    for c in book_text:
        char = c.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_characters(characters):
    dicts = []
    for char in characters:
        dicts.append({"char": char, "num": characters[char]})
    dicts.sort(reverse=True, key=sort_on)
    return dicts

def sort_on(items):
    return items["num"]