import shelve
from select_friend import select_friend_class

ms=shelve.open('messages.shlf')
db=shelve.open('database.shlf')

class send_message_class:
    def send_message(self,current_user):
        x=select_friend_class()
        send_to = x.select_friend()
        text = raw_input("What do you want to say? ")
        ms[str(ms.__len__())]={'message':text,'from':current_user,'to':send_to}
        print 'Message sent to '+db[str(send_to)]['username']