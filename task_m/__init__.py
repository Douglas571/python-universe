#main program ( reminder )
#-- gbull --
#for information about the API check the DOCHANDLE.py
#you MUST not include that file as import

import rem_g_handle as rHandle
import rem_g_traits as rTraits

#bueno, te toca XD

"""

    Criterios de aceptación:

        
        - ver todas las notas
        - agregar
        - editar
        - eliminar
    
    task-data-structure
        title
        date
        content

"""          

def main():
    keep_working = True
    while keep_working:
        print('Task Manger')

        print(' > 1.View')
        print(' > 2.Add')
        print(' > 3.Edit')
        print(' > 4.Delete')

        print()
        print(' > 0.Exit')

        option = int(input('[?]:'))

        if option == 0:
            keep_working = False
        elif option == 1:
            
        

if __name__ == '__main__':
    main()