import operator


def get_num_words(text):
    count = 0
    for word in text.split():
        if word > '':
            count += 1
    return count

def get_count_characters(text):
    chars = {}
    lowercase = text.lower()
    for word in lowercase.split():
        for char in word:
            if char in chars:
                chars[char] +=1
            else:
                chars[char] = 1
    return chars

def print_stats(stats):
     character_list = []
     for char in stats:
         if char.isalpha():
             amount = stats[char]
             character_list.append({char: amount})
     sorted_list = sorted(character_list, key=lambda x: list(x.values())[0], reverse=True)
     return sorted_list