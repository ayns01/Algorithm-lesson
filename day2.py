# names = ["Kano", "Juan", "Masa", "Danilo", "Ayana"]

# Linear Search
# target = "Danilo"
# for i in range(len(names)): # i: 0, 1, 2, 3, 4
#     if names[i] == target:
#         print(i)


# Binary Search
array = [1, 2, 4, 6, 8]
target = 6
head = 0
tail = len(array) - 1

while head <= tail:
    center = int((head + tail) / 2)
    if array[center] == target:
        print("Index of target is", center)
        break
    elif array[center] > target:
        tail = center - 1
    elif array[center] < target:
        head = center + 1
    else:
        print("error")
else:
    print(-1)