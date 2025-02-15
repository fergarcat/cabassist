from texts import *
import time
import os
import pandas as pd

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