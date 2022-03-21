
sum=0
for item in range(5):
    val=int(input("Enter Any Numbers:"))
    if type(val)==int:
        sum=sum+val
    else:
        print("Invalid Numbers",val)

print(sum)
import sys
sys.exit(0)



def my_reverse_logic(word):
    v1=list(word)
    v1.reverse()
    name=''
    for item in v1:
        name=name+item
    return name
a=my_reverse_logic("surendra")
print(a)

import sys
sys.exit(0)




values=[1,23,435,65,233,"A","B","C"]
def my_sort_logic(ele):
    if type(ele)==int:
        return ele
    else:
        return ord(ele)

values.sort(key=my_sort_logic)
print(values)
import sys
sys.exit(0)




name=input("Enter your Name:")
age=int(input("Enter Your Age:"))
print('you name is {} and age {}'.format(name,age))
print('you name is {a} and age {b}'.format(a=name,b=age))
print('you name is {0} and age {1}'.format(name,age))
print(f'you name is {name} and age {age}')

import sys
sys.exit(0)
def outer_function():
    print("inside the Outer_function")

    def inner_function():
        print("Inside Inner function")

        #return 20
        def one_more_function():
            print("one more function")

            return 30            # 30 return by one_more_functin

        return one_more_function()       #one _more _function are given to return to the
    return inner_function()


x=outer_function()

print(x)