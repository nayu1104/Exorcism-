def rotate(text, key):
    if key == 26:
        return text  

    r = ""
    for c in text:
        if not c.isalpha() :
            r+=c 
        elif c.islower():
             r+=chr((ord(c)-ord('a')+key)%26 +ord('a'))
        elif  c.isupper():
             r+=chr((ord(c)-ord('A')+key)%26 +ord('A'))
    return r
