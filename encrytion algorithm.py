"""Make a function that encrypts a given input with these steps:"""
def encrypt (word):
    s = word[::-1]
    word1 = s.maketrans('aeou', '0123')
    return s.translate(word1) + "aca"


