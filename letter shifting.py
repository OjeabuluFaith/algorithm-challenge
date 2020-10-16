"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Create a function that takes in a sentence and a character to find. 
Return a dictionary of each word in the sentence, with the number of the specified character as the value.

example:
shift_letters("This is a test",  4) ➞ "test Th i sisa"



"""






def shift_letters(txt, n):
    letters = txt.replace(' ', '')
    n %= len(letters)
    shifted = iter((letters[-n:] + letters[:-n]))
    return ''.join(' ' if i.isspace() else next(shifted) for i in txt)