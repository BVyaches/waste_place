import random

a = [random.randint(0, 100) for i in range(1000)]


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr) - 1):
        item = arr[i]
        j = i - 1
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item

    return arr


def counting_sort(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    st = set(count)
    arr = []
    for i in st:
        for j in range(count[i]):
            arr.append(i)
    return arr


print(a)
print(bubble_sort(a))
