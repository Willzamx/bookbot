def get_book_length(bookText):
    return len(bookText.split())

def get_number_of_this_character(book_text):
    characters = {}
    for char in book_text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_characters(dict):
    my_list = list(dict.items())
    dict_list = []
    for item in my_list:
        new_dict = {}
        new_dict["char"] = item[0]
        new_dict["num"] = item[1]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
