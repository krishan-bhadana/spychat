import shelve
from signup import signupclass
from login import loginclass
from disp_users import disp_users_class
from start_chat import start_chat_class

ms=shelve.open('messages.shlf')
db=shelve.open('database.shlf')

current_user=None

print ("Hello, let's get started.")   #the program control starts here
while 1<2:

    existing_user = raw_input("1. Login\n2. Signup\n3. Display all users\n4. Stop application")
    if existing_user=='1':
        x=loginclass()
        back=x.login(current_user)
        if back==None:
            continue
        else:
            current_user=back
            x=start_chat_class()
            x.start_chat(current_user)

    elif existing_user=='2':
        x=signupclass()
        current_user=x.signup(current_user)
        x = start_chat_class()
        x.start_chat(current_user)

    elif existing_user=='3':
        x=disp_users_class()
        x.disp_users()

    elif existing_user=='4':
        db.close()
        break