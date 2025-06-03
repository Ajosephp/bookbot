def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_char_count(book_string):
    counted = {}
    
    for i in book_string.lower():
        if i not in counted:
            counted[i] = 1
        else:
            counted[i] += 1
    return counted

def sort_on(dict):
    return dict["num"]

def chars_dict_to_list_sorted(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        


    
