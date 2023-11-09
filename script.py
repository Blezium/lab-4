import sys

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_name(self):
        print(f"My name is {self.name}")

    def get_marks(self):
        marks_str = ""
        for mark in self.marks:
            marks_str += f"{str(mark)}, "

        marks_str = marks_str[:-2]

        print(f"{self.name} marks: {marks_str}")

    def get_average_mark(self):
        marks = self.marks
        sum = 0
        for m in marks:
            sum += m
        print(f"{self.name}'s average is {sum / len(marks)}")


    def set_name(self, new_name):
        if type(new_name) == str and new_name != "":
            self.name = new_name.strip()
            print(f"New name is {new_name}")
        else:
            print("Invalid name")

    def set_marks(self, new_marks):
        result_marks = []
        if new_marks != "":
            for m in new_marks.split(","):
                mark = m.strip()
                if mark.isnumeric():
                    result_marks.append(int(mark))
                else:
                    print("Invalid marks")
                    return

        self.marks = result_marks
        print("New marks are set")
    



class Group:
    def __init__(self, students):
        self.students = []
        for i in range(len(students)):
            student = Student(students[i]["name"], students[i]["marks"])
            self.students.append(student)
    
    def get_student(self, name):
        for st in self.students:
            if st.name == name.strip():
                return st
                break

    def get_average_marks(self):
        for st in self.students:
            st.get_average_mark()

    def set_student(self, name, marks):
        if name.strip() == "": 
            print("Invalid name")
            return
        if marks.strip() == "": 
            print("Invalid marks") 
            return
        
        marks_list = []
        for m in marks.split(","):
            mark = m.strip()
            if mark.isnumeric():
                marks_list.append(int(mark))
            else:
                print("Invalid marks")
                return
        student = Student(name.strip(), marks_list)
        self.students.append(student)
        print("Student has been added")

    def remove_student(self, name):
        students = self.students
        for i in range(len(students)):
            if students[i].name == name:
                del self.students[i]
                print(f"{name} has been removed")
                return
        
        print("Student with this name is not found")


group1 = Group([{"name": "John", "marks": [5,2,5,6,5,7]}])


def ask(position):
    if position == "exit()":
        sys.exit()
    answer = ""
    if position == "start":
        print(" Type command or 'help' to see commands: ")
        answer = input("").strip()
    
    if position == "set st":
        print(" Type student name, then two spaces and marks separated by commas:")
        answer = input(" ")
        if len(answer.split("  ")) == 2:
            [name, marks] = answer.split("  ")
            group1.set_student(name, marks)
        else:
            print("Invalid value")
        ask("start")
    
    if position == "get st marks":
        print(" Type name of a student: ")
        answer = input(" ")
        student = group1.get_student(answer.strip())
        if student:
            student.get_marks()
        else:
            print("There is no student with this name")
        ask("start")

    if position == "get average mark":
        print(" Type name:")
        ans = input(" ").strip()
        student = group1.get_student(ans)
        if student:
            student.get_average_mark()
        else:
            print("Invalid name")

    if position == "set st name":
        print(" Type current name and new name separated by a comma: ")
        answer = input(" ")
        if len(answer.split(",")) == 2:
            [cur_name, new_name] = answer.split(",")
            student = group1.get_student(cur_name)
            if student:
                student.set_name(new_name)
        else:
            print("Invalid value")
        ask("start")

    if position == "set st marks":
        print(" Type student name, then two spaces and marks separated by commas:")
        answer = input(" ")
        if len(answer.split("  ")) == 2:
            [name, marks] = answer.split("  ")
            student = group1.get_student(name)
            if student:
                student.set_marks(marks.strip())
            else:
                print("There is no student with this name")
        else:
            print("Invalid value")
        ask("start")


    if position == "get average marks":
        group1.get_average_marks()

    if position == "remove st":
        print(" Type name")
        ans = input(" ").strip()
        group1.remove_student(ans)


    if answer == "help":
        print("")
        print("'set st' -------------- add a new student")
        print("'set st marks' -------- overwrite student`s marks")
        print("'get st marks' -------- get student`s marks")
        print("'get average mark' ---- get student`s average mark")
        print("'get average marks' --- get students` average marks")
        print("'remove st' ----------- remove a student from the group")
        print("")

        ask("start")
    elif answer != "":
        ask(answer)
    else:
        ask("start")


ask("start")