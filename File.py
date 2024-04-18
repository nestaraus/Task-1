import Notes

def read_file():
    try:
        array = []
        file = open("task.json","r",encoding='utf-16')
        task = file.read().strip().split("\n")
        for i in task:
            split_i = i.split(';')
            tasks = Notes.Notes(
                id = split_i[0], name = split_i[1], note = split_i[2], time = split_i[3]) 
            array.append(tasks)
    except Exception:
        print ('Заметок нет')
    finally:
        return array
        

def write_file(array, mode):
    file = open("task.json", mode='w',encoding='utf-16')
    file.seek(0)
    file.close()
    file = open("task.json", mode=mode, encoding='utf-16')
    for task in array:
        file.write(Notes.Notes.get_out(task))
        file.write('\n')
    file.close