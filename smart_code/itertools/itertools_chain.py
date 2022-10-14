"""
    Make an iterator that returns elements from the first iterable until it is exhausted. 
    Then proceeds to the next iterable, until all of the iterables are exhausted. 
    Used for treating consecutive sequences as a single sequence. 
"""

from itertools import chain

iterator1 = 'ABC'
iterator2 = '123'

print(list(chain(iterator1, iterator2)))

"""Result
['A', 'B', 'C', '1', '2', '3']
"""