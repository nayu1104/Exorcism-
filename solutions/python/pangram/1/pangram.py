import string 

def is_pangram(sentence):
    sentence = sentence.lower()
    for w in string.ascii_lowercase:
        if w not in sentence:
            return False 
    return True 
    
    
