"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

example: uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

"""

def uncensor(string, vowels):
    new_ = ""
    counter = 0
    for i in range(len(string)):
        if string[i] == "*":
            new_ += vowels[counter]
            counter += 1
        else:
            new_ += string[i]
    return new_


