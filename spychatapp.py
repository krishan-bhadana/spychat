import shelve
from termcolor import colored
from datetime import datetime

db=shelve.open('database.shlf')
ms=shelve.open('chat.shlf')

short_forms=[{'short':'brb','full':'be right back'},
             {'short':'ty','full':'thankyou'},
             {'short':'gtg','full':'got to go'},
             {'short':'rn','full':'right now'},
             {'short':'af','full':'as fuck'},
             {'short':'wtf','full':'what the fuck'},
             {'short':'wyd','full':'what you doing'}]


def login():

    flag = 0
    while flag == 0:
        username = raw_input('\nUsername: ')
        i = 0  # to search the shelve with index from 0 to number of users
        while i < db.__len__():
            if db[str(i)]['username'] == username:
                password = raw_input('Password: ')
                if db[str(i)]['password'] == password:
                    print 'Yor are logged in as ' + db[str(i)]['username']+'\n'
                    flag = 1
                    current_user=int(i)
                    return current_user
                    break
                else:
                    print 'Try again'
                    continue
            i = i + 1
        if flag==0:
            print 'Try again'
            return 99


def signup():

    age = raw_input('Enter your age:  ')
    age=int(age)
    if age<18:
        print 'Your age is not appropriate for being a spy'
        return
    elif age>50:
        print 'Your age is not appropriate for being a spy'
        return

    flag=0                                                       # flag sets when the account is succesfully created and stops the loop for re-entering a username

    while(flag==0):
        temp=None
        username=raw_input('Select a username: ')
        i = 0                                                       # to search the shelve with index from 0 to number of users
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
        print '\naccount created\n'
        flag=1
        db.close()


def disp_users():
    i=0
    while i<db.__len__():
        n=i+1
        print '\n\t\t('+str(n)+') Usrname: '+db[str(i)]['username']+'\n\t\t    Age: '+str(db[str(i)]['age'])+'\n\t\t    Rating: '+str(db[str(i)]['rating'])+'\n\t\t    Status: '+db[str(i)]['status_messages']
        i=i+1
    print '\n'


def select_friend():

    i=0
    while i<db.__len__():
        n=i+1
        print str(n)+' '+db[str(i)]['username']
        i=i+1
    send_to = raw_input('Select the user you want to send message from above: ')
    return int(send_to)-1


def chat_history(current_user):

    disp_users()
    choice=raw_input('Open chat history of?')
    choice=int(choice)-1
    i = 0
    while i < ms.__len__():
        if str(ms[str(i)]['to']) == str(current_user):
            if str(ms[str(i)]['from']) == str(choice):
                if len(ms[str(i)]['message'])==0:
                    print '\t\t\t('+colored(colored(ms[str(i)]['time'],"green"))+') '+'"It is a empty message"'
                else:
                    print '\t\t\t('+colored(colored(ms[str(i)]['time'],"green"))+') '+colored(ms[str(i)]['message'],"blue")
        elif str(ms[str(i)]['from']) == str(current_user):
            if str(ms[str(i)]['to']) == str(choice):
                if len(ms[str(i)]['message'])==0:
                    print '\t\t\t\t\t\t\t\t\t\t\t('+colored(colored(ms[str(i)]['time'],"green"))+') '+'"It is a empty message"'
                    print '\t\t\t\t\t\t\t\t\t\t\t('+colored(colored(ms[str(i)]['time'],"green"))+') '+colored(ms[str(i)]['message'],"red")
        i = i + 1


def read_message(current_user):
    i=0
    while i<ms.__len__():
        if str(ms[str(i)]['to'])==str(current_user):
            if len(ms[str(i)]['message'])==0:
                print 'Message from ('+colored(db[str(ms[str(i)]['from'])]['username'],"red")+'): '+colored(colored(ms[str(i)]['time'],"green"))+'\t'+colored('"It is a empty message"','blue')
            else:
                print 'Message from ('+colored(db[str(ms[str(i)]['from'])]['username'],"red")+'): '+colored(colored(ms[str(i)]['time'],"green"))+'\t'+colored(ms[str(i)]['message'],"blue")
        i=i+1


def send_message(current_user):
    send_to=select_friend()
    text = raw_input("Message: ")
    var = datetime.now()
    ms[str(ms.__len__())]={'message':text,'from':current_user,'to':send_to,'time':var}
    choice=raw_input('Message sent, Send again? (Y/N)')
    while choice.upper()=='Y':
        text = raw_input("Message: ")
        var=datetime.now()
        ms[str(ms.__len__())] = {'message': text, 'from': current_user, 'to': send_to,'time':var}
        choice = raw_input('Message sent, Send again? (Y/N)')


def start_chat(current_user):

    showmenu=True

    while showmenu==True:

        menu_choices = "\nWhat do you want to do?  \n 1. Send a secret message \n 2. Inbox  \n 3. Chat history\n 4. Logout \n"
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)
        if menu_choice == 1:
            send_message(current_user)
        elif menu_choice == 2:
            read_message(current_user)
        elif menu_choice==3:
            chat_history(current_user)
        else:
            showmenu = False

print ("Hello, let's get started.")
#db.clear()   #to clear the shelve file(not included in program)
#db.close()
#del db

while 1<2:
    existing_user = raw_input("1. Login\n2. Signup\n3. Display all users\n4. Stop application")
    if existing_user=='1':
        current_user=login()
        if current_user==99:
            continue
        start_chat(current_user)

    elif existing_user=='2':
        signup()
        db = shelve.open('database.shlf')

    elif existing_user=='3':
        disp_users()

    elif existing_user=='4':
        db.close()
        ms.clear()
        ms.close()
        break