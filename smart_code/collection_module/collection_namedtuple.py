'''
Python's namedtuple was created to improve code readability by providing a way to access values using descriptive field names instead of integer indices. - realpyton
Tuples are immutable, whether named or not. namedtuple only makes the access more convenient, by using names instead of indices. - stackoverflow
'''

from collections import namedtuple

As_a_string = namedtuple('Point', 'x y z')
As_a_list = namedtuple('Point', ['x', 'y', 'z'])
As_a_dict = namedtuple('Point', {'x':0, 'y':0, 'z':0})
newS = As_a_string(3, 4, 5)
newL = As_a_list(3, 4, 5)
newD = As_a_dict(3, 4, 5)
print(newS)
print(newL.x, newL.y)
print(newD[2])
print(newD)
print(newD._asdict().values())
print(newD._fields)
print(newD._replace(y=2))
Point2 = As_a_dict._make(['a', 'b', 'c'])
print(Point2)