v1=[10,20,30,(10,20,30)]
print(v1)
v2=v1.copy()
import copy
v3=copy.deepcopy(v1)
v1=[10,20,30,(10,20,30),['A','B','C']]
v2=v1.copy()
v3=copy.deepcopy(v1)
v4=copy.copy(v1)
v1[4][1]="BBBV"
print(v1)
print(v2)
print(v3)
print(v4)
