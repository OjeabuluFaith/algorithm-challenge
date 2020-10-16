"""
Author:faith ojeabulu 
Date:10th october 2020 



Question:In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.

Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not. 

example:
is_sastry(106755) ➞ True
# Concatenation of n and its successor = 106755106756
# 106755106756 is a perfect square (326734 ^ 2)


"""





import math
def is_sastry(n):
    a  = int(str(n) + str(n+1))
    if math.sqrt(a) % 1 == 0:
        return True
    else:
        return False
        