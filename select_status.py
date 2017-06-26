def select_status():
    global current_user

    choice=raw_input('Choose from previous status? (Y/N)')

    if choice.upper()=='N':
        status = raw_input('Status :')
        db[str(current_user)]['status_messages'].append(status)
        db[str(current_user)]['current_status']=len(db[str(current_user)]['status_messages'])-1

    if choice.upper() == 'Y':
        i=0
        while i<len(db[str(current_user)]['status_messages']):
            n=i+1
            print(str(n)+' '+db[str(current_user)]['status_messages'][i])
            i=i+1
        input=raw_input('Select from above status')
        db[str(current_user)]['current_status']=int(input)-1

