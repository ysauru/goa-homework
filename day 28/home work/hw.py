# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
def sum_str(a, b):
    # happy coding !
    if a =='' and b=='':return'0'
    if b =='':return a
    if a =='':return b
    if a =='' and b=='':return'0'
    return str(int(a)+int(b))

# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python

def uni_total(string):
    acc = 0
    for i in string:
        acc += ord(i)
    return acc

# https://www.codewars.com/kata/52f3149496de55aded000410/train/python

def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number

#

def password(st):
    if len(st) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    special_chars = "!@#$%^&*()_+-="

    for char in st:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special_chars:
            has_special = True
    return has_upper and has_lower and has_number and has_special

#
def most_frequent_item_count(collection):
    highest = 0
    for element in collection:
        if collection.count(element) >= highest:
            highest = collection.count(element)
    return highest
                    

#
def encode(st):
    vowels = {'a': '1',
              'e': '2',
              'i': '3',
              'o': '4',
              'u': '5'}
    encoded = []
    for i in st:
        if i in vowels:
            encoded.append(vowels[i])
        else:
            encoded.append(i)
    return "".join(encoded)
        
def decode(st):
    numbers = {'1': 'a',
               '2': 'e',
               '3': 'i',
               '4': 'o',
               '5': 'u'}
    decoded = []
    for i in st:
        if  i in numbers:
            decoded.append(numbers[i])
        else:
            decoded.append(i)
    return "".join(decoded)