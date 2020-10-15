import math
def is_sastry(n):
    a  = int(str(n) + str(n+1))
    if math.sqrt(a) % 1 == 0:
        return True
    else:
        return False
        