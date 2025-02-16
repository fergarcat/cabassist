# Menu() Class
import time
import os
from ClassRide import *
from ClassTimer import *
from texts import *
from definitions import *
from auth import *




def menu_display(menu,currentRide, Rides, waitfee, drivefee, file):
        logo_display()
        print('\n')

        if menu == 'welcome':
            i = 0
            while i < 3:  # Permitir hasta 3 intentos
                if login():
                    print(f'{txt_welcome}')
                    print(f'{txt_press_enter}')
                    input()
                    return  # Sale de la función si el login es exitoso
                else:
                    i += 1
                    os.system('cls')
                    print('\n')
                    logo_display()
                    print(f'{txt_login_incorrect} {3 - i} attempts left')
            print(f'{txt_acces_denied}')  # Si se agotan los intentos
            exit_program()


        elif menu == 'home':
                  display_fees(waitfee, drivefee)
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
        elif menu == 'list':
                        display_last_rides(file)
                        print(f'{txt_press_enter}')
                        input()
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

