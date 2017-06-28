import shelve

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
        db[str(db.__len__())]={'username':username,'password':password,'age':age,'rating':rating,'status_messages':status}
        print '\naccount created'
        flag=1
        db.close()

def disp_users():
    i=0
    while i<db.__len__():
        n=i+1
        print '\n\t\t('+str(n)+') Usrname: '+db[str(i)]['username']+'\n\t\t    Age: '+str(db[str(i)]['age'])+'\n\t\t    Rating: '+str(db[str(i)]['rating'])+'\n\t\t    Status: '+db[str(i)]['status_messages']
        i=i+1
    print '\n'

def select_status():
    global current_user

    choice=raw_input('\n\t\t\tCurrent status: "'+db[str(current_user)]['status_messages']+'"'+'\n\t\t\tChange status? (Y/N)')

    if choice.upper()=='Y':
        status = raw_input('Enter new Status :')
        db[str(current_user)]['status_messages']=status
        db.close()

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

        menu_choices = "\nWhat do you want to do? \n 1. Set status  \n 2. Send a secret message \n 3. Read a secret message \n 4. Read Chats from a user \n 5. Logout \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                select_status()
                db = shelve.open('database.shlf')
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
#db.close()
#del db

while 1<2:
    existing_user = raw_input("1. Login\n2. Signup\n3. Display all users\n4. Stop application")
    if existing_user=='1':
        back=login()
        if back==True:
            continue
        start_chat()

    elif existing_user=='2':
        signup()
        db = shelve.open('database.shlf')
        start_chat()

    elif existing_user=='3':
        disp_users()

    elif existing_user=='4':
        messages['chats'][:] = []
        messages['from'][:] = []
        messages['to'][:] = []
        db.close()
        break