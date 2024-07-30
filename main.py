def main():
    path_to_file = "books/frankenstein.txt"
    text = read_the_book(path_to_file)
    word_count = count_words(text)
    character_count = count_characters(text)
    # print(text)
    # print(word_count)
    print(character_count)

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
        char_int_dict[char] = 0
        for key in char_int_dict:
            if char_int_dict[key] == 0:
                char_int_dict[key] = 1
            else:
                char_int_dict[key] += 1
    # print(char_int_dict)
    return char_int_dict

main()