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

def signup():

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
        flag=1

print ("Hello, let's get started.")

existing_user=raw_input("Are you a existing user ? (Y/N)")

if existing_user.upper()=='Y':
    n=db.__len__()-1                                        #because index is 1 less than length
    print db[str(n)]['status_messages'][0]
    login()
    print current_user

else:
    signup()