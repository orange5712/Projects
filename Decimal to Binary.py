def p(a, b, c, d):
    if d < c:
        return p(a, b * a, c, d + 1)
    else:
        return b

def pow(a, c):
    b = a
    d = 1
    return p(a, b, c, d)

def f(x, n):
    if x > 0:
        return f(x // 2, n + 1)
    else:
        return n

def F(x):
    n = 0
    return f(x, n)

def k(x, m, g):
    if x % pow(2, F(x) - 1) == 1:
        return g + 1
    elif x % pow(2, F(x) - 1) > 0:
        return k(x % pow(2, F(x) - 1),
                 F(x % pow(2, F(x) - 1)),
                 g + pow(10, F(x % pow(2, F(x) - 1)) - 1))
    else:
        return g

def Binary(x):
    m = F(x)
    g = pow(10, F(x) - 1) if x > 1 else 0
    return k(x, m, g)

# Testing the function
print(Binary(7))  # Output: 111
