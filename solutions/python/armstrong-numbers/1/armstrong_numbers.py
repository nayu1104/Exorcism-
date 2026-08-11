def is_armstrong_number(number):
    digit = len(str(number))
    nc = number 
    s = sum(int(d) ** int(digit) for d in str(number))
    return nc == s
    
