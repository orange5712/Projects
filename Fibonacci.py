def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def f(n, p, g, k, c):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif c < n:
        return f(n, g, g + p, k + g, c + 1)
    else:
        return 2 * g + k + p

def fibiter(n):
    p = 1
    g = 0
    k = 1
    c = 2
    return f(n, p, g, k, c)

# Testing the functions
print(fib(5))  
print(fibiter(5))  