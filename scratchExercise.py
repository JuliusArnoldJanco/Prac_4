""" Scratch Exerise"""


""" Function for counting words"""
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        """Counts occurences of words in the string"""
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
"""Creates new line at the end of each entry, format position k, v. k = words, v = occurrence. sorted()= organises the dictionary alphabetically."""
print("\n".join("{}: {}".format(k, v) for k, v in sorted(word_count(' this is a collection of words of nice words this is a fun thing it is').items())))
