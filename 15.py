#!/usr/bin/python -tt

# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.


# How many routes are there through a 20x20 grid?

#SOLUTION NOTE:
#2/4/2012
# Kid's stuff using DP.

S = 20
m = [[0 for i in range(S+1)] for j in range(S+1)]
for i in range(S+1):
    for j in range(S+1):
        if i == 0 or j == 0:
            m[i][j] = 1
        else:
            m[i][j] = m[i-1][j] + m[i][j-1]
print m[S][S]
