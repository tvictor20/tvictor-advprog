class Student():
    counter = 0
    maleCounter = 0
    def __init__(self, name, lastName, gender):
        self.name = name
        self.lastName = lastName
        self.number = Student.counter
        if gender == "male":
            Student.maleCounter += 1
        Student.counter += 1

studentList = []
studentList.append(Student("Tommy", "Victor", "male"))

studentList.append(Student("Ben", "Rosin", "male"))

def main():
    running = 1
    while running == 1:
        print "There are " + str(studentList[0].counter) + " students in the directory"
        print "Press 1 to see everyone in the directory"
        print "Press 2 to add someone to the directory"
        print "Press 3 to close"
        try:
            x = input()
        except NameError:
            print "Invalid input"
            x = 4
        print ""
        if x == 1:
            for i in studentList:
                print i.name + " " + i.lastName
            print ""

        if x == 2:
            fname = raw_input("What is their first name? ")
            lname = raw_input("What is their last name? ")
            gender = raw_input("What is their gender?")
            studentList.append(Student(fname, lname, gender))

        if x == 3:
            running = 0


main()
