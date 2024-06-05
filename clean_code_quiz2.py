# Binary Search in python


def binarySearch(array, x, a, b):
    # Repeat until the pointers low and high meet each other
    while a <= b:
        # middle assigned to lowest element + (highest element - lowest element) / 2
        c = a + (b - a) // 2
        if array[c] == x:
            return c
        elif array[c] < x:
            a = c + 1
        else:
            b = c - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array) - 1)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Not found")
