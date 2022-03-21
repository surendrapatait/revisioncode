def m3():
    print(1)
    print(2)
    print(3)
    for item in range(5):
        if item==3:
            return     #
        print(item)
    print(4)
    print(5)

m3()
import sys
sys.exit(0)




def m2():
    print(1)
    print(2)
    for item in range(5):
        if item==5:
            continue
        print(item)

    print(3)
    print(4)
m2()
import sys
sys.exit(0)


def m1():
    print(1)
    print(2)

    for item in range(5):
        if item==2:
            break
        print(item)
    print(3)
    print(4)

m1()
import sys
sys.exit(0)


for col  in range(5):
    for row in range(5):
        print(col,row,end='\t\t')
        if row==2 or col==2:
            break
            print(col,row)
    print()



import sys
sys.exit(0)



for col in range(5):
    for row in range(5):
        print(col,row,end='\t\t')
        if row==2 and col==2:
            break
    print()