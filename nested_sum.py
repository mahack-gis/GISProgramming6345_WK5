

def nested_sum(t):
    t = [[1, 2], [3], [4, 5, 6]]
    total = 0
    for x in t:
        total += sum(x)
    return total

print(total)

