# This tool computes the cartesian product of input iterables.
'''
Input Format :
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

Output Format :
Output the space separated tuples of the cartesian product.

Sample Input :          Sample Output
1 2                     (1, 3) (1, 4) (2, 3) (2, 4)
3 4
'''
from itertools import product 

A = map(int, input().split())
B = map(int, input().split())

for i in product(A, B):
    print(i, end = ' ')
