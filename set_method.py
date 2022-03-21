
v1={2,3,4,5,7,8,9}
v2={1,2,3,4,5,7,8,9}
print(v1.remove(9))   #remove the elements
print(v1)
import sys
sys.exit(0)

v1={2,3,4,5,7,8,9}
v2={1,2,3,4,5,7,8,9}
print(v1.pop())
print(v1.pop())       # pop doest the # In set pop the first elemrnts not last
import  sys
sys.exit(0)
v1={1,2,3,4,5,7,8,9}
v2={1,2,3,4,5,7}
print(v2.issubset(v1))
print(v1.issubset(v2))
print(v1.issubset(v2))
print(v2.issuperset(v1))
import sys
sys.exit(0)
v1={1,2,3,4,5,7,8,9}
v2={1,2,3,4,5,7,8,9}
print(v1.isdisjoint(v2))
import sys
sys.exit(0)


v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
result=v1.update(v2)
print(v1)
print(v2)
import sys
sys.exit(0)


v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
v1.symmetric_difference_update(v2)
print(v1)
import sys
sys.exit(0)
v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
print(v1.symmetric_difference(v2))
import sys
sys.exit(0)



v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
v2.intersection_update(v1)
print(v2)

import sys
sys.exit(0)
v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
print(v1.intersection(v2))
print(v1)
print(v2)
import sys
sys.exit(0)

v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
v2.difference_update(v1)   #uncommon in both   _update Method store the value in the v2
print(v2)

import sys
sys.exit(0)
v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
print(v2.difference(v1))   #uncommon in both


import sys
sys.exit(0)
v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
v1.copy()
v2.copy()
print(v1)
print(v2)
import sys
sys.exit(0)


v1={1,2,3,4,5}
v2={1,2,3,4,5,7,8,9}
v1.add(6)
print(v1)

