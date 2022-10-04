# itertools.combinations_with_replacement(iterable, r)
# This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
'''
Input Format :
A single line containing the string S and integer value k separated by a space.
The string contains only UPPERCASE characters.

Output Format :
Print the combinations with their replacements of string S on separate lines.

Sample Input :
HACK 2

Sample Output :
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import combinations_with_replacement
S, k = input().split()
k = int(k)

for i in combinations_with_replacement(sorted(S), k):
    print(''.join(i))