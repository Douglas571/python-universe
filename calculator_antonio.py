#basic calculator development
#i only use one .py for all the implementations
# -- Groundbullet --

import math as _mathlib

OPTARGLIST = ( 1,  #sum
               2,  #sub
               3,  #mul
               4 ) #div

strlist  = ( "Add", "Substract", "Multiply", "Divide" )
stroplst = ( "Enter the left operand value:", "Enter the right operand value:" )

regLeftList  = [] #register list of x
regRightList = [] #register list of y
regResList   = [] #register list of result

#first, we need to stablish the methods:

def add ( var_x, var_y ):
     return float( var_x + var_y )

def sub ( var_x, var_y ):
     return float( var_x - var_y )

def mul ( var_x, var_y ):
     return float( var_x * var_y )

def div ( var_x, var_y ):
     return float( var_x / var_y )

#at this point, we need to handle the user input

def OPTHANDLE ( var_xf, var_yf, var_opt ):
     var_result = 0.0
     if  ( var_opt == OPTARGLIST[0] ):
            var_result = add ( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[1] ):
            var_result = sub( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[2] ):
            val_result = mul( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[3] ):
            val_result = div( var_xf, var_yf )
     else:
          return "Invalid Operation"
     
     regLeftList.append ( var_xf )
     regRightList.append( var_yf )
     regResList.append  ( var_result )
     
     return var_result
#end of function

#now we can use all the methods defined to build a simple calculator

def entrypoint__( ):
     var_opt    = 0
     var_xop    = 0.0
     var_yop    = 0.0
     var_result = 0.0
     print( "Choose the option\n" )
     print( "1 - " + strlist[0] )
     print( "2 - " + strlist[1] )
     print( "3 - " + strlist[2] )
     print( "4 - " + strlist[3] )
     var_opt = input()
     print( stroplst[0] )
     var_xop = input()
     print( stroplst[1] )
     var_yop = input()
     var_result = OPTHANDLE( var_xop, var_yop, var_opt )
     print( var_result )
#end of function

#we need to handle a loop for the app lifecycle

def Main ( ):
     var_bsucess    = 0
     var_opt        = 0
     while( var_bsucess == 0 ):
          entrypoint__()
          print( "Do you want to quit ? \n 1 - Yes \n Any other key - No" )
          var_opt = input()
          if( var_opt == 1 ):
               var_bsucess = 1
               break
          elif( var_opt != 1 ):
               continue
     #end of loop
#end of function

#last of all, we need to call main for call the options automatically

Main()

#greetings \n.n/
