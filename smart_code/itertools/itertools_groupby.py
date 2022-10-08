"""comperess the string
"""
'''
Input Format :
A single line of input consisting of the string S.

Output Format :
A single line of output consisting of the modified string.

Sample Input :
1222311

Sample Output :
(1, 1) (3, 2) (1, 3) (2, 1)
'''
from itertools import groupby

S = input()
for i,k in groupby(S):
    a = len(list(k)), int(i)
    print(tuple(a), end=" ")
