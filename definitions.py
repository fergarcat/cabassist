from texts import *
import time
import os
import pandas as pd
from auth import authenticate_user
import getpass

#Displays last 3 rides
def display_last_rides(filename):
    Rides = []
    try:
        df = pd.read_csv(filename)
    except:
        os.system('cls')
        print(txt_error_reading_data)
        print(txt_press_enter)
        input()
    if not df.empty:
        df = df.sort_index(ascending=False)
        print(f'{txt_last_drives}')
        print(f'{df}')

#Displays current drive data
def display_drive(ride):
    print(f'{txt_ride_start} {formatTime(ride.startTime)}\n{txt_current_time} {formatTime(time.time())}\n{txt_run_length} {round(ride.driveMeter,2)} {txt_sec}\n{txt_wait_length} {round(ride.waitMeter,2)} {txt_sec}\n')

#Calculates total fare
def total_fare(ride, waitfee, drivefee):
          return(round((ride.driveMeter * drivefee) + (ride.waitMeter * waitfee),2))

#Displays fees
def display_fees(waitfee, drivefee):
    print(f'{txt_current_drive_fee:} {drivefee}\t{txt_current_wait_fee:} {waitfee}\n')

# Def formatTime. Convert float time values to HH:MM:SS format
def formatTime(t):
  struct_time = time.localtime(t)
  formatted_time = time.strftime("%H:%M:%S", struct_time)
  return(formatted_time)

#Save ride data to file
def save_data(currentRide,filename):
    # Create a DataFrame
    data = []
    data.append([formatTime(currentRide.startTime), formatTime(currentRide.endTime), currentRide.driveMeter, currentRide.waitMeter, currentRide.Fare])
    # Convert list to DataFrame
    df = pd.DataFrame(data, columns=['StartTime', 'EndTime', 'DriveMeter', 'WaitMeter', 'Fare'])
    try:
        if os.path.exists('rides.csv'):
            df.to_csv('rides.csv', mode='a', header=False, index=False)
        else:
            df.to_csv(filename, index=False)
    except:
        os.system('cls')
        print(txt_error_saving_data)
        print(txt_press_enter)
        input()

# Login
def login():
    global currentUser
    username = input(f'{txt_enter_username} ')
    currentUser = username
    password = getpass.getpass(f'{txt_enter_password} ')
    return authenticate_user(username, password)

def logo_display():
    os.system('cls')
    print(f'{txt_logo_1}')
    print(f'{txt_logo_2}')
    print(f'{txt_logo_3}')
    print(f'{txt_logo_4}')
    print(f'{txt_logo_5}')
    print(f'{txt_logo_6}')
    print(f'{txt_logo_7}')

#Exits the program          
def exit_program():
  print(f'\n\n\t{txt_quit}\n\n')
  time.sleep(3)
  quit()

