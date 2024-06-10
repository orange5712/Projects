def sumofpd(x, g, c):
    if g == x:
        return c
    elif x % g == 0:
        return sumofpd(x, g + 1, c + g)
    else:
        return sumofpd(x, g + 1, c)

def Sumofpdd(x):
    g = 1
    c = 0
    return sumofpd(x, g, c)

def A(a, b):
    return 2 if Sumofpdd(a) == b else 1

def B(a, b):
    return 2 if Sumofpdd(b) == a else 0

def Amicable(a, b):
    return A(a, b) == B(a, b)


