import shelve

db=shelve.open('database.shlf')

class disp_user_class:

    def disp_users(self):
        i = 0
        while i < db.__len__():
            n = i + 1
            print '\n\t\t(' + str(n) + ') Username: ' + db[str(i)]['username']+'\n\t\t    Rating: '+db[str(i)]['rating']+'\n\t\t    Status: ' +db[str(i)]['status_messages'][int(db[str(i)]['current_status'])]+ '\n'
            i = i + 1
        print '\n'
