import time
from ClassRide import *
from ClassTimer import *
from texts import *
from menu import *

#Global variables
   
Rides = []
currentRide = Ride()
waitfee = 0.02
drivefee = 0.05
waitTimer = Timer()
driveTimer = Timer()
filename = 'rides.csv'

#Main function
def main():
    menu_welcome()
    input()

#Displays home menu
def menu_home():
    option = menu_display('home',currentRide,Rides,waitfee,drivefee, filename)
    if option == "R":
          currentRide.reset(waitfee,drivefee)
          waitTimer.restart()
          driveTimer.restart()
          menu_wait()
    if option == "S":
          menu_setup()
    if option == "L":
          menu_list()
    elif option == "Q":
          exit_program()
    else:
          menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
          menu_home()

# Displays waiting menu
def menu_wait():
    waitTimer.restart()
    while True:
        option = menu_display('wait',currentRide,Rides,waitfee,drivefee, filename)
        if option == "D":
            currentRide.waitMeter = currentRide.waitMeter + waitTimer.get_time()
            menu_drive()
        elif option == "E":
            currentRide.waitMeter = currentRide.waitMeter + waitTimer.get_time()
            menu_end()
        else:
            menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
            menu_wait()
 
 #Displays driving menu
def menu_drive():
    driveTimer.restart()
    while True:
        option = menu_display('drive',currentRide,Rides,waitfee,drivefee, filename)
        if option == "S":
          currentRide.driveMeter = currentRide.driveMeter + driveTimer.get_time()
          menu_wait()
        else:
          menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
          menu_drive()

#Displays end of currentRide message and total fare to pay
def menu_end():
        currentRide.Fare = total_fare(currentRide, waitfee, drivefee)
        currentRide.endTime = time.time()
        save_data(currentRide,filename)
        menu_display('end',currentRide,Rides,waitfee,drivefee, filename)
        menu_home()

#Displays configuration options
def menu_setup():
    global drivefee
    global waitfee
    while True:
        option = menu_display('setup',currentRide,Rides,waitfee,drivefee, filename)
        if option == "D":
            while True:
                try:
                    drivefee = float(input(f'{txt_enter_drive_fee}'))
                    menu_setup()
                except ValueError:
                    menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
                    menu_setup()
        elif option == "W":            
            while True:
                try:
                    waitfee = float(input(f'{txt_enter_wait_fee}'))
                    menu_display('setup',currentRide,Rides,waitfee,drivefee, filename)
                except ValueError:
                    menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
                    menu_setup()
        elif option == "M":
            menu_home()
        else:
            menu_display('wrong',currentRide,Rides,waitfee,drivefee, filename)
            menu_setup()    



# Shows welcome message
def menu_welcome():
    menu_display('welcome',currentRide,Rides,waitfee,drivefee, filename)
    menu_home()

# Shows last rides
def menu_list():
    global filename
    menu_display('list',currentRide,Rides,waitfee,drivefee, filename)
    menu_home()    

main()