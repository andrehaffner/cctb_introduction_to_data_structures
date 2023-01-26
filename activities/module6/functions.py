
def find_unique(a): return list(set(a))


def bubble_sort(a):
    for j in range(len(a)):
        swapped = False
        i = 0
        while i < len(a) - 1:
            if a[i] > a[i + 1]:
                # swapping
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
            i = i + 1
        if not swapped:
            break
    return a


a = [40, 10, 25, 15, 15, 20, 40]
print("Unique values from the list:", find_unique(a))
print("List sorted using bubble sort", bubble_sort(a))
