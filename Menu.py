import Notes

def menu ():
    print('Выбирите необходимое действие \n1: Посмотреть список заметок\n2: Добавить новую заметку\n3: Удалить заметку\n4: Редактирование заметки\n5: Вывод выбранной заметки\n6: Выборка по дате создания\n7: Выход')

def input_note():
    a = input_text(
        input('Введите заголовок заметки: '))
    b = input_text(
        input('Введите заметку: '))
    return Notes.Notes(name=a, note=b)

def input_text(text):
        return text