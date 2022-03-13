def contacts():
    try:
        print('Welcome!')
        print('|---1: Find your friend                 ---|')
        print('|---2: Add a new friend                 ---|')
        print('|---3: Delete a person                  ---|')
        print('|---4: Show all people\'s phone numbers  ---|')
        print('|---5: Exit                             ---|')
        temp = input('What can I do for you: ')
        addressBook = {} 
        while 1:
            search = int(temp) # make sure the input is a number. If the value of the input is not a number, except will catch the error.
            if search < 1 or search > 5:# If the number of the input is not between 1 and 5, the input is invalid.
                print('invalid input, try again!')
            else:
                if search == 1:# find a person
                    name = input('Please input the name: ')
                    if name in addressBook:
                        print(addressBook[name])
                    else:
                        print('No result, please try again!')
                elif search == 2: # add a new person and his phone number, or edit the information of an existed person.
                    newFriend = input('please input the name of your friend: ')
                    if newFriend in addressBook:# Whether or not the person is already in the address book
                        change = input('Already exist, do you want to edit it? Edit(y)/Exit(n): ')
                        if change == 'y':
                            newNumber = input('Please input the new number: ')
                            addressBook.update({newFriend:newNumber})
                            print(newFriend, newNumber)
                        elif change == 'n':
                            pass
                        else:
                            print('invalid input!')
                            pass
                    else:
                        newNumber = input('please input the phone number: ')
                        addressBook.update({newFriend:newNumber})
                        print(newFriend, ' : ', addressBook[newFriend])
                elif search == 3:#Delete a person
                    delContacts = input('Please input the name: ')
                    if delContacts in addressBook:
                        del addressBook[delContacts]
                        print('Deleted')
                    else:
                        print('This person is not in your address book!')
                elif search == 4:#show the whole address book
                    bookList = list(addressBook)
                    if len(bookList) == 0:# check whether or not the address book is empty
                        print("You haven\'t added any person yet!")
                    else:
                        for each in bookList:
                            personNumber = addressBook[each]
                            print(each, ' : ', personNumber)
                else:
                    break
            nextRound = input('Keep Using? Yes(y)/No(n): ')
            if nextRound == 'y':
                temp = input('What Can I do for you: ')
            elif nextRound == 'n':
                break
            else:
                print('Invalid input!')
                break
        return 'Thank you for using, have a nice day!'
    except(ValueError):
        return 'Invalid input, exit your personal account!'



def loginSystem():
    try:
        print('|--- Register an account(N/n)  ---|')
        print('|--- Log in(E/e)               ---|')
        print('|--- Close the program(Q/q)    ---|')
        system = {}
        while 1:
            order = input('Can I help you?: ')
            if order == 'N' or order == 'n':# register an account
                username = input('Please input the username: ')
                password = input('Please input the password: ')
                system.update({username:password})
                print('Your account has been registered.')
            elif order == 'E' or order == 'e': # log in
                username = input('Please input your username: ')
                i = 3
                while i > 0:# user has 3 times
                    if username not in system:#whether or not the account has been registered
                        i -= 1
                        print('This username has not been registered, you still can try ' + str(i) +' times.')
                        username = input('Please input your username: ')
                    else:
                        password = input('Please input your password: ')
                        systemRecord = system[username]
                        if password == systemRecord:# check the password
                            print(contacts())
                            break
                        else:
                            i -= 1
                            print('Your password is not correct, you still can try ' + str(i) +' times.')
                            username = input('Please input your username: ')
            elif order == 'Q' or order == 'q':# exit the program
                leave = input('Do you want to close the program? y(yes)/n(no): ')
                if leave == 'y':
                    break
                elif leave == 'n':
                    pass
                else:
                    print('Invalid input!')
                    break
            else:
                print('Invalid input')
        return 'Good Bye!'
    except(ValueError):
        return 'Invalid input, Bye~'

print(loginSystem())
                    
        
    
                
                            
                    
            
                    
                        
                    
                    
                
            
            
        
