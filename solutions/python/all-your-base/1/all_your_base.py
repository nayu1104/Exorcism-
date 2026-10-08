def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")   
    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
           
    total=0
    for d in digits:
        total = total *input_base +d

    if total==0:
        return [0]

    ans=[]
    while (total!=0):
        ans.append(total%output_base)
        total = total // output_base

    return ans[::-1]
        

    
    