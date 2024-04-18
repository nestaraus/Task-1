import Menu
import Functions

def console():
    terminal = ''
    while terminal != '7':
        Menu.menu()
        terminal = input().strip()
        if terminal == '1':
            Functions.show('all')
        if terminal == '2':
            Functions.add()
        if terminal == '3':
            Functions.show('all')
            Functions.id_functions('delite')
        if terminal == '4':
            Functions.show('all')
            Functions.id_functions('edit')
        if terminal == '5':
            Functions.show('id')
            Functions.id_functions('show')
        if terminal == '6':
            Functions.show('time')
        if terminal == '7':
            break
            