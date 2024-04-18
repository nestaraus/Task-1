import Notes
import File
import Menu



def add():
    notes= Menu.input_note()
    array = File.read_file()
    for tasks in array:
        if Notes.Notes.get_id(notes) == Notes.Notes.get_id(tasks):
            Notes.Notes.add_id(notes)
    array.append(notes)
    File.write_file(array, 'a')
    print('Заметка сохранена')

def show(format):
    boolean = True
    array = File.read_file()
    if format == 'time':
        time = input('Введите дату в формате дд.мм.гггг')
    for tasks in array:
        if format == 'all':
            boolean = False
            print(Notes.Notes.get_description(tasks))
        if format == 'id':
            boolean = False
            print('id: '+ Notes.Notes.get_id(tasks))
        if format == 'time':
            boolean = False
            if time in Notes.Notes.get_time(tasks):
                print(Notes.Notes.get_description(tasks))
    if boolean == True:
        print('Заметок нет')

def id_functions(choise):
    id = input ('Введите id')
    array = File.read_file()
    boolean = True
    for tasks in array:
        if id == Notes.Notes.get_id(tasks):
            boolean = False
            if choise == 'edit':
                task = Menu.input_note()
                Notes.Notes.add_name(tasks, task.get_name())
                Notes.Notes.add_note(tasks, task.get_note())
                Notes.Notes.add_time(tasks)
                print('Вы изменили запись')
            if choise == 'delite':
                array.remove(tasks)
                print("Запись удалена")
            if choise == 'show':
                print(Notes.Notes.get_description(tasks))
    if boolean == True:
        print("Неверно введен id")
    File.write_file(array, 'a')

                    