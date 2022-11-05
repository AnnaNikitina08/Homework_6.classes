class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def mid_grade(self):
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        res1 = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(Lecturer.mid_grade(self), 1)}"
        return res1
    #
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return
        return round(Lecturer.mid_grade(self), 1) < round(other.mid_grade(), 1)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_courses(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self):
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        for course, grade in self.grades.items():
            res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                  f"Cредняя оценка за домашние задания {round(Student.mid_grade(self), 1)}\n" \
                  f"Курсы  в  процессе изучения:{self.courses_in_progress}\n" \
                  f"Завершенные курсы: {self.finished_courses}"
            return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return round((Student.mid_grade(self)), 1) < round((other.mid_grade()), 1)


def mid_grade_students_courses(course, *args):
    grades_all_students = []
    for Student in args:
        if course in student.courses_in_progress:
            grades_all_students.append(round(Student.mid_grade(), 1))
            res = sum(grades_all_students) / len(grades_all_students)
        return f'Средняя оценка студентов за курс "{course}" - {round(res, 1)}'

def mid_grade_lecturers_courses(course, *args):
    grades_all_lecturers = []
    for Lecturer in args:
        if course in Lecturer.courses_attached:
            grades_all_lecturers.append(round(Lecturer.mid_grade(), 1))
            res1 = sum(grades_all_lecturers) / len(grades_all_lecturers)
    return f'Средняя оценка всех лекторов за курс "{course}" - {round(res1, 1)}'


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ["Java"]

student = Student('Marc', 'Stine', 'male')
student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ["Java", "C++"]

cool_reviewer = Reviewer("Jon", "Smit")
cool_reviewer.courses_attached += ['Python']

some_reviewer = Reviewer("Jon", "Smit")
cool_reviewer.courses_attached += ["Python", "C++"]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(student, 'Python', 9)
cool_reviewer.rate_hw(student, 'Python', 9)
cool_reviewer.rate_hw(student, 'Python', 10)

# print(best_student.grades)
# print(student.grades)

best_lecturer = Lecturer("Peter", "Hill")
best_lecturer.courses_attached += ['Python', "Java"]

lecturer_1 = Lecturer("Sam", "Novac")
lecturer_1.courses_attached += ['Python']

student.rate_courses(best_lecturer, 'Python', 10)
student.rate_courses(best_lecturer, 'Python', 10)
student.rate_courses(best_lecturer, 'Python', 10)


student.rate_courses(lecturer_1, 'Python', 10)
student.rate_courses(lecturer_1, 'Python', 7)
student.rate_courses(lecturer_1, 'Python', 9)

# print(best_lecturer.grades)
# print(lecturer_1.grades)
# #
# #
# print(some_reviewer)
# #
# print(best_lecturer)
#
# print(lecturer_1)

# print(best_lecturer > lecturer_1)
#
# print(best_student> student)

# print(mid_grade_students_courses('Python', student, best_student))

print(mid_grade_lecturers_courses('Python', best_lecturer, lecturer_1))