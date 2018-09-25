# Selection Sort

alist = [2, 3, 1, 7, 5, 4, 8, 6]

# for i from 0 to len(alist)
# min - temp variable to assign min value
for i in range(len(alist)):
    min_index = i
    #find j from i to len(alist)
    for j in range(i, len(alist)):
        if alist[min_index] > alist[j]:
            min_index = j
    #swap ith element with min_index
    temp = alist[i]
    alist[i] = alist[min_index]
    alist[min_index] = temp
print(alist)


# Bubble Sort

alist2 = [2, 3, 1, 7, 5, 4, 8, 6]
swap_count = -1
j = len(alist2) - 1

while swap_count != 0:
    swap_count = 0
    for i in range(j):
        if alist2[i] < alist2[i + 1]:
            swap_count += 1
            temp = alist2[i]
            alist2[i] = alist2[i + 1]
            alist2[i + 1] = temp
            # print(alist2)
    j -= 1
# print(alist2)
