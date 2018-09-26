# MergeSort

def merge(l, r, a):
    nL = len(l)
    nR = len(r)
    i = 0
    j = 0
    k = 0
    while i < nL and j < nR:
        if l[i] < r[j]:
            a[k] = l[i]
            k += 1
            i += 1
        else:
            a[k] = r[j]
            k += 1
            j += 1

    while i < nL:
        a[k] = l[i]
        i += 1
        k += 1

    while j < nR:
        a[k] = r[j]
        j += 1
        k += 1

def mergesort(array):
    n = len(array)
    if n < 2:
        return
    mid = int(n / 2)
    left = array[:mid]
    right = array[mid:]
    mergesort(left)
    mergesort(right)
    merge(left, right, array)


arr = [6, 11, 4, 3, 20, 7]
n = len(arr)
mergesort(arr)
print(arr)