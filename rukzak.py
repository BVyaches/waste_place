K, W = tuple([int(i) for i in input().split()])
new_list = [int(i) for i in input().split()]
a = [new_list[i] for i in range(len(new_list)) if i % 2 == 0]
b = [new_list[i] for i in range(len(new_list)) if i % 2 == 1]


def tourist(w, k, a, b, pos):
    if k >= K and w <= W:
        return True
    if w > W or pos == 3:
        return False
    else:
        return tourist(w + a[pos], k + b[pos], a, b, pos + 1) or tourist(w, k, a, b, pos + 1)


if tourist(0, 0, a, b, 0):
    print(1)
else:
    print(0)
