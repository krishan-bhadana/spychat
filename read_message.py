import shelve

ms=shelve.open('messages.shlf')

class read_message_class:

    def read_message(self,current_user):

        i=0
        while i<int(ms.__len__()):
            if str(ms[str(i)]['to'])==str(current_user):
                print 'Message from '+db[str(ms[str(i)]['from'])]['username']+' :'+ms[str(i)]['message']
            else:
                print 'no message'
            i=i+1