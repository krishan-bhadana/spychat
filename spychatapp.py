import shelve
current_user=0                                #variable which tells which user logged in
print ("Hello, let's get started.")
db=shelve.open('db.shlf')
existing_user=raw_input("Are you a existing user ? (Y/N)")

def login():
    flag=0
    while flag==0:
        username = raw_input('Username: ')
        i = 0                                                        # to search the shelve with index from 0 to number of users
        while i < db.__len__():
            if db[str(i)]['username']== username:
                password = raw_input('Password: ')
                if db[str(i)]['password']==password:
                    print 'Yor are logged in '+db[str(i)]['username']
                    flag=1
                    break
            i=i+1
def signup():
    flag=0                                                       #flag sets when the account is succesfully created and stops the loop for re-entering a username

    while(flag==0):
        username=raw_input('Select a username: ')
        i = 0                                                       #to search the shelve with index from 0 to number of users
        while i<db.__len__():
            if db[str(i)]['username']==username:
                print 'Username already exists, please try again'
                break
            i=i+1
        if db[str(i)]['username'] == username:
            continue
        password=raw_input('Create password: ')
        #age=raw_input('Enter your age:  ')
        #rating=raw_input('Enter your rating: ')
        #status=raw_input('Status :')
        #db[str(db.__len__())]={'username':username,'password':password,'age':age,'rating':rating,'status_messages':status_messages[status],'current_status':0}
        print 'account created'
        flag=1

#def start_chat():
   # print 'here starts the new chat'

if existing_user.upper()=='Y':
    login()
    #start_chat()
else:
    signup()
    #start_chat()