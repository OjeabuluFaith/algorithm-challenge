"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Create a function that takes a string and shifts the letters to the right by an amount n but not the whitespace.

example:
shift_letters("This is a test",  4) ➞ "test Th i sisa"



"""






def shift_letters(txt, n):
    letters = txt.replace(' ', '')
    n %= len(letters)
    shifted = iter((letters[-n:] + letters[:-n]))
    return ''.join(' ' if i.isspace() else next(shifted) for i in txt)