"""
    Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, 
    missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted
"""

from itertools import zip_longest

iterator1 = 'ABCDE'
iterator2 = '12345'

# for _val in zip_longest(iterator1, iterator2, fillvalue = '-'):
#     print(_val)
    
"""Result
('A', '1')
('B', '2')
('C', '3')
('D', '4')
('E', '5')
"""

iterator3 = 'ABCDE'
iterator4 = '123'

for _val2 in zip_longest(iterator3, iterator4, fillvalue = '-'):
    print(_val2)
    
"""Result
('A', '1')
('B', '2')
('C', '3')
('D', '-')
('E', '-')
"""