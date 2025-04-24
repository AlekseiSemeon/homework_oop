class Student:
    """Создаем класс Студент"""

    def __init__(self, name, surname, gender):
        """Перегрузка метода __init__ для определения класса Студент"""
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def add_courses(self, course_name):
        """Возможность добавлять пройденные курсы"""
        self.finished_courses.append(course_name)

    def rate_hs(self, lector, course, grade):
        """Реализуем возможность выставлять оценки Лекторам"""
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Реализует определение средней оценки и возвращает характеристики экземпляра класса"""
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for x, y in self.grades.items():
            grades_count += len(self.grades[x])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        inf = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {round(self.average_rating, 1)}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return inf

    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Mentor:
    """Создавем класс Преподователь"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Создаем класс Лектор"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """Реализует определение средней оценки и возвращает характеристики экземпляра класса"""
        grades_count = 0
        for x, y in self.grades.items():
            grades_count += len(self.grades[x])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        inf = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average_rating, 1)}'
        return inf

    def __lt__(self, other):
        """Реализует сравнение через операторы '<,>' по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    """Создаем класс Проверяющий"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """Реалезуем возможность Проверяющим выставлять оценки Студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Dозвращает характеристики экземпляра класса"""

        inf = f'Имя: {self.name}\nФамилия: {self.surname}'
        return inf


# Создаем лекторов
best_lecturer_1 = Lecturer('Gorgon', 'Friman')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Ivan', 'Petrov')
best_lecturer_2.courses_attached += ['GIT']

# Создаем проверяющих
cool_reviewer_1 = Reviewer('John', 'Doe')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['GIT']

cool_reviewer_2 = Reviewer('Oscar', 'Dante')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['GIT']

# Создаем студентов
student_1 = Student('Armando', 'Lacosto', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Eric', 'Kartman', 'male')
student_2.courses_in_progress += ['GIT']
student_2.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам
student_1.rate_hs(best_lecturer_1, 'Python', 10)
student_1.rate_hs(best_lecturer_1, 'Python', 10)
student_1.rate_hs(best_lecturer_1, 'Python', 10)

student_1.rate_hs(best_lecturer_2, 'GIT', 7)
student_1.rate_hs(best_lecturer_2, 'GIT', 6)
student_1.rate_hs(best_lecturer_2, 'GIT', 9)

student_1.rate_hs(best_lecturer_1, 'Python', 5)
student_1.rate_hs(best_lecturer_1, 'Python', 9)
student_1.rate_hs(best_lecturer_1, 'Python', 9)

student_2.rate_hs(best_lecturer_2, 'GIT', 7)
student_2.rate_hs(best_lecturer_2, 'GIT', 9)
student_2.rate_hs(best_lecturer_2, 'GIT', 7)

# Выставляем оценки студентам
cool_reviewer_1.rate_hw(student_1, 'Python', 6)
cool_reviewer_1.rate_hw(student_1, 'Python', 5)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)

cool_reviewer_2.rate_hw(student_2, 'GIT', 7)
cool_reviewer_2.rate_hw(student_2, 'GIT', 9)
cool_reviewer_2.rate_hw(student_2, 'GIT', 6)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Cписок студентов
students = [student_1, student_2]

# Cписок лекторов
lecturer = [best_lecturer_1, best_lecturer_2]


# Функция для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
def student_rating(students, course_name):
    """Функция для подсчета средней оценки за домашние задания
    по всем студентам в рамках конкретного курса"""

    sum_all = 0
    count_all = 0
    for stud in students:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def lecturer_rating(lecturer, course_name):
    """Функция для подсчета средней оценки за лекции
    всех лекторов в рамках курса"""

    sum_all = 0
    count_all = 0
    for lect in lecturer:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {round(student_rating(students, 'Python'), 1)}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {round(lecturer_rating(lecturer, 'Python'), 1)}")
print()
