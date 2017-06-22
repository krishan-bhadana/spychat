import shelve

from datetime import datetime

current_user=None

db=shelve.open('database.shlf')
messages=shelve.open('messages.shlf')

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

def signup():

    global current_user

    age = raw_input('Enter your age:  ')
    age=int(age)
    if age<18:
        print 'Your age is not appropriate for being a spy'
        return
    elif age>50:
        print 'Your age is not appropriate for being a spy'
        return

    flag=0                                                       #flag sets when the account is succesfully created and stops the loop for re-entering a username

    while(flag==0):
        temp=None
        username=raw_input('Select a username: ')
        i = 0                                                       #to search the shelve with index from 0 to number of users
        while i<db.__len__():
            temp=db[str(i)]['username']
            if temp==username:
                print 'Username already exists, please try again'
                break
            i=int(i)+1
        if temp == username:
            continue
        password=raw_input('Create password: ')
        rating=raw_input('Enter your rating: ')
        status=raw_input('Status :')
        db[str(db.__len__())]={'username':username,'password':password,'age':age,'rating':rating,'status_messages':[status],'current_status':0}
        messages[str(messages.__len__())]={'chats':[0],'from':[0],'to':[0]}
        print 'account created'
        current_user=db.__len__()-1
        flag=1

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
        print '\n'+str(n)+' '+db[str(i)]['username']
        i=i+1
    send_to = raw_input('Select the user you want to send message from above: ')
    return send_to

def read_message():
    i=0
    while i<messages.__len__():
        if messages[str(i)]['to']==str(current_user):
            print 'Message from '+db[messages[str(i)]['from']]['username']+' :'+messages[str(i)]['text']
        i=i+1
def send_message():

    send_to=select_friend()
    original_image = 'bolt.jpg'
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    messages[str(current_user)]['chats'].append(text)
    messages[str(current_user)]['from'].append(current_user)
    messages[str(current_user)]['to'].append(send_to)
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
                messages[str(current_user)]['chats'][:]=[]
                messages[str(current_user)]['from'][:]=[]
                messages[str(current_user)]['to'][:]=[]

print ("Hello, let's get started.")
#db.clear()   #to clear the shelve file(not included in program)
#del db

while 1<2:
    existing_user = raw_input("1. Login\n2. Signup\n3. Stop application")
    if existing_user=='1':
        back=login()
        if back==True:
            continue
        start_chat()

    elif existing_user=='2':
        signup()
        start_chat()

    else:
        break
