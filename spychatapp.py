import shelve

print ("Hello, let's get started.")

db=shelve.open('db.shlf')
d={'username':'krishan','password':'bhadana'}
db['0']=d
total_no_of_users=db.__len__()
existing_user=raw_input("Are you a existing user ? (Y/N)")

def login():
    username = raw_input('Username: ')
    password = raw_input('Password: ')

def signup():
    global total_no_of_users                                   #the variable for total number of users
    flag=0                                                       #flag sets when the account is succesfully created and stops the loop for re-entering a username

    while(flag==0):
        username=raw_input('Select a username: ')
        i = 0                                                       #to search the shelve with index from 0 to number of users
        while i<int(total_no_of_users):
            temp=db[str(i)]['username']
            if temp==username:
                print 'Username already exists, please try again'
                break
            i=int(i)+1
        if temp == username:
            continue
        password=raw_input('Create password: ')
        db[str(total_no_of_users)]={'username':username,'password':password}
        total_no_of_users = int(total_no_of_users) + 1
        print 'account created'
        flag=1


if existing_user.upper()=='Y':
    login()
else:
    signup()