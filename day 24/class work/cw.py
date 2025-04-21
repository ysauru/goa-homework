# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(st):
    result = []
    for i in range(len(st)):
        letter = st[i] 
        repeated = letter.upper() + letter.lower() * i   
        result.append(repeated)
    return '-'.join(result)

# https://www.codewars.com/kata/559590633066759614000063/train/python
def min_max(lst):
  return [min(lst), max(lst)]

# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
def arithmetic(a, b, operator):
    match operator:
        case "add":
            return a + b
        case "subtract":
            return a - b 
        case "multiply":
             return a*b
        case "divide":
             return a/b 
        
# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        square = k * k
        count += str(square).count(str(d))
    return count