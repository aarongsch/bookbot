from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        prist("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")

    book_text = get_book_text(sys.argv[1])

    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    print(f"Found {count_words(book_text)} total words")

    print("--------- Character Count -------")
    
    characters = count_characters(book_text)

    sorted_characters = sort_characters(characters)
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()