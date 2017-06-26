import shelve
db=shelve.open('database.shlf')
class loginclass:
    def login(self,current_user):
        flag = 0
        while flag == 0:
            username = raw_input('\nUsername: ')
            i = 0  # to search the shelve with index from 0 to number of users
            while i < db.__len__():
                if db[str(i)]['username'] == username:
                    password = raw_input('Password: ')
                    if db[str(i)]['password'] == password:
                        print 'Yor are logged in ' + db[str(i)]['username'] + '\n'
                        flag = 1
                        current_user = i
                        return current_user
                        break
                    else:
                        print 'Try again'
                        continue
                i = i + 1
            if flag == 0:
                print 'Try again'
                return None