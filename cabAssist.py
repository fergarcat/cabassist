#    _____      _                        _     _
#   / ____|    | |         /\           (_)   | |
#  | |     __ _| |__      /  \   ___ ___ _ ___| |_
#  | |    / _` | '_ \    / /\ \ / __/ __| / __| __|
#  | |___| (_| | |_) |  / ____ \\__ \__ \ \__ \ |_
#   \_____\__,_|_.__/  /_/    \_\___/___/_|___/\__|

import time
import os
import sys
from ClassRide import *
from ClassTimer import *
from texts import *
from menu import *



   
Rides = []
currentRide = Ride()
waitfee = 0.02
drivefee = 0.05
waitTimer = Timer()
driveTimer = Timer()


#Main function
def main():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    menu_welcome()
    input()


#Exits the program          
def exit_program():
  print(f'\n\n\t{txt_quit}\n\n')
  time.sleep(3)
  quit()



#Displays home menu
def menu_home():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    option = menu_display('home',currentRide,Rides,waitfee,drivefee)
    
    if option == "R":
          
          currentRide = Ride()
          waitTimer = Timer()
          driveTimer = Timer()
          driveTimer.restart
          waitTimer.restart
          menu_wait()
    if option == "S":
          menu_setup()
    elif option == "Q":
          exit_program()
    else:
          menu_display('wrong',currentRide,Rides,waitfee,drivefee)
          menu_home()

# Displays waiting menu
def menu_wait():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    while True:
        option = menu_display('wait',currentRide,Rides,waitfee,drivefee)
        if option == "D":
            currentRide.waitMeter = currentRide.waitMeter + waitTimer.get_time()
            menu_drive()
        elif option == "E":
            menu_end()
        else:
            menu_display('wrong',currentRide,Rides,waitfee,drivefee)
            menu_wait()

#Displays driving menu
def menu_drive():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    while True:
        option = menu_display('drive',currentRide,Rides,waitfee,drivefee)
        if option == "S":
          currentRide.driveMeter = currentRide.driveMeter + driveTimer.get_time()
          menu_wait()
        else:
          menu_display('wrong',currentRide,Rides,waitfee,drivefee)
          menu_drive()

#Displays end of currentRide message and total fare to pay
def menu_end():
        global Rides
        global currentRide
        global waitfee
        global drivefee
        global waitTimer
        global driveTimer
        currentRide.Fare = total_fare(currentRide, waitfee, drivefee)
        currentRide.endTime = time.time()
        Rides.append(currentRide)
        menu_display('end',currentRide,Rides,waitfee,drivefee)
        currentRide.reset(waitfee,drivefee)
        menu_home()

#Displays configuration options
def menu_setup():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    while True:
        option = menu_display('setup',currentRide,Rides,waitfee,drivefee)
        if option == "D":
            while True:
                try:
                    drivefee = float(input(f'{txt_enter_drive_fee}'))
                    menu_setup()
                except ValueError:
                    menu_display('wrong',currentRide,Rides,waitfee,drivefee)
                    menu_setup()
        elif option == "W":            
            while True:
                try:
                    waitfee = float(input(f'{txt_enter_wait_fee}'))
                    menu_display('setup',currentRide,Rides,waitfee,drivefee)
                except ValueError:
                    menu_display('wrong',currentRide,Rides,waitfee,drivefee)
                    menu_setup()
        elif option == "M":
            menu_home()
        else:
            menu_display('wrong',currentRide,Rides,waitfee,drivefee)
            menu_setup()    


# Shows welcome message
def menu_welcome():
    global Rides
    global currentRide
    global waitfee
    global drivefee
    global waitTimer
    global driveTimer
    menu_display('welcome',currentRide,Rides,waitfee,drivefee)
    menu_home()




main()