import csv
import os
import sys
import msvcrt
import traceback


def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def login():
    print('========================================================================================================================')
    print('                                                    Easy ERP')
    print('========================================================================================================================')

    print(' ')
    
    print('Hello, Welcome to the login screen!')
    username = raw_input('Username : ')
    print('Password :')
    password = ''
    while True:
        x = msvcrt.getch()
        if x == '\r':
            break
        sys.stdout.write(' ')
        password +=x
    print(' ')
    with open('data.csv') as csvfile:
        info = csv.reader(csvfile, delimiter = ',')
        for row in info:
            if row[1] == 'p':
                p = row[2]
            elif row[1] == 'u':
                u = row[2]
            elif row[0] != 'info':
                break
    p = decrypt(p)
    password = password.lower()
    username = username.lower()
    p = p.lower()
    u = u.lower()
    if password == p and username == u:
        clear()
        welcome_screen(username)
    else:
        print('Invalid credentials entered!')
        login()

def decrypt(p):
    
    enlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

    p = p.split('a')
    for i in range (0, len(p)):
        length = len(p[i])
        p[i] = enlist[length-1]
    p = p[:-1]
    string = ""
    for i in p:
        string += i
    p = string
    return p

def encrypt(password):

    enlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    password_new = ''
    for i in range(0,len(password)):
        for j in enlist:
            if password[i] == j or password[i] == j.upper():
                index = enlist.index(j)
                index = index + 1
                string = ""
                for k in range(0,index):
                    password_new += '.'
                password_new += 'a'
    return password_new

def usr_setting():
    print('What would you like to edit?')
    print('1. User Name')
    print('2. Password')
    print('3. Store Name')
    print('4. Main Menu')

def control(choice,username):
    choice = str(choice)
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        add_item(username)
    elif choice == '4':
        delete_item(username)
    elif choice == '5':
        usr_setting()
    elif choice == '6':
        login()
    else:
        print('Invalid option entered!')
        welcome_screen(username)

def add_item(username):
    print('========================================================================================================================')
    print('                                                    Easy ERP')
    print('========================================================================================================================')
    print(' ')
    serial = raw_input('Serial Number: ')
    name = raw_input('Name of the item: ')
    unit = raw_input('Unit of measurement: ')
    qty = int(raw_input('units available: '))
    capacity = int(raw_input('units that can be held: '))
    diff = capacity - qty
    array = ['item',serial,name,unit,qty,capacity,diff]

    serial_array = []
    
    with open('data.csv') as csvfile:
        rows = csv.reader(csvfile,delimiter = ',')
        for i in rows:
            if i[0] == 'item':
                serial_array.append(i[1])

    if str(serial) not in serial_array:
    
        with open('data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(array)
    else:
        clear()
        print('Product already exists')
        x = raw_input('Press any key to continue')
        clear()
        welcome_screen(username)
    clear()
    print('Item added successfully!')
    x = raw_input('press any key to continue')
    clear()
    welcome_screen(username)

serial_array = []
name_array =[]

def delete_item(username):
    x = raw_input('Sure you want to delete an item? (y/n) : ')
    if x == 'y' or x == 'Y':
        os.rename('data.csv','data0.csv')
        with open('data0.csv') as csvfile:
            rows = csv.reader(csvfile,delimiter = ',')
            display = csv.reader(csvfile,delimiter = ',')
            print('Here are the list of items you can delete! (serial no, name)')
            for i in display:
                if i[0] == 'item':
                    print(i[1] + ' ' + i[2])
            print(' ')
            parameter = raw_input('Please enter serial number or name of the item to be deleted: ')
            x = 1
        with open('data0.csv') as csvfile:
            rows = csv.reader(csvfile,delimiter = ',')
            for i in rows:
                if i[1] == parameter or i[2] == parameter:
                    x = 0
                else:
                    with open('data.csv','a') as newfile:
                        writer = csv.writer(newfile)
                        writer.writerow(i)
        os.remove('data0.csv')
        clear()
        welcome_screen(username)
    elif x == 'N' or x == 'n':
        clear()
        welcome_screen(username)

    else:
        clear()
        x = input('Wrong input entered... Press any key to redirect to main menu.')
        clear()
        welcome_screen()
        
    
def welcome_screen(username):
    print('========================================================================================================================')
    print('                                                    Easy ERP')
    print('========================================================================================================================')

    print(' ')
          
    print('Hi ' + username + ', What would you like to do?')
    print('1. View Stock')
    print('2. Update Stock')
    print('3. Add new item')
    print('4. Delete an item')
    print('5. Edit user details')
    print('6. Logout')
    option = input('Option: ')
    clear()
    control(option,username)

try:
    os.system('mode con: cols=120 lines=40')
    login()
except:
    x = raw_input(" ")
    print '-'*60
    traceback.print_exc(file=sys.stdout)
    print '-'*60
