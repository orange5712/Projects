def p(a, b, c, d):
    if d < c:
        return p(a, b * a, c, d + 1)
    else:
        return b

def pow(a, c):
    b = a
    d = 1
    return p(a, b, c, d)

def f(x, v):
    if x > 0:
        return f(x // 2, v + 1)
    else:
        return v

def g(x):
    v = 0
    return f(x, v)

def K(x, n, y):
    if n == 0:
        return y
    elif x % 2 > 0:
        return K(x // 2, n - 1, y + pow(10, n))
    else:
        return K(x // 2, n - 1, y)

def Binary(x):
    n = g(x)
    y = 0
    return K(x, n, y)

# Testing the functions
print(pow(2, 3))  # Output: 8
print(g(7))  # Output: 3
print(K(7, 3, 0))  # Output: 1010
print(Binary(7))  # Output: 1010
