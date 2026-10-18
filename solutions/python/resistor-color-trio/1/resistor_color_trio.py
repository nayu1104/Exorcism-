def label(colors):
    c = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

    v = (c.index(colors[0])*10 + c.index(colors[1])) * (10 ** c.index(colors[2]))

    if v == 0:
        return "0 ohms"
    elif v % 1000000000 == 0:
        return f"{v//1000000000} gigaohms"
    elif v % 1000000 == 0:
        return f"{v//1000000} megaohms"
    elif v % 1000== 0:
        return f"{v//1000} kiloohms"
    else:
        return f"{v} ohms"