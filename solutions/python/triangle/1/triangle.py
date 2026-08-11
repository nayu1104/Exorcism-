def equilateral(sides):
    a,b,c = sides
    return v(a,b,c) and (a==b==c)
    

def isosceles(sides):
    a,b,c = sides
    return v(a,b,c) and (a==b or b==c or a==c)
    


def scalene(sides):
    a,b,c = sides
    return v(a,b,c) and not (a==b or b==c or a==c)
    


def v(a,b,c):
    return (a>0 and b>0 and c>0) and (a + b >= c and b + c >= a and a + c >=b)