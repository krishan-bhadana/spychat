import shelve
from signup import signupclass

from datetime import datetime

messages={'chats':[None]*100,'from':[None]*100,'to':[None]*100}

current_user=None
total_chat=0

db=shelve.open('database.shlf')

def login():
    global current_user
    flag = 0
    while flag == 0:
        username = raw_input('\nUsername: ')
        i = 0  # to search the shelve with index from 0 to number of users
        while i < db.__len__():
            if db[str(i)]['username'] == username:
                password = raw_input('Password: ')
                if db[str(i)]['password'] == password:
                    print 'Yor are logged in ' + db[str(i)]['username']+'\n'
                    flag = 1
                    current_user=i
                    break
                else:
                    print 'Try again'
                    continue
            i = i + 1
        if flag==0:
            print 'Try again'
            return True


def disp_users():
    i=0
    while i<db.__len__():
        n=i+1
        print '\n\t\t'+str(n)+' '+db[str(i)]['username']+'\n'
        i=i+1
    print '\n'

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

def select_friend():

    i=0
    while i<db.__len__():
        n=i+1
        print str(n)+' '+db[str(i)]['username']
        i=i+1
    send_to = raw_input('Select the user you want to send message from above: ')
    return int(send_to)-1

def read_message():
    global total_chat
    global messages
    i=0
    while i<int(total_chat):
        if str(messages['to'][i])==str(current_user):
            print 'Message from '+db[str(messages['from'][i])]['username']+' :'+messages['text'][i]
        i=i+1

def send_message():
    global messages
    global total_chat
    send_to=select_friend()
    text = raw_input("What do you want to say? ")
    messages['chats'][total_chat]=text
    messages['from'][total_chat]=current_user
    messages['to'][total_chat]=send_to
    total_chat=total_chat+1
    print 'Message sent'

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
                send_message()
            elif menu_choice == 3:
                read_message()
            elif menu_choice == 4:
                read_chat_history()
            else:
                showmenu = False
                #alist[:] = []

print ("Hello, let's get started.")
#db.clear()   #to clear the shelve file(not included in program)
#del db

while 1<2:
    existing_user = raw_input("1. Login\n2. Signup\n3. Display all users\n4. Stop application")
    if existing_user=='1':
        back=login()
        if back==True:
            continue
        start_chat()

    elif existing_user=='2':
        x=signupclass()
        current_user=x.signup(current_user)
        start_chat()

    elif existing_user=='3':
        disp_users()

    elif existing_user=='4':
        #messages['chats'][:] = []
        #messages['from'][:] = []
        #messages['to'][:] = []
        db.close()
        break