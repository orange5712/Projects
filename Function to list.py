def combine(lx, ly):
    if not lx and not ly:
        return []
    if lx:
        return [lx[0]] + combine(lx[1:], ly)
    if ly:
        return [ly[0]] + combine(lx, ly[1:])

def level(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return lst[0]
    else:
        combined = combine(lst[0], lst[1])
        return level([combined] + lst[2:])

def apply(ls, f):
    def apply_inner(ls, f, i):
        if not ls:
            return []
        else:
            return [f(ls[0], i)] + apply_inner(ls[1:], f, i + 1)
    return apply_inner(ls, f, 0)

def reverse(xs):
    def rev(xs, acc):
        if not xs:
            return acc
        else:
            return rev(xs[1:], [xs[0]] + acc)
    return rev(xs, [])

def applyr(ls, f):
    def apply_inner(ls, f, i):
        if not ls:
            return []
        else:
            return apply(ls[::-1], f)
    return reverse(apply_inner(ls, f, 0))

# Example function to use with apply and applyr
def example_function(x, i):
    return x + i

# Testing the functions
combined_list = combine([1, 3, 5], [2, 4, 6])
print("Combined:", combined_list)  # Combined: [1, 2, 3, 4, 5, 6]

leveled_list = level([[1, 2], [3, 4], [5, 6]])
print("Leveled:", leveled_list)  # Leveled: [1, 3, 5, 2, 4, 6]

applied_list = apply([1, 2, 3], example_function)
print("Applied:", applied_list)  # Applied: [1, 3, 5]

appliedr_list = applyr([1, 2, 3], example_function)
print("Applied Reverse:", appliedr_list)  # Applied Reverse: [5, 3, 1]
