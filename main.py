def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    organized_letters = get_organize_letters(letter_count)
    print(text)
    print(f" ---  Begin report of {book_path} ---")
    print(f"There are {word_count} words in the document")
    # print(letter_count)
    # print(organized_letters)

    fancy_char_count(organized_letters)

    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(input_text):
    split_text = input_text.split()
    i = 0
    for words in split_text: # alternatively could have used len(split_text)
        i += 1
    return i

def get_letter_count(text):
    chars = {}
    for c in text:
        lowered_text = c.lower()
        if lowered_text in chars:
            chars[lowered_text] += 1
        else:
            chars[lowered_text] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_organize_letters(dict):
    lst = []
    for i in dict:
        if i.isalpha() == True:
            lst.append({"name": i, "num": dict[i]})
    lst.sort(reverse=True, key=sort_on)
    return lst

def fancy_char_count(input):
    for i in input:
        print(f"The {i["name"]} character was found {i["num"]} times.")


main()