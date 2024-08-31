class StudentRecord:
    def __init__(self, name: str, roll_number: int,  marks: list):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

class StudentManagementSystem:
    def __init__(self):
        self.student_records = []

    def accept(self):
        name = input("Name: ")
        roll_number = input("Roll number: ")
        mark1 = input("Mark for first subject: ")
        mark2 = input("Mark for second subject: ")
        if not roll_number.isdigit() or not mark1.isdigit() or not mark2.isdigit():
            print("Either mark or a roll number is not an integer.")
            return
        roll_number = int(roll_number)
        mark1 = int(mark1)
        mark2 = int(mark2)

        if not any([True for record in self.student_records if record.roll_number == roll_number]):
            st_record = StudentRecord(name, roll_number, [mark1, mark2])
            self.student_records.append(st_record)
            print("A record has been created.")
        else:
            return 0

    def display(self):
        if self.count_students_records != 0:
            print("Student Records:")
            for record in self.student_records:
                print(f"Name: {record.name}")
                print(f"Roll number: {record.roll_number}")
                print(f"Mark for first subject: {record.marks[0]}")
                print(f"Mark for second subject: {record.marks[1]}")
                print()
        else:
            print("There are no student records in a syste,.")

    def search(self, roll_number=None):
        if not roll_number:
            roll_number = input("Roll number: ")

        if roll_number.isdigit():
            roll_number = int(roll_number)
        else:
            return 0

        for record in self.student_records:
            if record.roll_number == roll_number:
                return record
        return 0

    def delete(self):
        record = self.search()
        if record:
            self.student_records.remove(record)
            return 1
        else:
            return 0

    def update_roll_number(self):
        old_roll_number = input("Old roll number: ")
        old_roll_record = self.search(old_roll_number)
        new_roll_number = input("New roll number: ")
        new_roll_record = self.search(new_roll_number)

        if old_roll_record and not new_roll_record:
            old_roll_record.roll_number = new_roll_number
            return 1
        else:
            return 0



    @property
    def count_students_records(self):
        return len(self.student_records)

system = StudentManagementSystem()
system.accept()
system.accept()

system.display()

system.delete()
system.update_roll_number()
system.display()
