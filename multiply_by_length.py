"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Create a function to multiply all of the values in a list by the amount of values in the given list.


example :
MultiplyByLength([4, 1, 1]) ➞ ([12, 3, 3])

MultiplyByLength([1, 0, 3, 3, 7, 2, 1]) ➞  [7, 0, 21, 21, 49, 14, 7]

"""





def MultiplyByLength(arr):
    return [i*len(arr) for i in arr]
    
print(MultiplyByLength([2, 3, 1, 0]) )