#basic calculator development
#i only use one .py for all the implementations
# -- Groundbullet --

import math as _mathlib
import sys

DEBUG = False
if sys.argv[1] == 'debug':
     DEBUG = True
     print(f'Debugging!!')
else:
     DEBUG = False

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
     if DEBUG:
          print(f'var_x: {var_x}, type: {type(var_x)}')
          print(f'var_y: {var_y}, type: {type(var_y)}')

     return var_x + var_y

def sub ( var_x, var_y ):
     return var_x - var_y

def mul ( var_x, var_y ):
     return var_x * var_y

def div ( var_x, var_y ):
     return var_x / var_y

#at this point, we need to handle the user input

def OPTHANDLE ( var_xf, var_yf, var_opt ):

     if DEBUG:
          res = OPTARGLIST[0] == var_opt
          print(f'the operation is: {var_opt}')
          print(f'the OPTARGLIST[0] is: {OPTARGLIST[0]}')
          print(f'the comparison is: {res}')

          print(f'the type of var_opt is: {type(var_opt)}')
     
     var_result = 0.0
     if  ( var_opt == OPTARGLIST[0] ):
          var_result = add ( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[1] ):
          var_result = sub( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[2] ):
          var_result = mul( var_xf, var_yf )
     elif( var_opt == OPTARGLIST[3] ):
          var_result = div( var_xf, var_yf )
     else:
          return "Invalid Operation"
     
     regLeftList.append( var_xf )
     regRightList.append( var_yf )
     regResList.append( var_result )
     
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
     var_opt = int(input())
     print( stroplst[0] )
     var_xop = float(input())
     print( stroplst[1] )
     var_yop = float(input())
     var_result = OPTHANDLE( var_xop, var_yop, var_opt )
     print( var_result )
#end of function

#we need to handle a loop for the app lifecycle

def Main ( ):
     var_bsucess    = 1
     var_opt        = 0
     while( var_bsucess == 1 ):
          entrypoint__()
          print( "Do you want to quit ? \n 1 - Yes \n Any other key - No" )
          var_opt = input()

          if DEBUG:
               print(f'var_opt: {var_opt}, type: {type(var_opt)} ')

          if( var_opt == '1' ):
               var_bsucess = 1
          else:
               var_bsucess = 0
     #end of loop
#end of function

#last of all, we need to call main for call the options automatically

Main()

#greetings \n.n/
