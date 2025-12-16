def words_in_book(text):
    num_words = text.split()
    return len(num_words)

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts 

def sort_on(items):
    return items["num"]

def sorted_list(words):
    new_char_num_list = []
    for char, value in words.items():
        new_dict = {}
        if char.isalpha():
            new_dict["char"] = char 
            new_dict["num"] = value
            new_char_num_list.append(new_dict)
    new_char_num_list.sort(reverse=True, key=sort_on)
    return new_char_num_list

def format_message(words, list):
    message = f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count -----------\nFound {words} total words\n--------- Character Count -------\n"
    for item in list:
        char = item["char"]
        num = item["num"]
        message += f"{char}: {num}\n"
    return message