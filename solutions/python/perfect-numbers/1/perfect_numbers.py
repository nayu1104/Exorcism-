def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    s = 0
    for i in range(1,(number//2)+1):
        if number % i == 0:
            s += i
    
    if s == number:
        return "perfect"
    elif s < number :
        return "deficient"
    elif s > number :
        return "abundant"
        
