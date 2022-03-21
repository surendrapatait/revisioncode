class Employee:

    def __init__(self,eid,enm,eage):
        self.Emp_id=eid
        self.Emp_name=enm
        self.set_age=eage

    def set_age(self,age):
        if age>18:
            self._Empage=age
        else:
            print("Invalid Age")

    def get_age(self):
        return self._Empage

    def __str__(self):
        return f'''{self.Emp_id},{self.set_age},{self.Emp_name}'''

    def __repr__(self):
        return self(str)

    @classmethod
    def validation(cls,eid,enm,eage):
        if eid >0 and eage>18:
            return cls(eid,enm,eage)
        else:
            print('Invalid the age')



e1=Employee(101,'34234',34)
print(e1)
e1.Emp_age=14

print(e1)


import sys
sys.exit(0)

#
#
# '''
# class Employee:
#
#     def __init__(self,empid,epnm,epage):
#         self.employee_id=empid
#         self.employee_name=epnm
#         self.set_age(epage)
#
#     def set_age(self,age):
#         if age>18:
#             self._empAge=age
#         else:
#             print("Invalid age")
#
#     def get_age(self):
#         return self._empAge
#
#     def __repr__(self):
#         return str(self)
#
#
#     def __str__(self):
#         return f'''[{self.employee_id},{self.employee_name},{self._empAge}]'''
#
#
#
#
#     @classmethod
#     def validation_function(cls,empid,epnm,epage):
#         if empid>0 and epage>18 :
#             return cls(empid,epnm,epage)
#         else:
#             print( 'Inavalid the empid and epage')
#
#     epage=property(fset=set_age,fget=get_age)
#
# e1=Employee.validation_function(101,'dhruv',75)
# print(e1)
# e1.empAge=55
# print(e1)'''