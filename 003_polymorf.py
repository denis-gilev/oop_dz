from xml.sax.handler import property_interning_dict


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
        """Вычисляет среднюю оценку за все домашние задания."""
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
        """Вычисляет среднюю оценку за лекции."""
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

#############################################################3333

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(student, 'Python', 7)

student.rate_lecture(lecturer, 'Python', 8)

print(reviewer)
print('\n' * 2)
print(lecturer)
print('\n' * 2)
print(student)

