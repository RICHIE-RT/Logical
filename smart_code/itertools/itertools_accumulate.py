"""Make an iterator that returns accumulated sums, or accumulated results of other binary functions """

from itertools import accumulate

iterator = [1,2,3,4,5]
print(list(accumulate(iterator)))

"""Result
[1, 3, 6, 10, 15]
"""