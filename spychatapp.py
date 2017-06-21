import shelve

db=shelve.open('db.shlf')

def login():
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

def signup():
    #global total_no_of_users                                   #the variable for total number of users
    flag=0                                                       #flag sets when the account is succesfully created and stops the loop for re-entering a username

    while(flag==0):
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
        db[str(db.__len__())]={'username':username,'password':password}
        #total_no_of_users = int(total_no_of_users) + 1
        print 'account created'
        flag=1

print ("Hello, let's get started.")

existing_user=raw_input("Are you a existing user ? (Y/N)")

if existing_user.upper()=='Y':
    login()

else:
    signup()