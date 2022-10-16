"""
    Make an iterator that filters elements from data returning only those that have a
    corresponding element in selectors that evaluates to True. Stops when either the 
    data or selectors iterables has been exhausted.
"""

from itertools import compress

iterator1 = [1,2,3,4,5]
iterator2 = 'ABCDE'

print(list(compress(iterator1, [1, 0, 1, 0, 1])))
print(list(compress(iterator1, [True, False, True])))
print(list(compress(iterator2, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0])))

"""Result
[1, 3, 5]
[1, 3]
['A', 'C', 'E']
"""