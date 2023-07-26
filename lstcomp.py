    #// python project to accept the details of 5 students and mark list of 5 subjects and find the total and average marks of each student

import sys

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Roll No: ", self.rollno)
        print("Marks: ", self.marks)

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        if self.average() >= 90:
            return "A"
        elif self.average() >= 80:
            return "B"
        elif self.average() >= 70:
            return "C"
        elif self.average() >= 60:
            return "D"
        elif self.average() >= 50:
            return "E"
        else:
            return "F"
        

def main():
    students = []
    for i in range(5):
        name = input("Enter the name: ")
        rollno = input("Enter the roll no: ")
        marks = []
        for j in range(5):
            marks.append(int(input("Enter the marks: ")))
        students.append(Student(name, rollno, marks))

    for i in range(5):
        students[i].display()
        print("Total: ", students[i].total())
        print("Average: ", students[i].average())
        print("Grade: ", students[i].grade())
        print()

if __name__ == "__main__":
    main()

# Output:








    



