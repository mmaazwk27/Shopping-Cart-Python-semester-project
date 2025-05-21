
import datetime

process_menu={'organizers':1000,           # process_menu DICTIONARY WITH (PRODUCT NAME) AS [KEY]  AND (PRICES) AS [VALUES]
      'rugs':6000,                         
      'side coffee tables':990,
      'mirror':3900,
      'book selves':10000,
      'flower pots':500,
      'wall art decors':200,
      'TV console':14000,        
      'Hanging swings':16000,
      'bean bags':5000,
      'wall clocks':5000}


menu={'1':'organizers',                  # menu DICTIONARY WITH (SERIAL NUMBER) AS [KEY]  AND (PRODUCT NAME) AS [VALUES]
      '2':'rugs',                        # (FOR USER FRIENDLY OPERATIONS OF SELECTING PRODUCTS IN THE PROGRAM)
      '3':'side coffee tables',          # (* WILL BE LINKED WITH process_menu DECTIONARY FOR PRICE CALCULATIONS *)
      '4':'mirror',
      '5':'book selves',
      '6':'flower pots',
      '7':'wall art decors',
      '8':'TV console',
      '9':'Hanging swings',
      '10':'bean bags',
      '11':'wall clocks'
      }


# FUNCTION TO VIEW PRODUCT LIST
def view_menu(): 
    print('\n\n')
    print("-----Essence Decor Elegance Collection!-----")
    print("____________________________________________")
    counter = 1                                  #ITERATING ON KEY-VALUE PAIRS OF process_menu DICTIONARY
    for product, price in process_menu.items():  # product WILL BE [KEY] OF process_menu DICTIONARY AND price WILL BE ITS [VALUES]
        print(f"{counter:4}. {product:20}: {'':2}RS.{price}")
        counter += 1
    print("____________________________________________")
    print('\n\n')

# FUNCTION TO VIEW CART
def view_cart():
    print('\n\n\n______________________________')
    print ('\n-----Your Cart-----\n')
    for lst in cart:                                              # ITERATING IN cart DICTIONARY:
        print(f'{lst:16} Rs:{process_menu[lst]}  x {cart[lst]}')  # lst = product name        ( [KEY] IN cart DICTIONARY)
    print('______________________________')                       # process_menu[lst] = price ( [KEY] from dictionary)
    print(f'\nTotal bill is Rs: {bill}')                          # cart[lst] = quantity      ( [VALUE] OF lst IN cart DICTIONARY )
    print('______________________________')
    print('______________________________\n')

# FUNCTION TO ADD PRODUCTS TO CART
def add_to_cart():
    global cart # CURRENT cart DICTIONARY 
    while True:
        serial=['1','2','3','4','5','6','7','8','9','10','11']
        items=(input("Enter product number from menu you want to add to cart  or  press 'e' for exit: ")).strip()
        if items=="e" or items=="E":
            break
        if items not in serial and items !=('e' or 'E'):      # CHECKING VALID INPUT
            print('!!! PLEASE ENTER THE VALID OPTION !!!\n')
        elif items in menu.keys():   # CHECKING IF items[INPUT] IS IN [KEYS] OF menu DECTIONARY
            while True:
                quantity=(input('Enter the quantity in digits: ')).strip()
                if not quantity.isdigit():   # CHECK IF INPUT DOES NOT CONTAIN ANY OTHER CHARACTER INSTEAD OF DIGITS
                    print('\nEnter a valid quantity !\n')
                else:
                    q_int=int(quantity)   # CONVERTING THE INPUT INTO INTEGER
                    global bill
                    bill=bill + (process_menu[(menu[items])]*q_int) # ADDING BILL BY QUANTITY[INPUT] X PRICE ([VALUE] OF process_menu DICTIONARY)
                    if menu[items] in cart: # CHECKING PRODUCT[VALUE] OF menu DICTIONARY OF INPUT[KEY] PRESENT IN CART?
                        cart[(menu[items])]+=q_int  # ADDING THE EXISTING QUANTITY ([VALUE] OF INPUT[KEY]) BY INPUT QUANTITY(q_int)
                        print(f'\n->{cart[(menu[items])]} {menu[items]} added to the cart !\n')
                        break
                    else:
                        cart[(menu[items])]=q_int  # OTHERWISE ADD THE PRODUCT[KEY] AND QUANTITY[VALUE] IN THE cart DICTIONARY
                        print (f'\n->{q_int} {menu[items]} added to the cart!\n')
                        break
        
        


# FUNCTION TO REMOVE PRODUCTS FROM CART
def rem_cart():
    global cart
    while True:
        b=input('\nEnter the serial number from menu  of item  you want to remove from cart OR Press "e" to exit.\nSelect ->').strip()
        serial=['1','2','3','4','5','6','7','8','9','10','11']
        if b=="e" or b=="E": 
            break
        if b not in serial and b!=('e' or 'E'):   # CHECKING VALID INPUT
                print('enter valid option')
        elif b in menu.keys():     # CHECKING IF b[INPUT] IS IN [KEYS] OF menu DECTIONARY
            if menu[b] in cart:
                while True:
                    quantity = (input('Enter the quantity in digits: ')).strip()
                    if not quantity.isdigit():  # CHECK IF INPUT DOES NOT CONTAIN ANY OTHER CHARACTER INSTEAD OF DIGITS
                        print('\nEnter a valid Quantity.\n')
                    else:
                        q=int(quantity)   # CONVERTING THE INPUT INTO INTEGER
                        if q <= cart[(menu[b])] and q>0:  #CHECKS THE POSSIBLE INPUT INTEGER
                            cart[(menu[b])] -= q # SUBTRACTING QUANTITY[VALUE] FROM cart DICTIONARY
                            global bill
                            bill -= process_menu[(menu[b])] * q  # SUBTRACTING BILL BY  PRICE ([VALUE] OF process_menu DICTIONARY) X QUANTITY[INPUT]
                            if cart[(menu[b])] == 0:   # CHECK IF QUANTITY[VALUE] OF PRODUCT[KEY] IN cart DICTIONARY IS 0?
                                cart.pop((menu[b]))  # REMOVES THE WHOLE [KEY]-[VALUE] PAIR FROM cart DICTIONARY
                            print(f'\n->{q} {(menu[b])} removed from the cart!\n')
                            break
                        else:
                            print('\n Quantity exceeds the existing number of this product !!')
            elif menu[b] not in cart:  # CHECK IF PRODUCT[VALUE] OF menu DICTIONARY IS NOT IN cart DICTIONARY
                print ('\nItem is not in the cart!')
        


# FUNCTION TO CREATE AN ACCOUNT
def create_account():
    while True:
        while True:
            username = input('\nEnter Username:').strip()
            if len(username)==0: # CHECK IF USERNAME IS ENTERED
                print('Username space cannot be empty\n')
            else:
                username = username.lower()
                break
        if username in read_data.keys(): # CHECK USERNAME IN [KEYS] OF read_data DICTIONARY
            print('Username already taken.Please use another username\n')
            break
        else:
            while True:
                password = input('Enter Password:')
                if len(password)==0:  # CHECK IF PASSWORD IS ENTERED
                    print("Password space cannot be empty\n")
                else:
                    break
            user_account[username] = password   # SAVING username[KEY] AND password[VALUE] IN user_account DICTIONARY (INITIATED BEFORE CALLING FUNCTION: Line No.268)
            while True:
                fname = input('Enter your First name: ').strip()
                if len(fname)==0: # CHECK IF FIRST NAME IS ENTERED
                    print('Enter a valid name\n')
                else:
                    break
            lname = input('Enter your last name: ').strip()
            while True:
                _add = input('Enter your  billing address: ').strip()
                if len(_add)==0: # CHECK IF BILLING ADDRESS IS ENTERED
                    print("Billing address is necessary for proceeding into the store.\n")
                else:
                    break
            while True:
                numb = input('Enter your Phone number: ').strip()
                # CHECK IF INPUT DOES NOT ENTIRELY CONSIST OF DIGITS
                if not numb.isdigit():
                    print('Please enter a number containing digits only.\n')
                else:
                    # PROCESSING WHEN A VALID INPUT IS PROVIDED
                    break
            print('account created succefully')
            # WRITING A DICTIONARY OF USER DATA IN A STRING FORMAT TO WRITE IT IN A FILE
            u_data = '{'+f"'u_name':'{username}', 'Pass':'{password}', 'f_name':'{fname}', 'lname':'{lname}', 'add':'{_add}', 'phone':'{numb}', 'u_cart':{{}}"+'}'
            with open(f'{username}.txt', 'w') as f_user:
                f_user.write(u_data)  # WRITING THE DATA STRING
            break

# FUNCTION TO LOGIN TO ACCOUNT
def login():
    while True:
        username = input('\nenter username:').strip()
        if len(username)==0:
            print('Username space cannot be empty\n')
        else:
            username=username.lower()
            break
    while True:
        password = input('enter password:')
        if len(password)==0:
            print('Enter a Password\n')
        else:
            break
    # CHECKING THE username IN [KEYS] AND MATCHING ITS password[VALUE] WITH IT IN THE read_data DICTIONARY
    if username in read_data.keys() and read_data[username] == password:
        with open(f'{username}.txt', 'r') as f_user: # OPENS USER FILE
            ind_user_read=f_user.read() # SAVING THE READ DATA (WHICH IS STRING) IN ind_data_read
            f_user.close()
            # EVALUATING THE STRING FORM OF DICTIONARY(READ FROM FILE) INTO FUNCTIONING DICTIONARY AND ASSIGNING IT TO "user_data_read"
        user_data_read=eval(ind_user_read ) 
        fname = user_data_read.get('f_name') # GETTING [VALUE] OF f_name[KEY] FROM DICTIONARY AND ASSIGNING IT TO fname
        print(f'\n\n LOGIN SUCCESSFUL.\n\n----Welcome "{fname}!"----')
        
            ###  CART LOOP RUNNING  ###
        while True:
                print('__________________')
                print('<>  MAIN MENU  <>')
                print('------------------')
                a=input("\n1.View Product List\n2. Add to cart\n3.Remove from Cart\n4.View cart\n5.View Shopping History\n6.Proceed to checkout\n7.Log out\nSelect serial number of any one:\n->").strip()

                    # VIEW PRODUCT LIST
                if a=='1': 
                    
                    view_menu()   # CALLING FUNCTION to VIEW PRODUCT LIST 
                                        
                    # ADD PRODUCTS TO CART
                elif a=='2':  
                    view_menu()
                    add_to_cart()   # CALLING FUNCTION TO ADD PRODUCTS
                    
                    # REMOVE PRODUCTS FROM CART    
                elif a=='3':  
                    view_cart()
                    view_menu()
                    rem_cart()   # CALLING FUNCTION TO REMOVE PRODUCTS 
                    
                    # VIEW CART
                elif a=='4':
                    if len(cart)==0: # CHECK IF cart DICTIONARY IS EMPTY
                        print ('\n\n\n----------Cart---------\n* Your Cart is Empty :(\n----------------------\n\n')
                    else:
                        view_cart()  # CALLING FUNCTION TO VIEW CART 

                    # VIEW SHOPPING HISTORY
                elif a=='5':
                    u_cart = user_data_read.get('u_cart') # GETTING [VALUE] OF u_cart FROM user_data_read DICTIONARY
                    print ('\n\n\n\n\n_______________________________________________')
                    print ('_______________SHOPPING HISTORY_______________\n')
                    print ('  ------date/time:  --------- items purchase:---- \n')
                    if len(u_cart)==0: # CHECK IF DICTIONARY[VALUE] OF u_cart[KEY] IN THE DICTIONARY OF user_data_read IS 0 
                        print('            No Shopping History !\n\n')
                    else:
                            # ITERATING IN THE ITEMS OF u_cart DICTIONARY[KEY] IN user_read_data DICTIONARY    #| ## INFO ##      
                        for date,history in u_cart.items():                                                 #|HISTORY IS SAVED IN THE FORM OF DICTIONARY
                            cart_history=""                                                                 #|THAT DICTIONARY IS SAVE IN A DICTIONARY NAMED "u_cart"
                            total=0                                                                         #|THAT u_cart DICTIONARY IS SAVE IN A DICTIONARY OF READ DATA NAME "user_read_data"
                                # ITERATING IN THE ITEMS OF ANOTHER DICTIONARY[VALUE] OF u_cart DICTIONARY
                            for cart_items, quantity in history.items():
                                cart_history = cart_history + f'{cart_items} x {quantity}\n{"":27}'
                                # CALCULATING AMOUNT BY USING [VALUE] OF process_menu dictionary ->
                                # -> FROM THE [KEYS] OBTAINED FROM THE DATA
                                total+=(process_menu[cart_items])*quantity 
                            print (f'{date}   :     {cart_history}')
                            print (f'::: Total bill: Rs.{total}\n')
                            print (f'{"":15} ---------- {"":18} ')
                        print ('_______________________________________________')
                        print ('_______________________________________________\n\n\n')
                    
                    # CHECKOUT
                elif a=='6':
                    if len(cart)==0: # CHECK IF cart DICTIONARY IS EMPTY
                        print('\n\n No items in cart. Add atleast one product to proceed to checkout !!')
                    else:
                        view_cart()
                        while True:
                            confirm=input('\nDo you want to proceed or make changes? Press"Y" to proceed or "N" to go back: ').strip()
                            if confirm == "Y" or confirm =="y":
                                f_user_w=open(f'{username}.txt','w') # OPEN USER FILE IN WRITE MODE TO OVERWRITE OLD DATA WITH UPDATED DATA.

                                from datetime import datetime

                                # GET THE CURRENT DATE AND TIME
                                curr_datetime = datetime.now()

                                # FORMAT THE CURRENT DATE AND TIME
                                format = curr_datetime.strftime("%Y-%m-%d / %H:%M")
                                # SAVING THE cart DICTIONARY IN THE u_cart DICTIONARY WHICH IS SAVED IN THE USER DATA user_data_read DICTIONARY
                                user_data_read['u_cart'][format]=cart  
                                final_udata=str(user_data_read)      ### CONVERTING THE DATA DICTIONARY INTO STRING TO WRITE INTO FILE
                                f_user_w.write(final_udata)  # WRITING THE DATA INTO FILE
                                f_user_w.close()  # CLOSING FILE TO UPADTE FILE WITH THE WRITTEN DATA
                                print("\n\nThank You for placing your order. Your order will be delivered to your billing address within a week. :)\n")
                                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n')
                                cart.clear() # CLEARING cart DICTIONARY FOR FURTHER PURCHASE
                                global bill
                                bill-=bill # CLEARING THE BILL FOR FURTHER PURCHASE
                                user_data_read=eval(final_udata)  # AFTER SAVING, THE STRING IS AGAIN EVALUATED TO DICTIONARY FOR FURTHER OPERATIONS
                                break
                            elif confirm=="n" or confirm=="N":
                                print()
                                break
                            elif confirm!="n" or "N" or "y" or "Y":
                                print('\n!! CHOOSE A VALID OPTION !!')
                 # LOGOUT OF ACCOUNT        
                elif a == '7':
                    print('\nThank you for your visit. Hoping to see you again! :)\n')
                    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n')
                    break
        
                else:
                    print('\n!! CHOOSE AN APPROPRIATE OPTION !!\n')

    else:
        print('\n !! Invalid Username OR Password.Try Again !!')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


###    ----------------------    ###
###    MAIN CODE RUNNING LOOP    ###
###    ----------------------    ###

while True:
    user_account = {}
    print('\n\n==================================')
    print('| Welcome To "THE ESSENCE DECOR" |')
    print('==================================\n')
    print('1.Create Account')
    print('2.Login')
    print('3.Exit Application')
    choice = input('\nSelect an option:').strip()
    
     # CREATE AN ACCOUNT
    if choice=='1':
        import os
        if os.path.exists('accounts.txt') and os.path.getsize('accounts.txt') > 0: # CHECKS IF accounts.txt FILE EXISTS AND IS NOT EMPTY
                with open('accounts.txt', 'r+') as f_main: # AFTER CHECKING, OPENS IT IN READ MODE
                    users_read = f_main.read()
                    read_data=eval('{' + users_read + '}') # EVALUATING THE FILE DATA INTO DICTIONARY FOR USERNAME CHECKING OPERATIONS
        else:
            read_data={} # IF FILE DOSEN'T EXISTS, CREATES AN EMPTY DICTIONARY FOR USERNAME CHECKING OPERATION
        create_account() #CALLING FUNCTION TO CREATE AN ACCOUNT 
        with open('accounts.txt', 'a+') as f_main: 
            for username, password in user_account.items():
                f_main.write(f"'{username}':'{password}',\n") #SAVES THE INPUT DATA FROM user_account DICTIONARY IN THE accounts.txt FILE
    
     # LOGIN
    elif choice=='2':
        import os
        if os.path.exists('accounts.txt') and os.path.getsize('accounts.txt') > 0: # CHECKS IF accounts.txt FILE EXISTS AND IS NOT EMPTY
                with open('accounts.txt', 'r') as f_main: # AFTER CHECKING, OPENS IT IN READ MODE
                    users_read = f_main.read()
                    read_data=eval('{' + users_read + '}') # EVALUATING THE FILE DATA INTO DICTIONARY FOR USERNAME AND PASSWORD CHECKING OPERATIONS
                cart={} # INITATING EMPTY CART DICTIONARY 
                bill=0 #INITIATING BILL=0
                login()  # CALLING FUNCTION TO LOGIN 
        else:
            print('\nCreate atleast one account, no user files present for the program\n')

     # EXIT THE APPLICATION
    elif choice=='3':
        print('\nApplication closed!\n')
        break
    else:
        print('\n! Invalid Choice !')
        print('==================')