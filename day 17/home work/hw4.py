def vowel(word):
    list1 = ""
    list2 = "aeiou"
    for i in word:
        if i in list2:
            list1 += i
    return list1

print(vowel("weight"))