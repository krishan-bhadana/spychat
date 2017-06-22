import shelve

messages=shelve.open('messages.shlf')
print messages.__len__()
for i in messages:
    print i