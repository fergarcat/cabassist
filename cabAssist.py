import time
import sys
from ClassRide import *
from ClassTimer import *
from texts import *
from menu import menu_display
from definitions import *
import user_session as us    
import auth
import getpass
us.initialize_session()


#Main function
def main():
    menu_welcome()

#Displays home menu
def menu_home():
    while True:
        option = menu_display('home')
        if option == "R":
            us.currentRide.reset(us.waitfee, us.drivefee)
            us.waitTimer.restart()
            us.driveTimer.restart()
            menu_wait()
        elif option == "S":
            menu_setup()
        elif option == "L":
            menu_list()
        elif option == "U" and us.currentUser == 'admin':
            menu_users()
        elif option == "Q":
            exit_program()
        else:
            menu_display('wrong')
            continue

# Displays waiting menu
def menu_wait():
    us.waitTimer.restart()
    while True:
        option = menu_display('wait')
        if option == "D":
            us.currentRide.waitMeter += us.waitTimer.get_time()
            menu_drive()
            break
        elif option == "E":
            us.currentRide.waitMeter += us.waitTimer.get_time()
            menu_end()
            break
        else:
            menu_display('wrong')
            continue

 #Displays driving menu
def menu_drive():
    us.driveTimer.restart()
    while True:
        option = menu_display('drive')
        if option == "S":
            us.currentRide.driveMeter += us.driveTimer.get_time()
            menu_wait()
            break
        else:
            menu_display('wrong')
            continue



#Displays end of currentRide message and total fare to pay
def menu_end():
        us.currentRide.Fare = total_fare()
        us.currentRide.endTime = time.time()
        save_data()
        menu_display('end')
        menu_home()

#Displays configuration options
def menu_setup():
    while True:
        option = menu_display('setup')
        if option == "D":
            while True:
                try:
                    us.drivefee = float(input(f'{txt_enter_drive_fee}'))
                    break
                except ValueError:
                    menu_display('wrong')
        elif option == "W":
            while True:
                try:
                    us.waitfee = float(input(f'{txt_enter_wait_fee}'))
                    break
                except ValueError:
                    menu_display('wrong')
        elif option == "M":
            menu_home()
            break
        else:
            menu_display('wrong')
            continue

def menu_users():
    menuKey = None
    menuUser = None
    while True:
        option = menu_display('users')
        if option == "A":         
            menuUser = input(f'{txt_enter_username}')
            menuKey = getpass.getpass(f'{txt_enter_password}')
            menuKey2 = getpass.getpass(f'{txt_confirm_password}')
            if menuKey != menuKey2:
                    menu_display('wrong')
                    continue
            else:
                    try:
                        auth.register_user(menuUser, menuKey)
                    except:
                        menu_display('wrong')
        elif option == "D":
            menuUser = input(f'{txt_enter_username}')
            while True:
                menuConfirm = input(f'{txt_confirm_option}').upper()
                if menuConfirm == "Y":
                    try:
                        auth.delete_user(menuUser)
                        break
                    except:
                        menu_display('wrong')
                elif menuConfirm == "N":
                    break
                else:
                    menu_display('wrong')
            
        elif option == "L":
            auth.list_users()
            input(f'{txt_press_enter}')
        elif option == "M":
            menu_home()
            break
        else:
            menu_display('wrong')
            continue
    

# Shows welcome message
def menu_welcome():
    menu_display('welcome')
    menu_home()

# Shows last rides
def menu_list():
    menu_display('list')
    return   

main()