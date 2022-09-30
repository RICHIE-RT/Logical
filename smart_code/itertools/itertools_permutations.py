# This tool returns successive r length permutations of elements in an iterable.
'''
Input Format :
A single line containing the space separated string  and the integer value .
The string contains only UPPERCASE characters.

Output Format :
Print the permutations of the string  on separate lines.

Sample Input :
HACK 2

Sample Output : 
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
from itertools import permutations

A, B = input().split()
A = sorted(A)
B = int(B)

for i in permutations(A, B):
    print(''.join(i))
    