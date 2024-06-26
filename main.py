
# Main.py



def main():
    path_to_open = "books/frankenstein.txt"
    text = get_book_text(path_to_open)
    word_count = count_words(text)  
    print(f"{word_count} words found in the document")

def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
