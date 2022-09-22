'''
-> Find out most common value in given input.

Sample Input : 
aabbbccde
3

Sample Output :
b 3
a 2
c 2
'''

from collections import Counter

raw_data = sorted(input())
nof_common_values = int(input())
values = Counter(raw_data).most_common(nof_common_values)

for val in values : print(*val)
