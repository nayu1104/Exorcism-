def is_paired(input_string):
    f=[]
    for i in input_string:
        if i in('[','{','('):
            f.append(i)
        elif i in(']','}',')'):
            if len(f)==0:
                return False
            elif f.pop()+i not in ('[]','{}','()'):
                return False

    return len(f)==0
        
