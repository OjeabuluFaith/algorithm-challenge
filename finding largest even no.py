"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Write a function that finds the largest even number in a list.
 Return -1 if not found. The use of built-in function max() and sorted() are prohibited.


example: ([1, 3, 5, 7]) ➞ -1

"""



def largest_even(lst):
    res = -1
    for x in lst:
        if not x % 2 and x > res:
            res = x
    return res