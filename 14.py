#!/usr/bin/python -tt


# The following iterative sequence is defined for the set of positive integers:

# n  n/2 (n is even)
# n  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?


#SOLUTION NOTE:
#2/4/2012
# This problem is easy with little help of python dictionary.

def next(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

def get_len(i,d):
    if i in d:
        return d[i]
    else:
        return 1 + get_len(next(i),d)        

d = {13:10,40:9,20:8,10:7,5:6,16:5,8:4,4:3,2:2,1:1}

for i in range(1,1000000):
    d[i] = get_len(i,d)

print max(d, key=d.get)

    
