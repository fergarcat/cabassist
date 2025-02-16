# Menu() Class
import time
import os
from ClassRide import *
from ClassTimer import *
from texts import *
from definitions import *
from auth import *
import user_session as us




def menu_display(menu):
        global currentUser
        logo_display()

        if menu == 'welcome':
            i = 0
            while i < 3:  # Permitir hasta 3 intentos
                if login():
                    os.system('cls')
                    logo_display()
                    print(f'{txt_welcome}')
                    print(f'{txt_press_enter}')
                    input()
                    return  # Sale de la función si el login es exitoso
                else:
                    i += 1
                    os.system('cls')
                    logo_display()
                    print(f'{txt_login_incorrect} {3 - i} attempts left')
            print(f'{txt_acces_denied}')  # Si se agotan los intentos
            exit_program()


        elif menu == 'home':
                  print(f'{txt_login}{us.currentUser}\n')
                  display_fees()
                  print(f'{txt_options}')
                  if us.currentUser   == 'admin':
                        option = input(f'{txt_new_ride}{txt_list_rides}{txt_setup_fees}{txt_menu_users}{txt_to_quit}').upper()
                        return option
                  elif us.currentUser != 'admin':
                        option = input(f'{txt_new_ride}{txt_list_rides}{txt_setup_fees}{txt_to_quit}').upper()
                        return option
        elif menu == 'wait':
                    display_fees()
                    display_drive()
                    print(f'{txt_options}')
                    option = input(f'{txt_msg_wait}').upper()
                    return option
        elif menu == 'drive':
                     display_fees()
                     display_drive()
                     print(f'{txt_options}')
                     option = input(f'{txt_msg_drive}').upper()
                     return option
        elif menu == 'users':
                        option = input(f'{txt_users_options}').upper()
                        return option
        elif menu == 'list':
                        if get_last_rides():
                            print(f'{txt_press_enter}')
                            input()
                        else:
                            print(f'{txt_error_reading_data}')
                            print(f'{txt_press_enter}')
                            input()
        elif menu == 'setup':
                     display_fees()
                     print(f'{txt_options}')
                     option = input(f'{txt_msg_setup}').upper()
                     return option
        elif menu == 'end':
                     display_fees()
                     display_drive()
                     print(f'{txt_end} {us.currentRide.Fare} ')
                     print(f'{txt_press_enter}')
                     input()
                     return
        elif menu == 'wrong':
                   print(f'{txt_wrong_input}')
                   time.sleep(2)

