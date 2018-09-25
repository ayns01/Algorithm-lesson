# Prime number

def isPrime(n):
        if n <= 1:
            return print("it is not a prime number")
        else:
            for i in range(2, n):
                if n % i == 0:
                    return print("it is not a prime number")
                else:
                    continue
            return print("it is a prime number")
print(isPrime(12))


# Derrick's solution

import math

def prime(n):
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % 2 == 0:
            return False
    return True

# Euclidean algorithm
# a = q * b + r
# HCF - m
# m * a' = q * m * b' + r
# r = m * r'
# bとrの最大公約数はaとbの最大公約数mと同じ
# bとrのHCFは、bをa,rをbとして同じ計算をする

# HCF - using Recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print("GCD is ", gcd(60, 48))

# LCM
def lcm(a, b):
    return a * b / gcd(a, b)
print("LCM is ", int(lcm(2, 3)))

# Extra-bonus
def calcSquareRoot(n):
    return math.sqrt(n)
print("The squareroot of a given number is ", calcSquareRoot(3))


