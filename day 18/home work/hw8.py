def kata_13_december(lst): 
    lst2 = [] 
    for i in lst:  
        if i % 2 == 0: 
            continue 
        else:
            lst2.append(i)  
    return lst2 