"""Make a function that encrypts a given input with these steps:


Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:
a => 0
e => 1
i => 2
o => 2
u => 3

Step 3: Add "aca" to the end of the word: "1lpp0aca"

example:encrypt("burak") ➞ "k0r3baca"

"""




def encrypt (word):
    s = word[::-1]
    word1 = s.maketrans('aeou', '0123')
    return s.translate(word1) + "aca"


