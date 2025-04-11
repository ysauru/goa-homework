def power2(pow2):
    list1 = []
    for i in pow2:
       i **= 2
       list1.append(i)
    return list1

print(power2([1, 2, 3, 4]))