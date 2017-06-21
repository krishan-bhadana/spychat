import shelve
current_user                                 #variable which tells which user logged in
print ("Hello, let's get started.")

db=shelve.open('db.shlf')
d={'username':'krishan','password':'bhadana'}
db['0']=d
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
        db[str(db.__len__())]={'username':username,'password':password}
        print 'account created'
        flag=1


if existing_user.upper()=='Y':
    login()
else:
    signup()