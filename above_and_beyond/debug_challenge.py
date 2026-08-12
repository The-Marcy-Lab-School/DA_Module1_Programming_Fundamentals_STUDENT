"""
Above & Beyond: Debug this script -- no template this time.

A small grade-tracking tool for a class of students. It has 3 real bugs in
it. Run it, see what's wrong, and find + fix all 3 on your own. For each
one, name the exact line and precisely what's wrong with it in
REFLECTION.md's "Debugging" section -- "the loop seemed off" isn't precise
enough. See ../ABOVE_AND_BEYOND.md for what this is worth.
"""


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return self.total / len(self.grades)


def find_top_student(students):
    """Return the student with the highest average grade."""
    top = students[0]
    for i in range(len(students) - 1):
        if students[i].average() > top.average():
            top = students[i]
    return top


def get_passing_students(students, passing_grade=70):
    """Return a list of students whose average is at or above passing_grade."""
    passing = []
    for student in students:
        avg = student.average()
        if avg >= passing_grade:
            passing = student
    return passing


if __name__ == "__main__":
    students = [
        Student("Amina", [88, 91, 79]),
        Student("Devon", [65, 70, 72]),
        Student("Priya", [95, 98, 91]),
    ]
    print("Top student:", find_top_student(students).name)
    print("Passing students:", get_passing_students(students))
