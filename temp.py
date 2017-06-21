import shelvde
print ("Hello, let's get started.")
file=shelve.open('db.shlf')
name=raw_input('input username')
pass=raw_input('input password')
file[name]=name
total_no_of_users=file.__len__()
print total_no_of_users
existing_user=raw_input("Are you