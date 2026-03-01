class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 1 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
                return None
        return 'Ошибка'

    def _calculate_average(self):
        if not self.grades:
            return 0
        total_grades = []
        for grades_list in self.grades.values():
            total_grades.extend(grades_list)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        avg_grade = self._calculate_average()
        courses_in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'нет'
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'нет'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() < other._calculate_average()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() <= other._calculate_average()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() == other._calculate_average()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() != other._calculate_average()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() > other._calculate_average()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self._calculate_average() >= other._calculate_average()
        return NotImplemented



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calculate_average(self):
        if not self.grades:
            return 0
        total_grades = []
        for grades_list in self.grades.values():
            total_grades.extend(grades_list)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        avg_grade = self._calculate_average()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() < other._calculate_average()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() <= other._calculate_average()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() == other._calculate_average()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() != other._calculate_average()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() > other._calculate_average()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self._calculate_average() >= other._calculate_average()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

################################################################################################

student1 = Student('Анна', 'Петрова', 'Ж')
student2 = Student('Иван', 'Сидоров', 'М')

lecturer1 = Lecturer('Алексей', 'Николаев')
lecturer2 = Lecturer('Мария', 'Васильева')

reviewer1 = Reviewer('Ольга', 'Иванова')
reviewer2 = Reviewer('Дмитрий', 'Смирнов')

student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses += ['Git']

student2.courses_in_progress += ['Python', 'C++']
student2.finished_courses += ['Основы программирования']

lecturer1.courses_attached += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']

reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['Python', 'C++']

print("=== ВЫЗОВ ВСЕХ МЕТОДОВ ===")

print("\n--- Рецензенты выставляют оценки за домашние задания ---")
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Java', 7)

reviewer2.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'C++', 8)
reviewer2.rate_hw(student2, 'Python', 7)

print("\n--- Студенты оценивают лекции ---")
print(student1.rate_lecture(lecturer1, 'Python', 9))  # None
print(student1.rate_lecture(lecturer1, 'Java', 8))    # None
print(student2.rate_lecture(lecturer2, 'Python', 7))  # None
print(student2.rate_lecture(lecturer2, 'C++', 9))   # None

print("\n--- Проверка некорректных вызовов ---")
print(student1.rate_lecture(reviewer1, 'Python', 5))  # Ошибка (не лектор)
print(reviewer1.rate_hw(student1, 'C++', 5))          # Ошибка (курс не в progress)

print("\n=== ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ ===")
print("\n--- РЕЦЕНЗЕНТ 1 ---")
print(reviewer1)
print("\n--- РЕЦЕНЗЕНТ 2 ---")
print(reviewer2)
print("\n--- ЛЕКТОР 1 ---")
print(lecturer1)
print("\n--- ЛЕКТОР 2 ---")
print(lecturer2)
print("\n--- СТУДЕНТ 1 ---")
print(student1)
print("\n--- СТУДЕНТ 2 ---")
print(student2)

print("\n=== СРАВНЕНИЕ ОБЪЕКТОВ ===")
print(f"Студент1 > Студент2: {student1 > student2}")
print(f"Лектор1 < Лектор2: {lecturer1 < lecturer2}")

print("\n=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")

avg_student_python = average_student_grade([student1, student2], 'Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {avg_student_python:.1f}")

avg_lecturer_python = average_lecturer_grade([lecturer1, lecturer2], 'Python')
print(f"Средняя оценка за лекции по курсу 'Python': {avg_lecturer_python:.1f}")

avg_student_java = average_student_grade([student1, student2], 'Java')
print(f"Средняя оценка за домашние задания по курсу 'Java': {avg_student_java:.1f}")

avg_lecturer_cpp = average_lecturer_grade([lecturer1, lecturer2], 'C++')
print(f"Средняя оценка за лекции по курсу 'C++': {avg_lecturer_cpp:.1f}")
