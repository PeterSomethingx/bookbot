import sys

def main():
    book_path = 
    text = book_text(book_path)
    num_words = words_count(text)
    #print(num_words)
    book_char_count = char_count(text)
    #print_char_counts(book_char_count)
    sorted_char_list = sort_char_list(book_char_count)
    print_ordered_char(sorted_char_list, num_words, book_path)



def words_count(text):
    words = text.split()
    return len(words)



def book_text(path):
    with open(path) as f:
        return f.read()


def char_count(text):
    lower_text = text.lower()

    char_dict = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u": 0,
    "v": 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
    " " : 0,
    }
    for c in lower_text:
        for i in char_dict:
            if c == i:
                char_dict[i] += 1
    return char_dict



def print_char_counts(book_char_count):
    for i in book_char_count:
       print(f"''{i}': {book_char_count[i]}'")

def sort_char_list(book_char_count):
    char_list = [(char, count) for char, count in book_char_count.items()]
    char_list.sort()
    sorted_char_list = sorted(char_list, key=lambda pair: pair[1], reverse=True)
    return sorted_char_list

def print_ordered_char(sorted_char_list, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    for item in sorted_char_list:
        if item[0] != " ":
            print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

main()