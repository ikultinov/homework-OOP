class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def average_grade(self, grades):
        total = 0
        count = 0
        for grade in grades.values():
            for num in grade:
                total += num
                count += 1
        return total / count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: '
                f'{self.average_grade(self.grades)}\n'
                f'Курсы в процессе изучения: '
                f'{", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return (self.average_grade(self.grades) <
                other.average_grade(other.grades))


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

    def average_grade(self, grades):
        total = 0
        count = 0
        for grade in grades.values():
            for num in grade:
                total += num
                count += 1
        return round(total / count)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: '
                f'{self.average_grade(self.grades)}\n')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer'
        return (self.average_grade(self.grades) <
                other.average_grade(other.grades))


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


# создаем студентов:
best_student = Student('Ilona', 'Musk', 'female')
worst_student = Student('Jho', 'Baden', 'male')

# создаем проверяющего:
cool_reviewer = Reviewer('Some', 'Buddy')
good_reviewer = Reviewer('Nataly', 'Romanov')

# создаем лектора:
cool_lecturer = Lecturer('Ivan', 'Hacker')
second_lecturer = Lecturer('Vasil', 'Terkin')

# даем студенту изучать курс:
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['OOP']

#  даем курс для проверки проверяющему:
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
good_reviewer.courses_attached += ['OOP']

# даем лектору курс, который он ведет:
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['OOP']

# студент оценивает лектора:
best_student.rate_hw(cool_lecturer, 'Python', 5)
best_student.rate_hw(cool_lecturer, 'Git', 10)
worst_student.rate_hw(cool_lecturer, 'Python', 7)
worst_student.rate_hw(second_lecturer, 'OOP', 7)

# проверяющий оценивает студента:
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(worst_student, 'Python', 3)
good_reviewer.rate_hw(worst_student, 'OOP', 5)

print(cool_reviewer)
print(good_reviewer)
print(cool_lecturer)
print(second_lecturer)
print(best_student)
print(worst_student)
print(cool_lecturer < second_lecturer)
print(best_student < worst_student)

students = [best_student, worst_student]
lecturers = [cool_lecturer, second_lecturer]


def av_grade_all_std(classmen, course):
    total = 0
    count = 0
    for student in classmen:
        for c_name, grade in student.grades.items():
            if c_name == course:
                total += grade[0]
                count += 1
    return round(total / count)


print(av_grade_all_std(students, 'Python'))


def av_grade_all_lec(teachers, course):
    total = 0
    count = 0
    for lecturer in teachers:
        for c_name, grade in lecturer.grades.items():
            if c_name == course:
                total += grade[0]
                count += 1
    return round(total / count)


print(av_grade_all_lec(lecturers, 'OOP'))
