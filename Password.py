import time
user = ["Mythic"]
password = ["parth"]

while True:
    broken = False
    userAtempt = input("Username?\n")
    if userAtempt in user:
        while True:
            userPass = input("Password?\n")
            if userPass in password:
                print ("Welcome!")
                broken = True
                if broken:
                 break
            else:
                usertry = input("Incorrect\n Would you like to try again. \nType yes or no.?\n")
                if usertry == ("no"):
                    broken = True
                    break
    else:
        usertry = input("Incorrect\n Would you like to try again. \nType yes or no.?\n")
        if usertry == ("no"):
            broken = True
            break
