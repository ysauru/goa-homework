def negative(num):
    list1 = []
    for i in num:
        if i > 0:
            list1.append(i)
    return list1

print(negative([1, 2, 3, -1, -2]))