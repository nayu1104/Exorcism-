def is_valid(isbn):
    digits = isbn.replace("-","")
    if len(digits)!= 10 :
        return False

    t = 0
    for i,num in enumerate(digits):
            if num.isdigit():
                v = int(num)
            elif num == "X" and i == 9 :
                v = 10
            else :
                return False
            t+= v *(10-i)
    return t %11 == 0
                
