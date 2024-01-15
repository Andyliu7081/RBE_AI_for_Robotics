import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')

    with open(fname, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # lowercase
        text = regex.sub(' ', text)  # Remove non-alphabetic
        words = set(text.split())  # Create a set
    return words

def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    words1 = wordset(fname1)
    words2 = wordset(fname2)
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    return intersection / union

# # Example output
# FNAME1 = "glass_ascii.txt"
# FNAME2 = "alice_ascii.txt"
# print("Jaccard index between", FNAME1, "and", FNAME2, ":", jaccard(FNAME1, FNAME2))

