import shelve
from signup import signupclass
from login import loginclass
from disp_users import disp_users_class
from send_message import send_message_class
from read_message import read_message_class
from datetime import datetime

ms=shelve.open('messages.shlf')
db=shelve.open('database.shlf')

current_user=None

def select_status():
    global current_user

    choice=raw_input('Choose from previous status? (Y/N)')

    if choice.upper()=='N':
        status = raw_input('Status :')
        db[str(current_user)]['status_messages'].append(status)
        db[str(current_user)]['current_status']=len(db[str(current_user)]['status_messages'])-1

    if choice.upper() == 'Y':
        i=0
        while i<len(db[str(current_user)]['status_messages']):
            n=i+1
            print(str(n)+' '+db[str(current_user)]['status_messages'][i])
            i=i+1
        input=raw_input('Select from above status')
        db[str(current_user)]['current_status']=int(input)-1

def start_chat():

    showmenu=True

    while showmenu==True:

        menu_choices = "\nWhat do you want to do? \n 1. Set status update  \n 2. Send a secret message \n 3. Read a secret message \n 4. Read Chats from a user \n 5. Logout \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                select_status()
            elif menu_choice == 2:
                x=send_message_class()
                x.send_message(current_user)
            elif menu_choice == 3:
                x=read_message_class()
                x.read_message(current_user)
            elif menu_choice == 4:
                read_chat_history()
            else:
                showmenu = False
                #alist[:] = []

print ("Hello, let's get started.")   #the program control starts here
#db.clear()   #to clear the shelve file(not included in program)
#del
i=0
while i<ms.__len__():
    print ms[str(i)]['message']+'\n here'

while 1<2:

    existing_user = raw_input("1. Login\n2. Signup\n3. Display all users\n4. Stop application")
    if existing_user=='1':
        x=loginclass()
        back=x.login(current_user)
        if back==None:
            continue
        else:
            current_user=back
            start_chat()

    elif existing_user=='2':
        x=signupclass()
        current_user=x.signup(current_user)
        start_chat()

    elif existing_user=='3':
        x=disp_users_class()
        x.disp_users()

    elif existing_user=='4':
        #messages['chats'][:] = []
        #messages['from'][:] = []
        #messages['to'][:] = []
        db.close()
        break