def score(x, y):
    d = x**2 + y**2

    if d <= 1**2:return 10
    elif d<= 5**2: return 5
    elif d<=10**2: return 1
    else: return 0
