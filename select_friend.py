import shelve
db=shelve.open('database.shlf')

class select_friend_class:

    def select_friend(self):

        i = 0
        while i < db.__len__():
            n = i + 1
            print str(n) + ' ' + db[str(i)]['username']
            i = i + 1
        send_to = raw_input('Select the user you want to send message from above: ')
        return int(send_to) - 1
