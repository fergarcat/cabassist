from texts import *
import time
import os
import pandas as pd
from auth import authenticate_user
import getpass
import user_session as us

#Displays last 3 rides
def get_last_rides():
    Rides = []
    try:
        df = pd.read_csv(us.filename)
    except:
        return False
    if not df.empty:
        df = df.sort_index(ascending=False)
        print(f'{txt_last_drives}')
        print(f'{df}')
        return True

#Displays current drive data
def display_drive():
    print(f'{txt_ride_start} {formatTime(us.currentRide.startTime)}\n{txt_current_time} {formatTime(time.time())}\n{txt_run_length} {round(us.currentRide.driveMeter,2)} {txt_sec}\n{txt_wait_length} {round(us.currentRide.waitMeter,2)} {txt_sec}\n')

#Calculates total fare
def total_fare():
          return(round((us.currentRide.driveMeter * us.drivefee) + (us.currentRide.waitMeter * us.waitfee),2))

#Displays fees
def display_fees():
    print(f'{txt_current_drive_fee:} {us.drivefee}\t{txt_current_wait_fee:} {us.waitfee}\n')

# Def formatTime. Convert float time values to HH:MM:SS format
def formatTime(t):
  struct_time = time.localtime(t)
  formatted_time = time.strftime("%H:%M:%S", struct_time)
  return(formatted_time)

#Save ride data to file
def save_data():
    # Create a DataFrame
    data = []
    data.append([formatTime(us.currentRide.startTime), formatTime(us.currentRide.endTime), us.currentRide.driveMeter, us.currentRide.waitMeter, us.currentRide.Fare])
    # Convert list to DataFrame
    df = pd.DataFrame(data, columns=['StartTime', 'EndTime', 'DriveMeter', 'WaitMeter', 'Fare'])
    try:
        if os.path.exists('rides.csv'):
            df.to_csv('rides.csv', mode='a', header=False, index=False)
        else:
            df.to_csv(us.filename, index=False)
    except:
        os.system('cls')
        print(txt_error_saving_data)
        print(txt_press_enter)
        input()

# Login
def login():
    global currentUser
    username = input(f'{txt_enter_username} ')
    password = getpass.getpass(f'{txt_enter_password} ')
    if authenticate_user(username, password):
        us.currentUser = username
        return True
    else:
        return False

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

