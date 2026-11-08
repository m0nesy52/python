class FacultyError(Exception):
    pass


class StudentNotFoundError(FacultyError):
    pass


class CourseNotAvailableError(FacultyError):
    pass


class AlreadyEnrolledError(FacultyError):
    pass


class NotEnrolledError(FacultyError):
    pass


class InvalidGradeError(FacultyError):
    pass


class PromotionError(FacultyError):
    pass


class Discipline:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, specialty, discipline):
        self.courses.append((specialty, discipline))

    def teaches(self, specialty, discipline):
        return (specialty, discipline) in self.courses


class Record:
    def __init__(self, discipline, department, semester):
        self.discipline = discipline
        self.department = department
        self.semester = semester
        self.grade = None


class Student:
    def __init__(self, student_id, name, specialty):
        self.id = student_id
        self.name = name
        self.specialty = specialty
        self.semester = 1
        self.records = []

    def current_records(self):
        return [r for r in self.records if r.semester == self.semester]

    def find_current(self, discipline):
        for r in self.current_records():
            if r.discipline is discipline:
                return r
        return None

    def average(self):
        grades = [r.grade for r in self.records if r.grade is not None]
        if not grades:
            return None
        return sum(grades) / len(grades)


class Faculty:
    def __init__(self, name):
        self.name = name
        self.specialties = []
        self.departments = []
        self.disciplines = []
        self.students = {}
        self.next_id = 1

    def get_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError(f"Студент с ID {student_id} не найден")
        return self.students[student_id]

    def get_discipline(self, name):
        for d in self.disciplines:
            if d.name.lower() == name.strip().lower():
                return d
        raise FacultyError(f"Дисциплина «{name}» не найдена")

    def enroll_student(self, name, specialty):
        if specialty not in self.specialties:
            raise FacultyError(f"Специальность «{specialty}» не найдена")
        if not name.strip():
            raise FacultyError("ФИО не может быть пустым")
        student = Student(self.next_id, name.strip(), specialty)
        self.students[student.id] = student
        self.next_id += 1
        return student

    def expel_student(self, student_id):
        student = self.get_student(student_id)
        del self.students[student_id]
        return student

    def add_student_to_discipline(self, student_id, discipline_name):
        student = self.get_student(student_id)
        discipline = self.get_discipline(discipline_name)
        department = None
        for d in self.departments:
            if d.teaches(student.specialty, discipline):
                department = d
        if department is None:
            raise CourseNotAvailableError(
                f"Ни одна кафедра не читает «{discipline.name}» для специальности «{student.specialty}»"
            )
        if student.find_current(discipline):
            raise AlreadyEnrolledError(f"Студент уже изучает «{discipline.name}»")
        student.records.append(Record(discipline, department, student.semester))

    def remove_student_from_discipline(self, student_id, discipline_name):
        student = self.get_student(student_id)
        discipline = self.get_discipline(discipline_name)
        record = student.find_current(discipline)
        if record is None:
            raise NotEnrolledError(f"Студент не изучает «{discipline.name}»")
        student.records.remove(record)

    def set_grade(self, student_id, discipline_name, grade):
        student = self.get_student(student_id)
        discipline = self.get_discipline(discipline_name)
        if not isinstance(grade, int) or not 2 <= grade <= 5:
            raise InvalidGradeError("Оценка должна быть целым числом от 2 до 5")
        record = student.find_current(discipline)
        if record is None:
            raise NotEnrolledError(f"Студент не изучает «{discipline.name}»")
        record.grade = grade

    def promote_student(self, student_id):
        student = self.get_student(student_id)
        records = student.current_records()
        if not records:
            raise PromotionError("Студент не изучает ни одной дисциплины")
        for r in records:
            if r.grade is None:
                raise PromotionError(f"Нет оценки по «{r.discipline.name}»")
            if r.grade < 3:
                raise PromotionError(f"Дисциплина «{r.discipline.name}» не сдана")
        student.semester += 1

    def save_report(self, student_id):
        student = self.get_student(student_id)
        lines = [
            f"Ведомость успеваемости. {self.name}",
            f"Студент: {student.name} (ID {student.id})",
            f"Специальность: {student.specialty}",
            f"Семестр: {student.semester}",
            "",
        ]
        for r in student.records:
            grade = r.grade if r.grade is not None else "нет оценки"
            lines.append(
                f"Семестр {r.semester}: {r.discipline.name} | {r.department.name} | {grade}"
            )
        average = student.average()
        lines.append("")
        lines.append("Средний балл: " + (f"{average:.2f}" if average is not None else "нет оценок"))
        filename = f"report_{student.id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        return filename


def create_faculty():
    faculty = Faculty("Факультет информационных технологий")
    faculty.specialties = ["Прикладная информатика", "Кибербезопасность"]

    math = Department("Кафедра математики")
    soft = Department("Кафедра программной инженерии")
    sec = Department("Кафедра информационной безопасности")
    faculty.departments = [math, soft, sec]

    calculus = Discipline("Математический анализ")
    python = Discipline("Python")
    databases = Discipline("Базы данных")
    crypto = Discipline("Криптография")
    networks = Discipline("Защита сетей")
    faculty.disciplines = [calculus, python, databases, crypto, networks]

    pi, kb = faculty.specialties
    math.add_course(pi, calculus)
    math.add_course(kb, calculus)
    soft.add_course(pi, python)
    soft.add_course(kb, python)
    soft.add_course(pi, databases)
    sec.add_course(kb, crypto)
    sec.add_course(kb, networks)

    faculty.enroll_student("Иванов Иван", pi)
    faculty.enroll_student("Петрова Анна", kb)
    return faculty


def show_student(student):
    print(f"Студент: {student.name} (ID {student.id})")
    print(f"Специальность: {student.specialty}")
    print(f"Семестр: {student.semester}")
    for r in student.current_records():
        grade = r.grade if r.grade is not None else "нет оценки"
        print(f"  {r.discipline.name} | {r.department.name} | {grade}")
    average = student.average()
    print("Средний балл:", f"{average:.2f}" if average is not None else "нет оценок")


def work_with_student(faculty, student_id):
    while True:
        student = faculty.get_student(student_id)
        print(f"\nСтудент: {student.name} (ID {student.id})")
        print("1. Информация")
        print("2. Записать на дисциплину")
        print("3. Удалить из списка изучающих дисциплину")
        print("4. Выставить оценку")
        print("5. Перевести в следующий семестр")
        print("6. Отчислить")
        print("7. Сформировать ведомость")
        print("0. Назад")
        choice = input("Выбор: ").strip()
        try:
            if choice == "0":
                return
            elif choice == "1":
                show_student(student)
            elif choice == "2":
                print("Дисциплины факультета:", ", ".join(d.name for d in faculty.disciplines))
                faculty.add_student_to_discipline(student_id, input("Дисциплина: "))
                print("Студент записан на дисциплину")
            elif choice == "3":
                faculty.remove_student_from_discipline(student_id, input("Дисциплина: "))
                print("Студент удалён из списка изучающих дисциплину")
            elif choice == "4":
                discipline = input("Дисциплина: ")
                grade = int(input("Оценка (2-5): "))
                faculty.set_grade(student_id, discipline, grade)
                print("Оценка выставлена")
            elif choice == "5":
                faculty.promote_student(student_id)
                print("Студент переведён в следующий семестр")
            elif choice == "6":
                faculty.expel_student(student_id)
                print("Студент отчислен")
                return
            elif choice == "7":
                print("Ведомость сохранена в файл", faculty.save_report(student_id))
            else:
                print("Неизвестный пункт меню")
        except FacultyError as e:
            print("Ошибка:", e)
        except ValueError:
            print("Ошибка: нужно ввести целое число")


def main():
    faculty = create_faculty()
    while True:
        print(f"\n{faculty.name}")
        print("1. Работать со студентом (по ID)")
        print("2. Зачислить нового студента")
        print("3. Список студентов")
        print("0. Выход")
        choice = input("Выбор: ").strip()
        try:
            if choice == "0":
                break
            elif choice == "1":
                student_id = int(input("ID студента: "))
                faculty.get_student(student_id)
                work_with_student(faculty, student_id)
            elif choice == "2":
                print("Специальности:", ", ".join(faculty.specialties))
                name = input("ФИО: ")
                specialty = input("Специальность: ").strip()
                for s in faculty.specialties:
                    if s.lower() == specialty.lower():
                        specialty = s
                student = faculty.enroll_student(name, specialty)
                print(f"Студент зачислен, ID: {student.id}")
            elif choice == "3":
                for s in faculty.students.values():
                    print(f"{s.id}: {s.name}, {s.specialty}, семестр {s.semester}")
            else:
                print("Неизвестный пункт меню")
        except FacultyError as e:
            print("Ошибка:", e)
        except ValueError:
            print("Ошибка: нужно ввести целое число")


main()
