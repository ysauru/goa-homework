def descending_order(num):
    digits = []
    str_num = str(num)
    result = ""
    
    for char in str_num:
        digits.append(int(char))
    
    digits.sort(reverse=True)
    
    for digit in digits:
        result = result + str(digit)
    
    return int(result)
    