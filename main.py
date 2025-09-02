from stats import num_of_words
from stats import get_books_text
from stats import count_chars
from stats import sort
from stats import helper
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print(sys.exit(1))
    path = sys.argv[1]
    text = get_books_text(path)
    count = num_of_words(text)
    dic = count_chars(text)
    x = sort(dic)
    
    print(f"Found {count} total words")

    for item in x:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")

    
    

main()
