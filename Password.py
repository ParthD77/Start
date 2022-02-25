import time

user = ["mythic"]
password = ["parth"]

while True:
    broken = False
    userAtempt = input("Username?\n")
    userAtempt = userAtempt.lower()
    if userAtempt in user:
            userPass = input("Password?\n")
            if userPass in password:
                print ("Welcome!")
                broken = True
                if broken:
                    break
            else:
                usertry = input("Incorrect\n Would you like to try again. \nType yes or no.?\n")
                if usertry == ("yes"):
                    print ("Okay try again")
                elif usertry == ("no"):
                    broken = True
                    if broken:
                        break
                elif usertry != ("yes", "no"):
                    print ("Please only enter yes or no")
    else:
        usertry = input("Incorrect\n Would you like to try again. \nType yes or no.?\n")
        if usertry == ("yes"):
            print ("Okay try again")
        elif usertry != ("yes" or "no"):
            print ("Please only enter yes or no")
            broken = True
            if broken:
                break

