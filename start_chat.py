from send_message import send_message_class
from read_message import read_message_class

class start_chat_class:

    def start_chat(self,current_user):

        showmenu = True

        while showmenu == True:

            menu_choices = "\nWhat do you want to do? \n 1. Set status update  \n 2. Send a secret message \n 3. Read a secret message \n 4. Read Chats from a user \n 5. Logout \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    select_status()
                elif menu_choice == 2:
                    x = send_message_class()
                    x.send_message(current_user)
                elif menu_choice == 3:
                    x = read_message_class()
                    x.read_message(current_user)
                elif menu_choice == 4:
                    read_chat_history()
                else:
                    showmenu = False
                    # alist[:] = []
