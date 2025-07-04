import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        5. Редактировать оценку
        6. Удалить оценку
        7. Удалить предмет у ученика
        8. Удалить ученика
        9. Показать оценки конкретного ученика
        10. Средний балл по каждому предмету для конкретного ученика
        11. Добавить нового ученика
        12. Добавить новый предмет
        ''')
while True:
    command = int(input('Введите команду: '))

    if command == 1:
        # Добавление оценки
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        # Средний балл по всем предметам
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        # Вывод всех оценок
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Выход из программы')
        break

    elif command == 5:
        # Редактирование оценки
        student = input('Введите имя ученика: ')
        if student not in students_marks:
            print('ОШИБКА: неверное имя ученика')
            continue
        class_ = input('Введите предмет: ')
        if class_ not in students_marks[student]:
            print('ОШИБКА: предмет не найден')
            continue
        print('Текущие оценки:', students_marks[student][class_])
        index = int(input('Введите индекс оценки для редактирования (0-based): '))
        if 0 <= index < len(students_marks[student][class_]):
            new_mark = int(input('Введите новую оценку: '))
            students_marks[student][class_][index] = new_mark
            print('Оценка обновлена')
        else:
            print('Неверный индекс')

    elif command == 6:
        # Удаление оценки
        student = input('Введите имя ученика: ')
        if student not in students_marks:
            print('ОШИБКА: неверное имя ученика')
            continue
        class_ = input('Введите предмет: ')
        if class_ not in students_marks[student]:
            print('ОШИБКА: предмет не найден')
            continue
        print('Текущие оценки:', students_marks[student][class_])
        index = int(input('Введите индекс оценки для удаления (0-based): '))
        if 0 <= index < len(students_marks[student][class_]):
            del students_marks[student][class_][index]
            print('Оценка удалена')
        else:
            print('Неверный индекс')

    elif command == 7:
        # Удаление предмета
        student = input('Введите имя ученика: ')
        if student not in students_marks:
            print('ОШИБКА: неверное имя ученика')
            continue
        class_ = input('Введите предмет для удаления: ')
        if class_ in students_marks[student]:
            del students_marks[student][class_]
            print(f'Предмет {class_} удален для {student}')
        else:
            print('Предмет не найден')

    elif command == 8:
        # Удаление ученика
        student = input('Введите имя ученика для удаления: ')
        if student in students:
            students.remove(student)
            del students_marks[student]
            print(f'Ученик {student} удален')
        else:
            print('Ученик не найден')

    elif command == 9:
        # Оценки конкретного ученика
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Оценки для {student}:')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print('Ученик не найден')

    elif command == 10:
        # Средний балл по предмету
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Средний балл по предметам для {student}:')
            for class_ in classes:
                marks = students_marks[student][class_]
                avg = sum(marks) / len(marks)
                print(f'\t{class_} - {avg:.1f}')
        else:
            print('Ученик не найден')

    elif command == 11:
        # Добавление нового ученика
        new_student = input('Введите имя нового ученика: ')
        if new_student in students:
            print('Ученик уже существует')
        else:
            students.append(new_student)
            students.sort()
            students_marks[new_student] = {}
            for class_ in classes:
                students_marks[new_student][class_] = [random.randint(1, 5) for _ in range(3)]
            print(f'Ученик {new_student} добавлен')

    elif command == 12:
        # Добавление нового предмета
        new_class = input('Введите название нового предмета: ')
        if new_class in classes:
            print('Предмет уже существует')
        else:
            classes.append(new_class)
            for student in students_marks:
                students_marks[student][new_class] = [random.randint(1, 5) for _ in range(3)]
            print(f'Предмет {new_class} добавлен')