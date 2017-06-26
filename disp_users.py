import shelve
db=shelve.open('database.shlf')

class disp_users_class:

    def disp_users(self):

        i=0
        while i<db.__len__():
            n=i+1
            print '\n\t\t'+str(n)+' '+db[str(i)]['username']+'\n'
            i=i+1
        print '\n'
