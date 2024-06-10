SIZE = 100
BADVAL = -9999

class Stack:
    def __init__(self):
        self.sp = -1
        self.arr = [0] * SIZE

    def is_empty(self):
        return self.sp == -1

    def is_full(self):
        return self.sp == SIZE - 1

    def top(self):
        if self.is_empty():
            return BADVAL
        else:
            return self.arr[self.sp]

    def pop(self):
        if self.is_empty():
            return BADVAL
        else:
            val = self.arr[self.sp]
            self.sp -= 1
            return val

    def push(self, elm):
        if self.is_full():
            return 0
        else:
            self.sp += 1
            self.arr[self.sp] = elm
            return 1

    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
            return
        for i in range(self.sp, -1, -1):
            print(self.arr[i])

def hanoi(n, a, b, c):
    if n == 1:
        ele = a.pop()
        c.push(ele)
    else:
        hanoi(n - 1, a, c, b)
        base = a.pop()
        c.push(base)
        hanoi(n - 1, b, a, c)

def hanoi_tower(n):
    a = Stack()
    b = Stack()
    c = Stack()

    for i in range(n, 0, -1):
        a.push(i)

    hanoi(n, a, b, c)

    print("Final stack output:")
    c.print_stack()

if __name__ == "__main__":
    hanoi_tower(20)
