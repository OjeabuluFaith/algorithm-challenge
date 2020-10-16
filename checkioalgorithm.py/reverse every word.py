""" author : Faith ojeabulu
    date: 10th of october 2020
    question:
n a given string you should reverse every word, but the words should stay in their places."""
 
 
 
def backward_string_by_word(text):
    for i in text.split():
        text = text.replace(i, i[::-1])
    return text