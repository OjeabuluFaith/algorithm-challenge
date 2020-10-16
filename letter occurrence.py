"""
Author:faith ojeabulu 
Date:10th october 2020 



Question: Create a function that takes in a sentence and a character to find. 
Return a dictionary of each word in the sentence, with the number of the specified character as the value.


example: find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

"""






def find_occurrences(txt, ch):
    a = {}
    txt = t.lower()
    ch = c.lower()
    txt = t.split( )

    for i in txt:
        a[i.lower()] = i.count(ch)
        
    return a
