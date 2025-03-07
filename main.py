import sys
from stats import words_count, char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
        text = book_text(book_path)
        num_words = words_count(text)
    #print(num_words)
        book_char_count = char_count(text)
        print_char_counts(book_char_count)
        sorted_char_list = sort_char_list(book_char_count)
        print_ordered_char(sorted_char_list, num_words, book_path)


def book_text(path):
    with open(path) as f:
        return f.read()

def print_char_counts(book_char_count):
    for i in book_char_count:
       print(f"'{i}: {book_char_count[i]}'")

def sort_char_list(book_char_count):
    char_list = [(char, count) for char, count in book_char_count.items()]
    char_list.sort()
    sorted_char_list = sorted(char_list, key=lambda pair: pair[1], reverse=True)
    return sorted_char_list

def print_ordered_char(sorted_char_list, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"'{num_words} words found in the document'")
    print("")

    for item in sorted_char_list:
        if item[0] != " ":
            print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

main()