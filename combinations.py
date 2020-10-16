"""
Author:faith ojeabulu 
Date:10th october 2020 



Question:Write a function that returns the amount of possible combinations when drawing the given amount of cards from a deck of cards.

The function must take two inputs: k is the amount of cards to draw. n the total amount of cards in the deck.

For example, a poker hand can be described as a 5-combination (k = 5) of cards from a 52 card deck (n = 52). The 5 cards of the hand are all distinct, and the order of cards in the hand does not matter. There are 2,598,960 such combinations.

The amount of combinations should be returned as an integer.

example:combinations(10, 52) ➞ 15820024220

"""



import numpy
def combinations(*nums):
   result = numpy.prod(nums)
   return result  

print(combinations(3, 7, 4 ))