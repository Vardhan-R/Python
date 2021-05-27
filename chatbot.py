import math, time
upTime = 0
l = ["age", "buy", "commands", "customise", "exit", "pet", "points", "time", "uptime", "xp"]
strlst = ""
n = 'To enter a command, start with "!" and enter any of the following commands:'
for i in range (len(l)):
    strlst = strlst + '\n' + str(l[i])
c = n + strlst
slowModeTm = 0

running = False
choice = int(input("1 for Login and 2 for Register: "))
while choice != 1 and choice != 2:
    choice = int(input("1 for Login and 2 for Register: "))

if (choice == 1):
    while not(running):
        check1 = False
        check2 = False
        username_pos = 0
        password_pos = 0
        typed_username = input("Username: ") + '\n'
        typed_password = input("Password: ") + '\n'
        usernames = open("usernames.txt", "r")
        passwords = open("passwords.txt", "r")
        all_usernames = usernames.readlines()
        for i in range(len(all_usernames)):
            if typed_username == all_usernames[i]:
                check1 = True
                username_pos = i
                break

        all_passwords = passwords.readlines()
        for i in range(len(all_passwords)):
            if typed_password == all_passwords[i]:
                check2 = True
                password_pos = i
                break

        if check1 and check2 and (username_pos == password_pos):
            running = True
        else:
            print("Username and Password do not match.")
else:
    typed_username = input("Username: ") + '\n'
    check_usernames = open("usernames.txt", "r")
    all_usernames = check_usernames.readlines()
    while typed_username in all_usernames:
        print("This username already exists. Please type a different one.")
        typed_username = input("Username: ") + '\n'
    typed_password = input("Password: ") + '\n'
    usernames = open("usernames.txt", "a")
    passwords = open("passwords.txt", "a")
    usernames.write(typed_username)
    passwords.write(typed_password)
    print("Your account has been created.")

while running:
    petsFile = open("pet.txt", "r")
    pets = int(petsFile.readline())
    petFull = "The streamer's pet has been pet " + str(pets + 1) + " times!"

    upTime = upTime + 1

    ptsFile = open("pts.txt", "r")
    myPts = int(ptsFile.readline())
    myPtsFull = 'You have ' + str(myPts) + ' points! You may be able to buy something. To buy something, use the "!buy" command.'

    timeForStreamer = str(time.strftime("%H:%M:%S", time.localtime()))
    timeForStreamer = "It is currently "+ timeForStreamer + " for the streamer."

    buyFull = "Badges:" + '\n' + "1) ( . )( . ) -- 5 points" + '\n' + "2) {()} -- 10 points" + '\n' + "3) 8=====D -- 10 points (Customisable!)" + '\n' + '\n' + "4) [Remove Current Badge] -- 0 points"
    badgeDisp = open("badge.txt", "r")
    badgeDisplay = badgeDisp.readline()
    badgeDisp.close()

    rankDisp = open("xp.txt", "r")
    currentxp = rankDisp.readline()
    currentRank = math.floor(math.log10(int(currentxp) + 0.1)) + 1
    rankDisplay = "(" + str(currentRank) + ") "
    xpToRankUp = 10 ** math.ceil(math.log10(int(currentxp) + 1.1)) - int(currentxp) - 1
    xpMsg = "You have " + str(int(currentxp) + 1) + " XP points! You need " + str(xpToRankUp) + " more XP points to rank up!"
    rankDisp.close()

    def customise():
        badgeCheck = open("badge.txt", "r")
        currentBadge = badgeCheck.readline()
        newBadge = currentBadge
        if (len(currentBadge)) != 0:
            if (currentBadge[0] != "8" and currentBadge[0] != "("):
                print("Bot: You do not have the permission to use this command.")
            elif (currentBadge[0] == "8"):
                print("Here are the ways in which you can customise your current badge:")
                print("1) Increase the size by 1 =.")
                print("2) Decrease the size by 1 =.")
                while True:
                    choice = input("1 or 2? ")
                    ptsToCustomise = open("pts.txt", "r")
                    myPts = int(ptsToCustomise.readline())
                    if myPts >= 1:
                        myPts = myPts - 1
                        if choice == "1":
                            ptsEdit = open("pts.txt", "w")
                            ptsEdit.write(str(myPts))
                            ptsEdit.close()
                            currentBadge = currentBadge[0:-2] + "=D "
                            badgeUpdate = open("badge.txt", "w")
                            badgeUpdate.write(currentBadge)
                            badgeUpdate.close()
                        elif ((choice == "2") and (currentBadge[2] == "=")):
                            ptsEdit = open("pts.txt", "w")
                            ptsEdit.write(str(myPts))
                            ptsEdit.close()
                            currentBadge = currentBadge[0:-3] + "D "
                            badgeUpdate = open("badge.txt", "w")
                            badgeUpdate.write(currentBadge)
                            badgeUpdate.close()
                        elif ((choice == "2") and (currentBadge[2] != "=")):
                            print("Bot: That is not how you make a vagina!")
                        else:
                            break
                    else:
                        print("Bot: You don't have enough points to purchase this item.")
                        break
                    ptsToCustomise.close()
            elif (currentBadge[0] == "("):
                print("Here are the ways in which you can customise your current badge:")
                print("1) Increase the size.")
                print("2) Decrease the size.")
                c = -1
                for i in newBadge:
                    if i == " ":
                        c = c + 1
                c /= 4
                while True:
                    choice = input("1 or 2? ")
                    ptsToCustomise = open("pts.txt", "r")
                    myPts = int(ptsToCustomise.readline())
                    if myPts >= 1:
                        myPts = myPts - 1
                        joinBadge = ""
                        if choice == "1":
                            ptsEdit = open("pts.txt", "w")
                            ptsEdit.write(str(myPts))
                            ptsEdit.close()
                            c += 1
                            c = int(c)
                            newBadge = "("
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + "."
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + ")("
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + "."
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + ") "
                            badgeUpdate = open("badge.txt", "w")
                            badgeUpdate.write(newBadge)
                            badgeUpdate.close()
                        elif ((choice == "2") and (newBadge[1] == " ")):
                            ptsEdit = open("pts.txt", "w")
                            ptsEdit.write(str(myPts))
                            ptsEdit.close()
                            c -= 1
                            c = int(c)
                            newBadge = "("
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + "."
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + ")("
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + "."
                            for i in range(c):
                                newBadge = newBadge + " "
                            newBadge = newBadge + ") "
                            badgeUpdate = open("badge.txt", "w")
                            badgeUpdate.write(newBadge)
                            badgeUpdate.close()
                        elif ((choice == "2") and (newBadge[1] == ".")):
                            print("Bot: Your badge is already at its smallest size.")
                        else:
                            break
                    else:
                        print("Bot: You don't have enough points to purchase this item.")
                        break
                    ptsToCustomise.close()
        else:
            print("Bot: You do not have the permission to use this command.")
        badgeCheck.close()

    d = {"!commands": c, "!uptime": upTime, "!age": 16, "!pet": petFull, "!exit": "Bye!", "!time": timeForStreamer, "!points": myPtsFull, "!buy": buyFull, "!customise": "Customise:", "!xp": xpMsg}

    x = ""
    x = str(input(rankDisplay + badgeDisplay + "You: "))
    x = x.lower()

    def increaseXP(s):
        xpFile = open("xp.txt", "r")
        xp = int(xpFile.readline())
        xpFile.close()
        xpFile = open("xp.txt", "w")
        xp = str(xp + s)
        xpFile.write(xp)
        xpFile.close()

    increaseXP(1)

    if x in d:
        print("Bot:", d.get(x))

        if x == "!pet":
            petsEdit = open("pet.txt", "w")
            petsEdit.write(str(pets + 1))
            petsEdit.close()

        if x == "!buy":
            def buy():
                choice = input("1, 2, 3 or 4? ")
                if choice == "4":
                    badge = open("badge.txt", "w")
                    badge.close()
                    print("Bot: Your badge has been removed.")
                elif choice == "1" and myPts >= 5:
                    badgeCheck = open("badge.txt", "r")
                    currentBadge = badgeCheck.readline()
                    if currentBadge != "( . )( . ) ":
                        ptsEdit = open("pts.txt", "w")
                        ptsEdit.write(str(myPts - 5))
                        ptsEdit.close()
                        badge = open("badge.txt", "w")
                        badge.write("( . )( . ) ")
                        badge.close()
                        increaseXP(5)
                        print("Bot: Item successfully purchased!")
                    else:
                        print("Bot: You already have this badge!")
                    badgeCheck.close()
                elif choice == "2" and myPts >= 10:
                    badgeCheck = open("badge.txt", "r")
                    currentBadge = badgeCheck.readline()
                    if currentBadge != "{()} ":
                        ptsEdit = open("pts.txt", "w")
                        ptsEdit.write(str(myPts - 10))
                        ptsEdit.close()
                        badge = open("badge.txt", "w")
                        badge.write("{()} ")
                        badge.close()
                        increaseXP(10)
                        print("Bot: Item successfully purchased!")
                    else:
                        print("Bot: You already have this badge!")
                    badgeCheck.close()
                elif choice == "3" and myPts >= 10:
                    badgeCheck = open("badge.txt", "r")
                    currentBadge = badgeCheck.readline()
                    if currentBadge != "8=====D ":
                        ptsEdit = open("pts.txt", "w")
                        ptsEdit.write(str(myPts - 10))
                        ptsEdit.close()
                        badge = open("badge.txt", "w")
                        badge.write("8=====D ")
                        badge.close()
                        increaseXP(10)
                        print('Bot: Item successfully purchased! Congradulations! You have unlocked the command "!customise"!')
                    else:
                        print("Bot: You already have this badge!")
                    badgeCheck.close()
                elif choice == "1" and myPts < 5:
                    print("Bot: You don't have enough points to purchase this item.")
                elif choice == "2" and myPts < 10:
                    print("Bot: You don't have enough points to purchase this item.")
                elif choice == "3" and myPts < 10:
                    print("Bot: You don't have enough points to purchase this item.")
            buy()

        if x == "!customise":
            customise()

    if x == "!exit":
        break

    if len(x) != 0:
        if x[0] == "!" and x not in d:
            print("Bot: That command does not exist. Here's a list of our commands:", strlst)

    if upTime % 5 == 0:
        ptsEdit = open("pts.txt", "w")
        ptsEdit.write(str(myPts + 1))
        ptsEdit.close()
        print('Bot: You have earned a point! You may be able to buy something. To buy something, use the "!buy" command. To view your points, use the "!points" command.')

    petsFile.close()
    ptsFile.close()

    for i in range(slowModeTm):
        print(slowModeTm - i)
        time.sleep(1)

# points
# rewardSystem
# badges
# removeBadges
# ranks
# cutomise command should require another command to be typed in since multiple things are/will be customisable
# gifts
# sex badge (preferably animated) (custom for the vagina badge)
# bigger boobs (custom) (make C cup normal (like 3 spaces in b/w or smthing) and have to option to reduce down to A or increase (by changing the number of spaces))
# autocorrect specific characters to emojis
# in the points file, add all accounts' points
# add a feature to tag other accounts using "@"
# this can also be used to view other ppl's pts
# add all accounts' badges into one file
# make a new file for the badges available
# add other accounts' xp to the xp file
# the code uses the number of the line of the username, password, pts, badge, xp, etc. (each account will have a unique line number and that line number will be same in all these files)
