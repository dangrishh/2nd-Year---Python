class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print()
        print("Enter Information for Student")
        print("Name    : " + self.name)
        print("Course  : " + self.course)
        print("Year    : " + self.year)
        print("Scetion : " + self.section)

listOfStudents = []

j = 1
while True:
    print()
    print("Student Information #" + str(j))
    name = input("Name     : ")
    course = input("Course   : ")
    year = input("Year     : ")
    section = input("Section  : ")
    s = Student(name,course,year,section)
    listOfStudents.append(s)
    j = j + 1

    print()
    choice = input("Create Another Students? [Y/N] : ")
    if choice == 'Y' or choice == 'y': pass
    else: break

i = 1
for student in listOfStudents:
    print()
    print("Student #" + str(i))
    student.introduce()
    i = i + 1