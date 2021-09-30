#handler class for the reminder system
#-- gbull --

import rem_g_traits as rTraits #reminder_traits imp

class HREMINDER:
     #handle data ( 2 items ):
     reminder_list = [] #strictly list treatment for the reminder obj
     ivar_rem_count =  0  #count var for the reminders in list

     #handle methods:
     def Append_reminder( reminder_data ):
          reminder_list.append( reminder_data )
          ivar_rem_count = ivar_rem_count + 1
     #end of method

     def Kill_reminder( reminder_data ):
          if( ivar_rem_count > 0 ):
               reminder_list.remove( reminder_data )
               ivar_rem_count = ivar_rem_count - 1
          else:
               return
     #end of method

     def Check_for_reminders( ):
        ivar_count = 0
        while( ivar_count < ivar_rem_count ):
             print( "Title: " + str( reminder_list[ ivar_count ].str_title ) )
             print( "Date:  " + str( reminder_list[ ivar_count ].vec_time_at[0] ) + str( reminder_list[ ivar_count ].vec_time_at[1] ) )
             print( "Time:  " + str( reminder_list[ ivar_count ].vec_date_at[0] ) + str( reminder_list[ ivar_count ].vec_date_at[1] ) )
             print( "Notes: " + str( reminder_list[ ivar_count ].str_desc  ) )
             ivar_count = ivar_count + 1 
        #end of loop
     #end of method

     def Scan_today_reminders( ):
         ivar_count   =  0
         tday_count   =  0
         vec_remstack = [ ]
         while( ivar_count < ivar_rem_count ):
              if( int( reminder_list[ ivar_count ].vec_date_at[0] ) == int( rTraits.reminder.Get_actual_time().day ) and
                  int( reminder_list[ ivar_count ].vec_date_at[1] ) == int( rTraits.reminder.Get_actual_time().month ) ):
                   vec_remstack.append( reminder_list[ ivar_count ] )
                   tday_count = tday_count + 1
                   ivar_count = ivar_count + 1
              else:
                   ivar_count = ivar_count + 1
              #end of cond ( 2 ways )
          #end of loop
                  
         if( tday_count <= 0 ):
              print( "There are not reminders today" )
         else:
              ivar_cnt = 0
              print( "Today Reminders:" )
              while( ivar_cnt < tday_count ):
                  print( str( ivar_cnt + 1 ) + " - " + str( reminder_list[ ivar_cnt ].str_title ) )
                  print( str( reminder_list[ ivar_cnt ].str_desc ) )
                  ivar_cnt = ivar_cnt + 1
              #end of loop
         #end of cond ( 2 ways )
     #end of method
#end of class       
                  
