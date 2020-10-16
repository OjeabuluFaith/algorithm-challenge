"""
Author:faith ojeabulu 
Date:10th october 2020 

Goal : The goal of this challenge is to return Pascal’s triangle up to number 29. 
Pascal’s triangle is the sum of the two upper corners.

Question: Create a function that returns a row from Pascal’s triangle. 
To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column. """




def pascals_triangle(n):
    a=1
    b=[1]
    for i in range(1,n+1):
        a=a*(n+1-i)//i
        b.append(a)
    return " ".join([str(e) for e in b])