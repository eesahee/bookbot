path_to_file = 'books/frankenstein.txt'
with open(path_to_file) as f:
    file_contents = f.read()

def number_of_words(text_to_count):
    words = text_to_count.split()
    sum_words = 0
    for word in words:
        sum_words += 1
    return sum_words

def number_of_letters(text_to_count):
    lower_case = text_to_count.lower()
    letter_count = {}
    for letter in file_contents.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

count_words = number_of_words(file_contents)
count_of_letters_dictionary = number_of_letters(file_contents)
count_of_letters_list = list(count_of_letters_dictionary.items())
count_of_letters_list.sort(key=lambda x: x[1], reverse=True)

print(f" --- Begin report of {path_to_file} ---")
print(f"{count_words} words found in the document\n")
for letter in count_of_letters_list:
    print(f"The '{letter[0]}' character was found {letter[1]} times")
print("--- End report ---")
