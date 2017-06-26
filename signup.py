import shelve
db = shelve.open('database.shlf')
class signupclass:


    def signup(self,current_user):

        age = raw_input('Enter your age:  ')
        age = int(age)
        if age < 18:
            print 'Your age is not appropriate for being a spy'
            return current_user
        elif age > 50:
            print 'Your age is not appropriate for being a spy'
            return current_user

        flag = 0  # flag sets when the account is succesfully created and stops the loop for re-entering a username

        while (flag == 0):
            temp = None
            username = raw_input('Select a username: ')
            i = 0  # to search the shelve with index from 0 to number of users
            while i < db.__len__():
                temp = db[str(i)]['username']
                if temp == username:
                    print 'Username already exists, please try again'
                    break
                i = int(i) + 1
            if temp == username:
                continue
            password = raw_input('Create password: ')
            rating = raw_input('Enter your rating: ')
            status = raw_input('Status :')
            db[str(db.__len__())] = {'username': username, 'password': password, 'age': age, 'rating': rating,
                                     'status_messages': [status], 'current_status': 0}
            print 'account created'
            current_user = int(db.__len__()) - 1
            return current_user
            flag = 1
