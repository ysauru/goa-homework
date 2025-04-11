def evennum(even):
    list1 = []
    for i in even:
       if i % 2 == 0:
           list1.append(i)
    return list1
       

print(evennum([1, 2, 3, 4]))