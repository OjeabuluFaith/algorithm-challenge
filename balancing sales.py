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
    
    