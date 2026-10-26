def resistor_label(colors):
    c= ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

    if len(colors) == 4:
        v = (10*c.index(colors[0])+ c.index(colors[1]))* 10 ** c.index(colors[2])
    elif len(colors)==5:
        v = (100*c.index(colors[0])+ 10*c.index(colors[1])+c.index(colors[2]))* 10 ** c.index(colors[3])
    elif len(colors)==1:
        return "0 ohms"


    t={
    "grey":"0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
    }

    tol = t[colors[-1]]
    u="ohms"
    if v>=1000000:
        v = v/1000000
        u = "megaohms"
    elif v>=1000:
        v= v/1000
        u= "kiloohms"
    if v==int(v):
        v = int(v)

    return f"{v} {u} ±{tol}"
    


        
        
