#    _____      _                        _     _
#   / ____|    | |         /\           (_)   | |
#  | |     __ _| |__      /  \   ___ ___ _ ___| |_
#  | |    / _` | '_ \    / /\ \ / __/ __| / __| __|
#  | |___| (_| | |_) |  / ____ \\__ \__ \ \__ \ |_
#   \_____\__,_|_.__/  /_/    \_\___/___/_|___/\__|

import time
import os
import sys
from ride import *
from timer import *
from texts import *

Rides = []

waitfee = 0.02
drivefee = 0.05




# Def formatTime. Convert float time values to HH:MM:SS format
def formatTime(t):
  struct_time = time.localtime(t)
  formatted_time = time.strftime("%H:%M:%S", struct_time)
  return(formatted_time)

#Displays app logo
def display_logo():
    os.system('cls')
    print('\n\n')
    print(f'{txt_logo_1}')
    print(f'{txt_logo_2}')
    print(f'{txt_logo_3}')
    print(f'{txt_logo_4}')
    print(f'{txt_logo_5}')
    print(f'{txt_logo_6}')
    print(f'{txt_logo_7}')

#Displays fees
def display_fees():
    print(f'{txt_current_drive_fee:} {drivefee}\t{txt_current_wait_fee:} {waitfee}\n')
#Displays wrong input message
def display_wrong_input():
    os.system('cls')
    display_logo()
    print(f'{txt_wrong_input}')
    time.sleep(2)
#Displays current drive data
def display_drive(ride : Ride):
    print(f'{txt_ride_start} {formatTime(ride.startTime)}\n{txt_current_time} {formatTime(time.time())}\n{txt_run_length} {round(ride.driveMeter,2)} {txt_sec}\n{txt_wait_length} {round(ride.waitMeter,2)} {txt_sec}\n')
#Display single ride
def display_Ride(ride : Ride):
    print(f'\tStart: {formatTime(ride.startTime)} End: {formatTime(ride.endTime)} Drive: {round(ride.driveMeter,2)} Wait: {round(ride.waitMeter,2)} Fare: {ride.Fare}\n')
#Displays last 3 rides
def display_last_rides():
    print(f'{txt_last_drives}')
    if len(Rides) < 3:
        minRide = 0
        maxRide = len(Rides)-1
    else:
        minRide = len(Rides) - 3  # Esto asegura que minRide esté correctamente calculad
        maxRide = len(Rides)-1

    i = maxRide
    while i >= minRide:
        display_Ride(Rides[i])
        i -= 1

#Calculates total fare
def total_fare(ride : Ride):
          return(round((ride.driveMeter * drivefee) + (ride.waitMeter * waitfee),2))

#Displays welcome menu
def menu_home():
    os.system('cls')
    display_logo()
    display_fees()
    if Rides != []:
        display_last_rides()
    print(f'{txt_options}')
    option = input(f'{txt_menu_home}').upper()
    if option == "R":
          ride = Ride()
          menu_wait(ride)
    if option == "S":
          menu_setup()
    elif option == "Q":
          exit_program()
    else:
          display_wrong_input()
          menu_home()

# Displays waiting menu
def menu_wait(ride : Ride):
    waitTimer = Timer()
    while True:
        os.system('cls')
        display_logo()
        display_fees()
        display_drive(ride)
        print(f'{txt_options}')
        option = input(f'{txt_msg_wait}').upper()
        if option == "D":
            ride.waitMeter = ride.waitMeter + waitTimer.get_time()
            menu_drive(ride)
        elif option == "E":
            ride.Fare = total_fare(ride)
            ride.endTime = time.time()
            Rides.append(ride)
            menu_end(ride)
        else:
            display_wrong_input()
            menu_wait(ride)
#Displays driving menu
def menu_drive(ride : Ride):
  driveTimer = Timer()
  while True:
      os.system('cls')
      display_logo()
      display_fees()
      display_drive(ride)
      print(f'{txt_options}')
      option = input(f'{txt_msg_drive}').upper()
      if option == "S":
          ride.driveMeter = ride.driveMeter + driveTimer.get_time()
          menu_wait(ride)
      else:
          display_wrong_input()
          menu_drive(ride)

#Displays end of ride message and total fare to pay
def menu_end(ride : Ride):
        os.system('cls')
        display_logo()
        display_fees()
        display_drive(ride)
        print(f'{txt_end} {ride.Fare} ')
        print(f'{txt_press_enter}')
        input()
        menu_home()

#Displays configuration options
def menu_setup():
    os.system('cls')
    display_logo()
    display_fees()
    while True:
        option = input(f'{txt_msg_setup}').upper()
        if option == "D":
            global drivefee
            while True:
                try:
                    drivefee = float(input(f'{txt_enter_drive_fee}'))
                    menu_setup()
                except ValueError:
                    display_wrong_input()
                    menu_setup()
        elif option == "W":
            global waitfee
            while True:
                try:
                    waitfee = float(input(f'{txt_enter_wait_fee}'))
                    menu_setup()
                except ValueError:
                    display_wrong_input()
                    menu_setup()
        elif option == "M":
            menu_home()
        else:
            display_wrong_input()
            menu_setup()    

#Exits the program          
def exit_program():
  display_logo()
  print(f'\n\n\t{txt_quit}\n\n')
  time.sleep(3)
  quit()

# Shows welcome message
def menu_welcome():
    os.system('cls')
    display_logo()
    print(f'{txt_welcome}')
    print(f'{txt_press_enter}')
    input()
    menu_home()

#Main function
def main():
   menu_welcome()

main()
