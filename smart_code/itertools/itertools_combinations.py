#This tool returns the r length subsequences of elements from the input iterable. 
'''
Input Format :
A single line containing the string  and integer value  separated by a space.
The string contains only UPPERCASE characters.

Output Format :
Print the different combinations of string  on separate lines.

Sample Input :
HACK 2

Sample Output :
A
C
H
K
AC
AH
AK
CH
CK
HK
'''

from itertools import combinations

A, B = input().split()
A = sorted(A)
B = int(B)

for i in range(1, B + 1):
    for j in combinations((A), i):
        print(''.join(j))

# print(list(combinations((A), 2)))