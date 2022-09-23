'''
Input Format :
The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format :
Print the space separated elements of deque d.

Sample Input :              Sample Output:
6                           1 2
append 1
append 2
append 3
appendleft 4
pop
popleft
'''

from collections import deque

d = deque()
for i in range(int(input())):
    s = input().split()
    if s[0] == 'append':
        d.append(s[1])
    if s[0] == 'appendleft':
        d.appendleft(s[1])
    if s[0] == 'pop':
        d.pop()
    if s[0] == 'popleft':
        d.popleft()
    
for j in d:
    print(j, end = ' ')

