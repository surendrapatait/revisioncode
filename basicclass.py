class Student:
    def __init__(self,sna,sid,srl,sad):
        self.StudentName=sna
        self.StudentId=sid
        self.StudentRoll=srl
        self.StudentAddress=sad

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)


    @classmethod
    def student_creation(cls,sna,sid,srl,sad):
        if type(sna)==str and len(sna)>=5:
            if type(sid)==int  and sid >0:
                if type(srl)==int and srl>=0:
                    if type(sad)==str and len(sad)>0:
                        return  cls (sna,sid,srl,sad)
                    else:
                        print("Invalid Addreess")
                else:
                    print("Invalid the ROll Numbers")
            else:
                print("Invalid Student ID")
        else:
            print("Invalid Name")

    @staticmethod
    def display_student(ref ,adr):
        Student.address=adr

    def show_student_info(self):
        self.StudentId=105

# s5=Student.show_student_info()
# print(s5)

s1=Student.student_creation("Dhruv",101,1098,"Pune")
s2=Student.student_creation("Dhruv1",1055,1058,"Pune")
s3=Student.student_creation("Dhruv2",105,101,"Pune")
s4=Student("Dhruv3",105,10511,"Pune")
print(id(s1))
print(id(s2))
print(s1)
print(s2)
print(s3)
print(s4)

s=[s1,s2,s3,s4]
print(s)
print(s1.__dict__)



import sys
sys.exit(0)

class Student:
    def __init__(self,sid,snm,srl,aad="Pune"):

        self.StudentId=sid
        self.StudentName=snm
        self.StudentRoll=srl
        self.StudentAdress=aad

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)


s=Student(101,'Dhruv',55,"Latur")
s1=Student(102,"Surendra",25)
s2=Student(105,"Amruta",89)
print(s,s1,s2)
