"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. 
The scale will tip on the direction of the largest total. If both sides are equal, return "balanced"

example::scale_tip([1, 2, 3, "I", 4, 0, 0]) ➞ "left"
# 6 > 4 so it will tip left

"""








def scale_tip(lst):
    left =sum(lst[:3])
    right = sum(lst[-3:])
    for i  in lst:
        if left > right:
            return  "left"
        elif right > left:
            return  "right"
        else:
            return"balanced"
    
    