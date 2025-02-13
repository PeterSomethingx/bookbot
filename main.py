def main():
    book_path = "/root/workspace/github.com/PeterSomethingx/bookbot/books/frankenstein.txt" 
    text = book_text(book_path)
    num_words = words_count(text)
    #print(num_words)
    book_char_count = char_count(text)
    #print_char_counts(book_char_count)


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



main()