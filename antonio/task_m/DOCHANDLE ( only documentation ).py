#DOCHANDLE spanish
#Documento descriptor de las funciones, clases, variables y metodos del proyecto
#NO COMPILAR NI CORRER

el programa principal esta alojado en rem_Main.py, este empleara los metodos utilizados
en rem_g_handle y rem_g_traits. abajo dejo la descripcion de sus elementos para correcto uso

rem_g_traits:
     variables:
          vec_dat_tmp_date -> vector de 2 elementos que almacena la fecha en un formato de Dia  / Mes
          vec_tim_tmp_time -> vector de 2 elementos que almacena la hora  en un formato de Hora / Minutos

     importdata:
          datetime as time_t -> permite consultar la fecha y hora actuales

     funciones:
          Date_registry ( int day,  int month ) -> permite registrar datos en vec_dat_tmp_date de forma simplistica
          Time_registry ( int hour, int mins  ) -> permite registrar datos en ec_tim_tmp_time  de forma simplistica
          Get_actual_time( void** )             -> obtiene la fecha y hora actuales bajo la estructura time_t.now

     clases:
          reminder:
               variables:
                    vec_time_at -> vector propio para almacenar la hora en la cual empieza el evento
                    vec_date_at -> vector propio para almacenar la fecha del evento
                    str_title   -> Titulo del evento
                    str_desc    -> Descripcion del evento
                    
               metodos:
                    constructor:
                         _reminder_cst( vector(int) time, vector(int) date, string title, string date ) -> asigna las variables solicitadas a
                                                                                                           sus respectivos datos en la clase

rem_g_handle:
     variables:
          no_tiene ( x )

     importdata:
          rem_g_traits as rTraits -> importa rem_g_traits para usar las funciones determinadas

     funciones:
          como tal, no hay funciones mas alla del control de HREMINDER

     clases:
          HREMINDER:
               variables:
                    vec_rem_reminder_list -> vector responsable de contener los objetos de la clase reminder
                    int count             -> cuenta la cantidad de objetos reminder contenidos en el vector

               metodos:
                    Append_reminder ( reminder& data ) -> agrega un reminder a la lista
                    Kill_reminder   ( reminder& data ) -> quita un reminder ( no te garantizo que funcione dado que estas pasando un objeto y el trato que se le de a este es anomalo )
                    Check_for_reminders ( void** )     -> escanea vec_rem_reminder_list en busca de los reminder integrados en el
                    Scan_for today reminders( )        -> escanea vec_rem_reminder_list en busca de los reminder que coincidan en fecha con la fecha actual
                    
