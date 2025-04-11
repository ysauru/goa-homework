def double_values(list1):
    list2 = []
    for i in list1:
        i += i
        list2.append(i)
    return list2


print(double_values([1, 2, 3, 4]))