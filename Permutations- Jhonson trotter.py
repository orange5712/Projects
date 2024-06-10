LEFT_TO_RIGHT = True
RIGHT_TO_LEFT = False

def search(a, n, m):
    for i in range(n):
        if a[i] == m:
            return i + 1

def getM(a, dir, n):
    mp = 0
    m = 0
    for i in range(n):
        if dir[a[i] - 1] == RIGHT_TO_LEFT and i != 0:
            if a[i] > a[i - 1] and a[i] > mp:
                m = a[i]
                mp = m
        if dir[a[i] - 1] == LEFT_TO_RIGHT and i != n - 1:
            if a[i] > a[i + 1] and a[i] > mp:
                m = a[i]
                mp = m
    return m if m != 0 and mp != 0 else 0

def OnePerm(a, dir, n):
    m = getM(a, dir, n)
    pos = search(a, n, m)
    
    if dir[a[pos - 1] - 1] == RIGHT_TO_LEFT:
        a[pos - 1], a[pos - 2] = a[pos - 2], a[pos - 1]
    elif dir[a[pos - 1] - 1] == LEFT_TO_RIGHT:
        a[pos], a[pos - 1] = a[pos - 1], a[pos]
    
    for i in range(n):
        if a[i] > m:
            dir[a[i] - 1] = RIGHT_TO_LEFT if dir[a[i] - 1] == LEFT_TO_RIGHT else LEFT_TO_RIGHT
    
    print(''.join(map(str, a)), end=' ')

def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def printPermutation(n):
    a = list(range(1, n + 1))
    dir = [RIGHT_TO_LEFT] * n
    
    print(''.join(map(str, a)))
    
    for i in range(1, fact(n)):
        OnePerm(a, dir, n)

if __name__ == "__main__":
    n = 4
    printPermutation(n)
