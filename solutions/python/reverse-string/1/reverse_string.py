def reverse(text):
    s=""
    for i in range(len(text)-1,-1,-1):
        s+=text[i]

    return s
