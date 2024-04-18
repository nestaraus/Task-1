import uuid
from datetime import datetime

class Notes:
    def __init__(param, id = str(uuid.uuid4())[0:3], name = "text", note = "text", time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        param.id = id
        param.name = name
        param.note = note
        param.time = time
    
    def get_out(notes):
        return notes.id + ';' + notes.name + ';' + notes.note + ';' +  notes.time 
    
    def add_id(notes):
        notes.id = str(uuid.uuid4())[0:3]
    def add_name(notes,name):
        notes.name = name
    def add_note(notes, note):
        notes.note = note
    def add_time(notes):
        notes.time = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        
    def get_id(notes):
        return notes.id
    def get_name(notes):
        return notes.name
    def get_note(notes):
        return notes.note
    def get_time(notes):
        return notes.time
    def get_description(notes):
        return '\nid: ' + notes.id + '\n' + 'Заголовок: ' + notes.name + '\n' + 'Заметка: ' + notes.note + '\n' + 'Время создания: ' + notes.time