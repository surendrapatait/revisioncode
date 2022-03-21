c = {'ME5I':{"NUMBER OF STUDENT":50,'AVG RESULT':90},
        'ME3I':{"NUMBER OF STUDENTs":50,'AVG RESULT':50}}

print(c)

import sys
sys.exit(0)
Dict = {'Dict1': {},
        'Dict2': {}}
print("Nested dictionary 1-")
print(Dict)

# Nested dictionary having same keys
Dict = {'Dict1': {'name': 'Ali', 'age': '19'},
        'Dict2': {'name': 'Bob', 'age': '25'}}
print("\nNested dictionary 2-")
print(Dict)

# Nested dictionary of mixed dictionary keys
Dict = {'Dict1': {1: 'G', 2: 'F', 3: 'G'},
        'Dict2': {'Name': 'Geeks', 1: [1, 2]}}
print("\nNested dictionary 3-")
print(Dict)
import sys
sys.exit(0)

a={1:"One",2:'two',3:"three",4:'Four',5:'Five',6:'Six',1:"ONE"}
n={1:"One",2:'two',3:"three",4:'Four',5:'Five',6:'Six',1:"ONE"}

print(n.fromkeys(n))
print(n.fromkeys('One','Two',))
a={1,2,3,4,5,6}
n={1:"One",2:'two',3:"three",4:'Four',5:'Five',6:'Six',1:"ONE"}
n.setdefault(8,"ONE11211")
print(n)

