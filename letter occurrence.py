def find_occurrences(txt, ch):
    a = {}
    txt = t.lower()
    ch = c.lower()
    txt = t.split( )

    for i in txt:
        a[i.lower()] = i.count(ch)
        
    return a
