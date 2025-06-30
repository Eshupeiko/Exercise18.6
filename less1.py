# создаем словарь
translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# выводим английские слова, которые сохранены в словаре
print(f'Слова в словаре: {translator.keys()}')

# считываем слово, которое нужно перевести
eng_word = input('Введите слово, которое нужно удалить: ')
if eng_word in translator.keys():
    del translator[eng_word]
    print('Задача выполнена')
    print(f'Отредактированный словарь:')
    for key, value in translator.items():
        # выводим пары ключ - значение
        print(f'{key} - {value}')

else:
    print("Этого слова нет в словаре")
    for key, value in translator.items():
            # выводим пары ключ - значение
            print(f'{key} - {value}')
    print(f'Исходный словарь:')
