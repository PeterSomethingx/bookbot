def main():
    with open("/root/workspace/github.com/PeterSomethingx/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)


if __name__ == "__main__":
    main()