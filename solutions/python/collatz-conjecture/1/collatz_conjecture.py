def steps(number):
    if(number<=0):
        raise ValueError("Only positive integers are allowed")
    elif(number == 1):
        return 0
    else:
        c =0
        while(number>1):
            if(number % 2 ==0):
                number = number /2
                c+=1
            else:
                number = (number*3)+1
                c+=1
    return c
