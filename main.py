import sys
from stats import words_in_book, count_characters, sorted_list, format_message

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
    words = words_in_book(text)
    characters = count_characters(text)
    new_list = sorted_list(characters)
    message = format_message(words, new_list)
    print(message)
    #print(f"Found {words} total words")
    #print(characters)
    #print(new_list)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


main()