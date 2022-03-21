class family:
    def __init__(self,fmid,fmnm,fmaddr,fmrl):
        self.Family_id=fmid
        self.Family_Name=fmnm
        self.Family_Address=fmaddr
        self.Family_relation=fmrl

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

f1=family(101,'Patait',"vida",'self')
f2=family(102,"mule",'narayamgaon',"daugher in law")


def write_page():
    file=open('Family.txt','w+')
    fm1=f'''{f1.Family_id},{f1.Family_Name},{f1.Family_relation},{f1.Family_Address}\n'''
    fm2 = f'''{f2.Family_id},{f2.Family_Name},{f2.Family_relation},{f2.Family_Address}'''

    fm=[fm1,fm2]

    file.writelines(fm)

write_page()
import sys
sys.exit(0)





class Student():
    def __init__(self,stid,stnm,strl,stbr):
        self.student_id=stid
        self.student_nm=stnm
        self.student_roll=strl
        self.student_branch=stbr

    def __str__(self):
        return f'''{self.__dict__}'''
    def __repr__(self):
        return str(self)


s1=Student(101,'kldslfjf',344,'Mechanical')
s2=Student(105,'asdjlkjdsjlfj',45345,'civil')

def write_file():
    st1=f'''{s1.student_id},{s1.student_nm},{s1.student_roll},{s1.student_nm}\n'''
    st2 = f'''{s2.student_id},{s2.student_nm},{s2.student_roll},{s2.student_nm}\n'''
    s=[st1,st2]
    file=open('STUDENT.text','a')
    file.writelines(s)
    file.close()

#write_file()

def read_file():
    file=open('STUDENT.text','r')
    for read in file.readlines():
        print(read)
read_file()








import sys
sys.exit(0)




class Student:
    def __init__(self,stid,stnm,stcls,stbr):

        self.Student_name=stid
        self.Student_ID=stnm
        self.Student_Class=stcls
        self.Studennt_branch=stbr

    def __str__(self):

        return f''' {self.__dict__}\n'''

    def __repr__(self):
        return str(self)


s1=Student(101,'Dhruv','Mechanical','ME3I')
s2=Student(102,'hdfhh','CIVIL','ME4I')

#print(s1,s2)
def write_student():
    file=open('student.txt','w')
    str1 = f'''{s1.Student_ID},{s1.Student_name},{s1.Student_Class},{s1.Studennt_branch},\n'''
    str2 = f'''{s2.Student_ID},{s2.Student_name},{s2.Student_Class},{s2.Studennt_branch}'''
    file.writelines(str1)
    file.writelines(str2)
    file.close()
write_student()

def read_file():
    file=open('student.txt','r')
    for line in file.readlines():
        print(line)

read_file()