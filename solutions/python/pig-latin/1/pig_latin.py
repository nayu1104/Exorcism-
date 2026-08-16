def translate(text):
    word = text.split()
    words= [t(w) for w in word]
    return " ".join(words)




def t(text):
    if text.startswith(('a','e','i','o','u','xr','yt')):
        return text + "ay"
    elif text[0] not in ('a','e','i','o','u'):
        if text.startswith("thr"):
            return text[3:]+"thray"
        if text.startswith("sch"):
            return text[3:]+"schay"
        if text.startswith("qu"):
            return text[2:] +text[:2]+"ay"
        if text[1:3] =="qu":
            return text[3:] +text[:3]+"ay"
        if text[1] not in ('a','e','i','o','u'):
            if text[1] =='y':
                return text[1:]+text[:1]+"ay"
            if text[2:4] =="qu":
                return text[3:] +text[:5]+"ay"
            return text[2:] + text[:2] + 'ay'
        return text[1:] + text[0] +'ay'
    
    
   
     
