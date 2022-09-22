'''
Input Format :
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Output Format : 
Print the item_name and net_price in order of its first occurrence.

Sample Input :                  Sample Output :
9                               BANANA FRIES 12
BANANA FRIES 12                 POTATO CHIPS 60
POTATO CHIPS 30                 APPLE JUICE 20
APPLE JUICE 10                  CANDY 20
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''

from collections import  OrderedDict

dicto = OrderedDict()
for _ in range(int(input())):
    data = input().split()
    keys = ' '.join(data[:-1])
    values = int(data[-1])
    if keys in dicto:
        dicto[keys] = dicto[keys] + values
    else :
        dicto[keys] = values
        
for i, j in dicto.items():
    print(i, j)
    