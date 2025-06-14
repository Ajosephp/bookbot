import sys

from stats import (
    get_book_text,
    get_num_words,
    get_char_count,
    chars_dict_to_list_sorted
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    chars_list_sorted = chars_dict_to_list_sorted(chars_dict)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_list_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
if __name__ == "__main__":
    main()
