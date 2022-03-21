class Nummericerror(BaseException):
    def __init__(self,error):
        self.Error=error


def student_data():
    name=input('Enter the student Name:')
    for item in range(3):
        try:
            age=int(input("Enter the age:"))
        except ValueError as v:
            #print(v.args)
            if item==2:
                raise Nummericerror('The age will be integer')
        else:
            break
    email=input("Enter the Emailid:")

    return name,age,email
while True:
    student_data()
    choice=input('Do you want to continoue y or N:')
    if choice.lower() in ['y' or 'yes']:
        break
