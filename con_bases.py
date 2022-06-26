def tobin(n = 0):
    bin = []
    sbin = ""
    while n != 0:
        bin.insert(0, (n % 2))
        n //= 2
    for e in bin:
        sbin += str(e)
    return (sbin)

def tohex(n = 0):
    hex = []
    shex = ""
    tabhex = ["A", "B", "C", "D", "E", "F"]
    while n != 0:
        r = n % 16
        if r >= 10:
            hex.insert(0, tabhex[r % 10])
        else:
            hex.insert(0, r)
        n //= 16
    for e in hex:
        shex += str(e)
    return (shex)

def tooct(n = 0):
    oct = []
    soct = ""
    while n != 0:
        oct.insert(0, n % 8)
        n //= 8
    for e in oct:
        soct += str(e)
    return (soct)

def todec(n = "0", base = 0):
    n = str(n).upper()
    dec = 0
    memb = []
    bases =[2, 8, 16]
    hextab = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    for aln in n:
        memb.append(aln)

    if base not in bases:
        print("base invalida")
        return (-1)
    if base == 2:
        for e in memb:
            if e not in "01":
                print("Binário invalido.")
                return (-1)
    elif base == 8:
        for e in memb:
            if e not in "01234567":
                print("Octal invalido.")
                return (-1)
    elif base == 16:
        for e in memb:
            if e in "ABCDEF":
                i = memb.index(e)
                memb[i] = hextab[e]
            elif e not in "1234567890":
                print("Hexadecimal invalido.")
                return (-1)
    for e in memb:
        i = memb.index(e)
        memb[i] = int(e)
    c = len(memb) - 1
    i = 0
    while c >= 0:
        dec += memb[i] * (base ** c)
        c -= 1
        i += 1
    return (str(dec))

