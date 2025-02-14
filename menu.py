# Menu() Class
import time
import os
import sys
from ClassRide import *
from ClassTimer import *
from texts import *
from definitions import *


def menu_display(menu,currentRide, Rides, waitfee, drivefee):
        os.system('cls')
        print('\n')
        print(f'{txt_logo_1}')
        print(f'{txt_logo_2}')
        print(f'{txt_logo_3}')
        print(f'{txt_logo_4}')
        print(f'{txt_logo_5}')
        print(f'{txt_logo_6}')
        print(f'{txt_logo_7}')

        if menu == 'welcome':
            print(f'{txt_welcome}')
            print(f'{txt_press_enter}')
            input()
            return
        elif menu == 'home':
                  display_fees(waitfee, drivefee)
                  #if Rides != []:
                  #       display_last_rides(Rides)
                  print(f'{txt_options}')
                  option = input(f'{txt_menu_home}').upper()
                  return option
        elif menu == 'wait':
                    display_fees(waitfee, drivefee)
                    display_drive(currentRide)
                    print(f'{txt_options}')
                    option = input(f'{txt_msg_wait}').upper()
                    return option
        elif menu == 'drive':
                     display_fees(waitfee, drivefee)
                     display_drive(currentRide)
                     print(f'{txt_options}')
                     option = input(f'{txt_msg_drive}').upper()
                     return option
        elif menu == 'setup':
                     display_fees(waitfee, drivefee)
                     print(f'{txt_options}')
                     option = input(f'{txt_msg_setup}').upper()
                     return option

        elif menu == 'end':
                     display_fees(waitfee, drivefee)
                     display_drive(currentRide)
                     print(f'{txt_end} {currentRide.Fare} ')
                     print(f'{txt_press_enter}')
                     input()
                     return
        elif menu == 'wrong':
                   print(f'{txt_wrong_input}')
                   time.sleep(2)

