from contextlib import nullcontext

from stats import get_num_words, get_count_characters, print_stats
import sys

try:
    path = sys.argv[1]
except:
    print("""
    Usage: python3 main.py <path_to_book>
    """)
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

word_count = get_num_words(get_book_text(path))
character_count = get_count_characters(get_book_text(path))
stats = print_stats(get_count_characters(get_book_text(path)))


print(f"""============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
for stat in stats:
    for key, value in stat.items():
        print(f"{key}: {value}")
print("============= END ===============")