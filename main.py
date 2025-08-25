from stats import get_num_words
from stats import char_count
from stats import sort_report
import sys
def get_book_text(file):
    with open(file) as f:
        book_contents = f.read()
        return book_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_num_words(args[1]))
    print("--------- Character Count -------")
    sort_report(args[1])
    print("============= END ===============")


main()    
