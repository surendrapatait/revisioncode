def addition(num1,num2):
    num1=int(input('Enter the first Number1:'))
    num2 = int(input('Enter the first Number2:'))
    result=num1+num2
    return result

def multiplication(a,b):
    a = int(input('Enter the first Number1:'))
    b= int(input('Enter the first Number2:'))
    result=a*b
    return result

x=multiplication(10,20)
print(x)


import sys
sys.exit(0)














'''def outer_function():
    print('inside outer')

    def inner_function():
        print('Inside inner')

    return inner_function    #inner the ref


x=outer_function()
print(x)

x()
x()
x()
x()


                               # always return the o/p of Inner




import sys
sys.exit(0)'''


'''def outer_function():
    print('Inside Outer 1')

    def inner_function():
        print('inside inner  2')

        def one_more_inner():
            print('inside One More Inner3')
        

        one_more_inner()
    inner_function()
    print('outer Complteded 4')


x=outer_function()
print(x)


#x=outer_function()                            # only refrence is given bcs we do not call outer_function                                      # if we make object of the function then call it then its gives the return as None othrwilse it gives the wriiten in print

# outer_function()                             #inside inner and outer completed given
# x=outer_function()
# print(x)                                      #inside inner and outer completed id given+ none value is given'''

