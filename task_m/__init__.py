#main program ( reminder )
#-- gbull --
#for information about the API check the DOCHANDLE.py
#you MUST not include that file as import

import rem_g_handle as rHandle
import rem_g_traits as rTraits
from rem_g_traits import Reminder

import datetime

#bueno, te toca XD

"""

    Criterios de aceptación:

        
        - listo - ver todas las notas
        - listo - agregar
        - editar
        - eliminar
    
    task-data-structure
        title
        date
        content

"""          

APP = rHandle.HREMINDER()

def main():
    keep_working = True

    APP.add(Reminder('example1', 'content1'))

    while keep_working:
        print('[>]Reminder Manger')

        print(' > 1.View')
        print(' > 2.Add')
        print(' > 3.Edit')
        print(' > 4.Delete')

        print()
        print(' > 0.Exit')

        option = int(input('[?]:'))
        print()

        if option == 0:
            keep_working = False
        elif option == 1:
            view_reminders()

        elif option == 2:
            add_reminder()

        elif option == 3:
            edit_reminder()

        elif option == 4:
            delete_reminder()
        
def view_reminders():
    print('[>] Viewing reminders')
    from_this_day = input(' [?] from this day? (y/n): ')
    reminder_list = []
    if from_this_day == 'y':
        APP.scan_today_reminders()
    else:
        print('  [>] All reminders: \n')
        APP.check_for_reminders()

    input('[?] continue...')

def add_reminder():
    print('[>]Adding Reminder')

    title = input(' [?] title: ')
    content = input(' [?] reminder: ')

    APP.add(Reminder(title, content))

def edit_reminder():
    print('[>]Editing Reminder')

    id = int(input(' [?] id: '))
    title = input(' [?] title: ')
    content = input(' [?] reminder: ')

    if title == '': title = None
    if content == '': content = None

    new_data = Reminder(title, content)
    new_data.id = id

    APP.edit(new_data)

def delete_reminder():
    print('[>]Deleting Reminder')

    id = int(input(' [?] id:'))
    APP.delete(id)

if __name__ == '__main__':
    main()