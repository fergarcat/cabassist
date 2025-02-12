#    _____      _                        _     _
#   / ____|    | |         /\           (_)   | |
#  | |     __ _| |__      /  \   ___ ___ _ ___| |_
#  | |    / _` | '_ \    / /\ \ / __/ __| / __| __|
#  | |___| (_| | |_) |  / ____ \\__ \__ \ \__ \ |_
#   \_____\__,_|_.__/  /_/    \_\___/___/_|___/\__|

import time
import os
import sys
from .ride import Ride
from .timer import Timer


Rides = []
txt_logo_1 = "\t\t   _____      _                        _     _   "
txt_logo_2 = "\t\t  / ____|    | |         /\           (_)   | |  "
txt_logo_3 = "\t\t | |     __ _| |__      /  \   ___ ___ _ ___| |_ "
txt_logo_4 = "\t\t | |    / _` | '_ \    / /\ \ / __/ __| / __| __|"
txt_logo_5 = "\t\t | |___| (_| | |_) |  / ____ \\__ \__ \ \__ \ |_"
txt_logo_6 = "\t\t  \_____\__,_|_.__/  /_/    \_\___/___/_|___/\__|"
txt_logo_7 = "\t\t\tSolution provided by FERGARCAT@GITHUB\n"
txt_welcome = "\t\t\t*** Welcome to Cab Assist! ***\nThis application is developed for educational purpose within the AI Bootcamp @FactoríaF5 \n""\nThis app offers taxi drivers a light and reliable solution to trace their rides.\nYou will be able to keep record of all your rides, change your fees and charge your customers.\n\n\t\t\t*** IMPLEMENTED FEATURES ***\n\t\t\tBASIC LEVEL:\n\t\t\t- Shows welcome message(this).\n\t\t\t- Start a new ride.\n\t\t\t- Keep record of the waiting fare.\n\t\t\t- Keep record of the riding fare.\n\t\t\t- End ride and calculate total fare.\n\t\t\t- Start a new ride without closing the app.\n\t\t\tMEDIUM LEVEL:\n\t\t\t- Setup Fee Options.\n\t\t\tADVANCED LEVEL:\n\t\t\t- Use of OOP code.\n\n\t\tVisit https://github.com/fergarcat/cabassist for more details."
txt_options = "\n\t\t\tPlease select one OPTION.\n"
txt_menu_home = "\t\t\t(R) To Start a New Ride\n\n\t\t\t(S) To SETUP Fees\n\n\t\t\t(Q) To Quit\n\n"
txt_msg_wait = "\t\t\t(D) Press To DRIVE\n\n\t\t\t(E) To END ride\n\n"
txt_msg_drive = "\t\t\tPress S to STOP driving.\n\t\t\tRide cant't be finished while driving."
txt_quit = "***Thanks for using Cab Assist. We are looking to see you again soon!***"
txt_wrong_input = "\t\t\t*** WRONG INPUT ***"
txt_run_length = "\t\t\tYou\'ve been driving for: "
txt_wait_length = "\t\t\tYou\'ve been waiting for: "
txt_sec = "seconds"
txt_ride_start = "\t\t\tYour ride has started at: "
txt_meter_start = "\n\t\t\tYou are STOPPED. Meter is running.\n\n"
txt_current_time = "\t\t\tCurrent time: "
txt_end = "\t\t\tYour drive has FINISHED. Total FARE: "
txt_press_enter = "\n\t\t\tPress any KEY to continue..."
txt_last_drives = "\tLast 3 DRIVES: \n"
txt_current_drive_fee = "\t\tCurrent Drive Fee: "
txt_current_wait_fee = " Current Wait Fee: "
txt_msg_setup = "\n\n\t\t\t*** Setup Fees ***\n\n\t\t\t(D) To change Drive Fee\n\t\t\t(W) To change Wait Fee\n\t\t\t(M) Back to MAIN Menu\n"
txt_enter_drive_fee = "\n\n\t\t\tEnter new Drive Fee: "
txt_enter_wait_fee = "\n\n\t\t\tEnter new Wait Fee: "
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
