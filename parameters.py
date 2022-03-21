def addition(a,y,x=10 ,*args,**kwargs):
    print(args)
    print(kwargs)

addition(1,5)
addition(10,20,25,255,45)
addition(10,25)
addition(25,89)
addition(25,79,78979,a=20,b=30,c=89,d=89)
import sys
sys.exit(0)



def addition(*args):
    sum1=sum(args)
    print(sum1)

addition()
addition(10,25,25,8995,597987,89550255.244,987897,)



import sys
sys.exit(0)
def addition(*args):
    sum=0
    for item in args:
        if type(item)==int:
            sum=sum+item
        else:
            print("Invalid the item",item)
    print(sum)

addition(25,25,850,25,"K",'A','B')



