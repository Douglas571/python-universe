#traits file of reminder program
#here is the handle of the most basic structures
#i take care about the returning types because the python versions varying in the threatment
#-- gbull --


import datetime as time_t #we need to import the time traits in order to get the actual datetime

vec_dat_tmp_date      = [2] #dynamic vector what changes each time what the user try to register a reminder (date)
vec_tim_tmp_time      = [2] #same as above (time)

class Reminder:
     def __init__(self, title, content):
          self.title = title
          self.content = content
          self.date = time_t.datetime.now()

     def __str__(self):
          string  = f'Title: {self.title}\n' 
          string += f'Content: {self.content}\n'
          string += f'Date: {self.date}\n'

          return string



class reminder:     #regent object
     #object data:
     vec_time_at  = [] #time: 12:00 by example
     vec_date_at  = [] #date: 12/11 by example
     str_title    = ""  #main title: birthday by example
     str_desc     = ""  #other notes: its it birthay, buy a cake
     
     #object methods:
     def _reminder_cst(self, time_vec, date_vec, title_str, desc_str ):
          vec_time_at[0] = int( time_vec[0] )
          vec_time_at[1] = int( time_vec[1] )

          vec_date_at[0] = int( date_vec[0] )
          vec_date_at[1] = int( date_vec[1] )

          str_title = str( title_str )
          str_desc  = str( desc_str  )
     #end of method
          
#end of class

def Date_registry( ivar_day, ivar_month ):
     vec_dat_tmp_date[0] = int( ivar_day )
     vec_dat_tmp_date[1] = int( ivar_month )
#end of function

def Time_registry( ivar_hour: int, ivar_mins: int ):
     vec_tim_tmp_time[0] = int( ivar_hour )
     vec_tim_tmp_time[1] = int( ivar_mins )
#end of function

def Get_actual_time( ):
     return time_t.now
#end of function
