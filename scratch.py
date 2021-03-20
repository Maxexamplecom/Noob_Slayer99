import time
import random
#usrm = Username
#passrd = Password
#cnfrm = Confirm
#pswrd = Password

email = ('wateriswet247365@gmail.com')
username = ("Noob Slayer")
password = ("Islaynoobs")
Eml = input("please enter email")
if Eml == (email):

    user = input("Please enter username          ")
    if user == username:
        pswrd = input("Please enter password          ")
        if pswrd == password:
            print('a verifacation code has been sent')
            eml = input('please enter the verifacation Code')
            if eml == ("Okay"):
                print("Login successful")
                wshpro = input("Do you wish to proceed?        ")
                if wshpro == ('yes'):
                    print("great!")
                    time.sleep(.5)
                    print("Proceed to the following webpage to acess your account")
                    print("www.gmail.com/u/0/#inbox")
else:
    print('invalid Input')
    print('Please Restart The Program')
    print("sequence terminated")
    time.sleep(2)
    print("Process approved")
    time.sleep(2)
    print("Account termination aquired")

