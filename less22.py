# создаем словарь
translator = {'bug': 'ошибка', 'function': 'функция', 'approve': 'согласовать'}
# выводим английские слова, которые сохранены в словаре
print(f'Слова в словаре: {translator.keys()}')

# считываем слово, которое нужно перевести
eng_word = input('Введите слово, которое нужно удалить: ')
if eng_word in translator.keys():
    del translator[eng_word]
