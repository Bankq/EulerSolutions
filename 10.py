#!/usr/bin/python -tt
import math

#Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million(2,000,000)

MAX = 2000000


a = [0] * MAX

def update(i,a):
    mark = i 
    while mark < len(a):
        a[mark] = 1
        mark += i


def is_prime(i):
    if i < 2: return False
    if i == 2: return True
    check = 2
    maxN = math.sqrt(i)
    while check < maxN + 1:
        if i % check == 0:
            return False
        check += 1
        return True

def sum_up():
    sum = 0
    for i in range(2,MAX):
        if a[i] == 0:
            # number unchecked
            if is_prime(i):
                sum += i
                update(i,a)
        elif a[i] == 1:
            # number marked as not prime
            continue
    return sum


#print is_prime(4)
print sum_up()
