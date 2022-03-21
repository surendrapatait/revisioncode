#diffrence between return and print
def addition(a,b):
    result=a+b
    return result
a=addition(10,20)

def get_doubles(val):
    print(val*2)
get_doubles(a)
import sys
sys.exit(0)

class Calculation:

    def addition(a,b):
        result=a+b
        print(result)


    def subraction(a,b):
        result=a-b
        print(result)

    def multiplication(a,b):
        result=a*b
        print(result)


    def division(a,b):
        result=a/b
        print(result)



    a=int(input('Enter The any Numbers:'))
    b=int(input("Enter the any Second Numbers:"))


    Choice =int(input("1.addition"
                      "2.subraction"
                      "3.multiplication"
                      "4.division"
                      ))

    if Choice==1:
        addition(a,b)
    elif Choice==2:
        subraction(a,b)
    elif Choice==3:
        multiplication(a,b)
    elif Choice==4:
        division(a,b)
    else:
        print("InValid Numbers")
