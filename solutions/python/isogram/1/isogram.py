def is_isogram(phrase):
    phrase = phrase.lower()
    for l,char in enumerate(phrase):
        if char.isalpha() and char  in phrase[l+1:]:
            return False

    return True 
        
