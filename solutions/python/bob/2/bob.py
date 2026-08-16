def response(hey_bob):
    s = hey_bob.strip()
    if(s==""):
        return "Fine. Be that way!" 
    elif(s.isupper() and s.endswith('?')):
        return "Calm down, I know what I'm doing!"
    elif(s.isupper()):
        return "Whoa, chill out!"
    elif(not s.isupper() and s.endswith('?')):
        return "Sure."
    else:
        return "Whatever."
        
        