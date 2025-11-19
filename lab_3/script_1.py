class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def display_info(self):
        print(f"Студент: {self.name}\nГруппа: {self.group}")


new_student = Student("Филин Александр Алексеевич", 221131)
new_student.display_info()
