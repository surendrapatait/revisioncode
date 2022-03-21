
def client_reqiurement(functref):
     def business_function(a,b):
         if type(a)==int and type(b)==int:
             if a>0 and b>0:
                 result=functref(a,b)
                 print(result)
             else:
                 print("Iterger Shoud be Positive")
         else:
             print('type Should be Ineger')
     return business_function



def addition(m,n):
    result=m+n
    return result

# var=client_reqiurement(addition)
# var(1000,20)
# import sys
# sys.exit(0)
# @client_reqiurement
def addition(m,n):
    result=m+n
    return result

addition(10,300)






'''def outer_function():
    print("outer starts..1")

    def inner_function():
        print('inner_function..2')

        def one_more_inner_function():
            print("one more Inner Functions..3")
        #return one_more_inner_function
    print("outer completed..4")

    return inner_function

x=outer_function()

x()

x()
x()
x()
'''


'''
def client_requirement(functref):
    def business_calling(x,y):
        if type(x)==int and type(y)==int:
            if x>0 and y>0:
                result=functref(x,y)
                #print(result)
            else:
                print("Integer must be Postive")
        else:
            print("Varrible must be Interger")
    return business_calling

#@client_requirement
def addition(n1,n2):
    result=n1+n2
    return result
addition(10,20)

a=client_requirement(addition)'''




