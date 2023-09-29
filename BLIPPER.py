import random
import datetime
import time


x = datetime.datetime.now()
t = x.strftime("%d %B %Y")
items = ["Spotify","Apple Music"]
expiry = [t,t]
expiresin = ["EXPIRED","EXPIRED"]


def mainmenu():
    print("*"*80)
    print()
    print("* B L I P P E R *".center(80))
    print("* Live An Organised Life with Blipper - The Ultimate App *".center(80))
    print()
    print("*"*80)
    print("\n"*3)
    print("PRESS ENTER TO CONTINUE".center(80))
    input()

def removeitem():
    global items
    global expiry
    global expiresin
    print("*"*80)
    print("LET'S REMOVE AN ITEM".center(80))
    print("\n"*2)
    print("What item do you want to remove?".center(80))
    for i in range(len(items)):
        s = str(i+1)+". "+items[i]
        print(s.center(80))
    n = int(input("INPUT HERE > "))
    item = items[n-1]
    items.pop(n-1)
    expiry.pop(n-1)
    expiresin.pop(n-1)
    a = "You have removed "+item+"."
    print(a.center(80))
    print("PRESS ENTER TO CONTINUE")
    print("*"*80)
    input()
    
def additem():
    global items
    global expiry
    global expiresin
    print("*"*80)
    print("LET'S ADD AN ITEM".center(80))
    print("\n"*2)
    print("< What do you want to add?".rjust(80))
    item = str(input("INPUT HERE >"))
    items.append(item)
    print("\n"*2)
    print("< What is the expiry month? (1-12)".rjust(80))
    m = int(input("INPUT HERE >"))
    valid = 0
    while valid == 0:
        if m >= 1 and m <= 12:
            month = m
            valid = 1
        else:
            m = int(input("INPUT CORRECTLY! > "))
    print("\n"*2)
    thirtydays = [4,6,9,11]
    thirty1days = [1,3,5,7,8,10,12]
    if month in thirtydays:
        print("< What is the expiry date? (1-30)".rjust(80))
        d = int(input("INPUT HERE >"))
        valid = 0
        while valid == 0:
            if d >= 1 and d <= 30:
                day = d
                valid = 1
            else:
                d = int(input("INPUT CORRECTLY! > "))
    elif month in thirty1days:
        print("< What is the expiry date? (1-31)".rjust(80))
        d = int(input("INPUT HERE >"))
        valid = 0
        while valid == 0:
            if d >= 1 and d <= 31:
                day = d
                valid = 1
            else:
                d = int(input("INPUT CORRECTLY! > "))
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    full = str(day)+" "+months[month-1]+" 2022"
    expiry.append(full)
    x = datetime.datetime.now()
    t = x.strftime("%d")
    q = x.strftime("%m")
    if q in thirtydays:
        remainingd = 30-int(t)
    elif q in thirty1days:
        remainingd = 31-int(t)
    else:
        remainingd = 28-int(t)
    remainingd2 = (month - int(q)-1)*30
    remainingdays = remainingd + remainingd2
    expiresin.append(remainingdays)
    print("You have added item",item,"which expires at",full)
    print("PRESS ENTER TO CONTINUE")
    print("*"*80)
    input()
    
    
def accountcreation():
    pass
    
def loadingscreen():
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Loading....")
    time.sleep(1)

def personalitems():
    global items
    global expiry
    global expiresin
    print("\n"*5)
    print("*"*80)
    print("* B L I P P E R *".center(80))
    print("\n"*3)
    a = "{0:20} {1:1} {2:18} {3:1} {4:15}".format("ITEM","|","EXPIRY DATE","|","EXPIRES IN")
    print(a.center(80))
    print()
    for i in range(len(items)):
        a = "{0:20} {1:1} {2:18} {3:1} {4:15}".format(items[i],"|",expiry[i],"|",str(expiresin[i]))
        print(a.center(80))
    print("\n"*3)
    print("1. Add New Item".center(80))
    print("2. Remove An Item".center(80))
    print("3. Exit Blipper".center(80))
    print()
    x = datetime.datetime.now()
    t = "DATE & TIME: "+x.strftime("%d %B %Y %I:%M %p")
    print(t.center(80))
    print("*"*80)
    print("\n"*5)
    choice = int(input("Please input a number > "))
    return choice
    
mainmenu()
running = 1
while running == 1:
    loadingscreen()
    n = personalitems()
    if n == 3:
        running = 0
    elif n == 1:
        additem()
    elif n == 2:
        removeitem()
