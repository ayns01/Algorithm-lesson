# Insertion Sort

arr = [10, 5, 3, 6, 1, 4, 2, 8, 7, 9]

for i in range(1, len(arr)): # i: the index of the elements that will be inserted
    x = arr[i]
    k = i - 1
    while k >= 0 and x < arr[k]:
            arr[k + 1] = arr[k]
            k -= 1
    arr[k + 1] = x
print(arr)


# Factorial n
# 1. iterative Way
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= 1

# 2. Recursive Way
def factorial_recur(n):
    if n == 1:
        return 1
    return n * factorial_recur(n - 1)

# Fibonacchi - iteration
def fibonacchi_iter(n):
    n1 = 0
    n2 = 1
    for i in range(2, n):
        if n == 1:
            return n1
        elif n == 2:
            return n2
        else:
            nth = n1 + n2
            n1 = n2
            n2 = nth
    return nth
print(fibonacchi_iter(6))


# Fibonacci - Recursion
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))

