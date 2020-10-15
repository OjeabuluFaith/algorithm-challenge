def pascals_triangle(n):
    a=1
    b=[1]
    for i in range(1,n+1):
        a=a*(n+1-i)//i
        b.append(a)
    return " ".join([str(e) for e in b])