#handler class for the reminder system
#-- gbull --

import rem_g_traits as rTraits #reminder_traits imp
from rem_g_traits import Reminder

import datetime

class HREMINDER:
     reminder_list = []
     last_id =  0

     # Recuerda pasar "self" como primer 
     # parametro para los metodos de una clase
     def add(self, reminder):
          self.last_id += 1
          reminder.id = self.last_id
          self.reminder_list.append( reminder )

     def edit(self, new_data):
          # enumerate() devuelve un iterator cuyo primer elemento 
          # es el indice y el segundo elemento es el element en sí
          for idx, rem in enumerate(self.reminder_list):

               if rem.id == new_data.id:
                    if not new_data.title:
                         new_data.title = rem.title

                    if not new_data.content:
                         new_data.content = rem.content

                    self.reminder_list[idx] = new_data

     def delete(self, id):
          self.reminder_list = [rem for rem in self.reminder_list if rem.id != id]
          #Esto es lo que en python llamamos "list comprehensions"
          # lo que hace es ciclar a trabes de los elementos en reminder_list
          # y verifica que el id sea diferente al especificado,
          # de esa forma el recordatorio a eliminar queda por 
          # fuera de la lista.

     def kill_reminder(self, reminder_data):
          if reminder_list:
               self.reminder_list.remove(reminder_data)

     def check_for_reminders(self):
          for reminder in self.reminder_list:
              print(reminder)

     def scan_today_reminders(self):
          vec_remstack = []

          today = datetime.date.today()

          for rem in self.reminder_list:
               date = rem.date
               if date.year == today.year and date.month == today.month and date.day == today.day:
                    vec_remstack.append(rem)
                  
          if vec_remstack:
               print("Today Reminders:")
               for rem in vec_remstack:
                    print(rem)

          else:
               print("There are not reminders today")
                  
