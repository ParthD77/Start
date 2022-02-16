user = "Mythic".lower()
password = "parth"

userAtempt = input("Username?\n")
if userAtempt.lower() == user:
    userPass = input("Password?\n")
    if userPass == password:
        print ("Welcome!")
    else:
        print ("Incorrect")
else:
    print ("Incorrect")