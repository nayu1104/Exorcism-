def value(colors):
    l=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    s=""
    for c in colors[0:2]:
        s+=str(l.index(c))
    return int(s)