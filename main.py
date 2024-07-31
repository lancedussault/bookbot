def main():
    path_to_file = "books/frankenstein.txt"
    text = read_the_book(path_to_file)
    word_count = count_words(text)
    character_count = count_characters(text)
    dict_list = convert_dict_to_list(character_count)
    dict_list.sort(reverse=True, key=sort_on)
    #print(text)
    #print(word_count)
    #print(character_count)
    #print(dict_list)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    for item in dict_list:
        print(f"The {item['char']} character was found {item['count']} times")
    print("--- End report ---")

def read_the_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_int_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char not in char_int_dict:
            char_int_dict[char] = 1
        else: 
            char_int_dict[char] += 1
    return char_int_dict

def convert_dict_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        if key.isalpha():
            new_dict = {
                'char': key,
                'count': value
            }
            dict_list.append(new_dict)
    return dict_list

def sort_on(dict):
    return dict["count"]

main()