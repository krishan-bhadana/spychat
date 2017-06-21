import shelve

current_user=None

db=shelve.open('db.shlf')

def login():
    global current_user
    flag = 0
    while flag == 0:
        username = raw_input('Username: ')
        i = 0  # to search the shelve with index from 0 to number of users
        while i < db.__len__():
            if db[str(i)]['username'] == username:
                password = raw_input('Password: ')
                if db[str(i)]['password'] == password:
                    print 'Yor are logged in ' + db[str(i)]['username']
                    flag = 1
                    current_user=i
                    break
                else:
                    print 'Try again'
                    continue
            i = i + 1
        if flag==0:
            print 'Try again'

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
        print 'account created'
        current_user=db.__len__()-1
        flag=1

def select_status():
    global current_user
    i=str(current_user)
    choice=raw_input('Choose from previous status? (Y/N)')

    if choice.upper()=='N':
        status = raw_input('Status :')
        #current_user=str(current_user)
        #db[str(current_user)]['status_messages'].append(status)
        #db[str(current_user)]['current_status']=len(db[str(current_user)]['status_messages'])-1
        #n=db[str(current_user)]['current_status']
        #print len(db[str(current_user)]['status_messages'])
        #print len(db[str(current_user)]['status_messages'])


def start_chat():

    showmenu=True

    while showmenu==True:

        menu_choices = "What do you want to do? \n 1. Set status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                select_status()
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif menu_choice == 3:
                send_message()
            elif menu_choice == 4:
                read_message()
            elif menu_choice == 5:
                read_chat_history()
            else:
                showmenu = False

print ("Hello, let's get started.")

existing_user=raw_input("Are you a existing user ? (Y/N)")

if existing_user.upper()=='Y':
    #print db[str(db.__len__()-1)]['status_messages'][0]               #to print the status message
    login()
    start_chat()

else:
    signup()
    start_chat()