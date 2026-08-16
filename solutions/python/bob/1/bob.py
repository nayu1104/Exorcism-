def response(hey_bob):
    s = hey_bob.strip()
    if(not s.isupper() and s.endswith('?')):
        return "Sure."
    elif(s.isupper() and s.endswith('?')):
        return "Calm down, I know what I'm doing!"
    elif(s.isupper()):
        return "Whoa, chill out!"
    elif(s==""):
        return "Fine. Be that way!" 
    else:
        return "Whatever."
        
        