import random
import time

#array that holds the name of everyone in the class
names = ['Amanda', 'Rishika', 'Avni', 'Anissa', 'Chloe', 'Jennifer',
'Tierra', 'Stefanie', 'Sydney', 'Anna', 'Annabelle', 'Tianna', 'Jessenia', 'Stephanie', 'Christina',
'Ashley', 'Aileen', 'Aneil', 'Aurpita', 'Karina']
#creates an identical array to names that is modified in the program
norepeatnames = ['Amanda', 'Rishika', 'Avni', 'Anissa', 'Chloe', 'Jennifer',
'Tierra', 'Stefanie', 'Sydney', 'Anna', 'Annabelle', 'Tianna', 'Jessenia', 'Stephanie', 'Christina',
'Ashley', 'Aileen', 'Aneil', 'Aurpita', 'Karina']

#coldcaller that picks a random name in the class and does not call on the same name twice in a row
def coldcall():
    global names
    global going
    #picks the first random name
    current = random.choice(names)
    #sets the previous name to an empty string
    previous = ""
    classtime = True
    print("Press enter to start cold calling. Press Q to stop cold calling")
    while(classtime):
        z = input()
        if(z=='q' or z == 'Q'):
            classtime = False
            printMenu()
            break
        redo = True
        #checks to make sure a new name is being picked
        while(redo):
            if(current != previous):
                print(current)
                #sets the name printed to the prvious name
                previous = current
                #picks a new name
                current = random.choice(names)
                redo = False
            else:
                #if it picks the same name twice, pick a new name
                current = random.choice(names)

#coldcaller that won't call on anyone twice until everyone has spoken
def norepeat():
    global names
    global norepeatnames
    classtime = True
    print("Press enter to start cold calling. Press Q to stop cold calling.")

    #classtime loop that allows the program to cold call forever
    while(classtime):
        z = input()
        if(z=='q' or z == 'Q'):
            classtime = False
            printMenu()
            break
        n = random.choice(norepeatnames)
        print(n)
        norepeatnames.remove(n)
        if(len(norepeatnames)<1):
            norepeatnames = names

#creates random groups given a group size
def randomgroup():
    #global variables used
    global names
    global norepeatnames
    #number of students in the classroom
    students = len(names)
    #number of groups
    n = 0
    #size of each group
    size = 0
    #vvariable that represents whether the program should ask the user about group size or not
    ask = False
    #an array to hold the names of the class in a random order
    randomOrder = []
    #upperbound for loop that changes based on how many people you want in each group
    upper = students
    counter = 0
    group = ''
    #array that holds a group in each position
    groups = []
    #variable that is true when there can be the same number of people in each group
    uneven = False

    #lets the user decide how they want to make the groups
    print('Enter A to input how many people you want in each group. Enter B to input how many groups you want')
    ans = input()
    if(ans == 'a' or ans == 'A'):
        print('How many people do you want in each group?')
        size = int(input())
        n = int(students/size)
        ask = True
    if(ans == 'b' or ans == 'B'):
        print('How many groups do you want?')
        n = int(input())
        size = int(students/n)

    #left over people who need to be placed in a group
    remainder = students%size

    #checks to see if students are not divisible into requested group size and then distributes extras accordingly
    if(ask):
        if(students%size !=0):
            uneven = True
            print('How many groups would you like? ' + str(n) + ' or ' + str(n+1))
            answer = input()
    else:
        if(students%size !=0):
            uneven = True
            answer = n
    #places all the students in an array in a random order
    for i in range(0,len(names)):
        c = random.choice(norepeatnames)
        randomOrder.append(c)
        norepeatnames.remove(c)
    norepeatnames = names
    #if uneven number of people in group, adjusts the upperbound for the loop
    if(uneven):
        upper = students - remainder
    #creates random groups
    while(counter < upper):
        for x in range(0,n):
            for z in range(0,size):
                group = randomOrder[counter] + ' ' + group
                counter = counter + 1
            groups.append(group)
            group = ''
    #distributes extra students into groups based on user's preferences
    if(uneven):
        if(int(answer) == n):
            while(upper < students):
                b = (upper%len(groups))
                groups[(b - 1)] = groups[(b- 1)] + ' ' + randomOrder[upper]
                upper = upper + 1
        else:
            g = ''
            while(upper < students):
                g = randomOrder[upper] + ' ' + g
                upper = upper + 1
            groups.append(g)
    for x in groups:
        print(x)
    #delays before printing the menu
    time.sleep(3)
    printMenu()

#randomly assigns each student in the class a number between 1 and 20
def randomNum():
    global names
    global norepeatnames
    randomOrder = []
    for i in range (0,len(names)):
        c = random.choice(norepeatnames)
        randomOrder.append(c)
        norepeatnames.remove(c)
    norepeatnames = names
    for x in range(0, len(randomOrder)):
        if(x<9):
            print(' ' + str(x + 1) + ' ' + randomOrder[x])
        else:
            print(str(x + 1) + ' ' + randomOrder[x])
    time.sleep(2)
    printMenu()

def printMenu():
    print(" \n Press A to cold-call a random name. \n Press B to cold-call with no repeats. \n Press C to generate groups. \n Press D to assign random numbers.\n Press Q to quit.")
    choice = input()
    if(choice == 'a' or choice == 'A'):
        coldcall()
    elif(choice == 'b' or choice == 'B'):
        norepeat()
    elif(choice == 'c' or choice == 'C'):
        randomgroup()
    elif(choice =='d' or choice == 'D'):
        randomNum()
    elif(choice == 'q' or choice == 'Q'):
        exit()
    else:
        print("invalid choice")
        printMenu()
def isAbsent(students):
    global names
    global norepeatnames
    newlist = []
    students = students.title()
    for i in range (0,len(names)):
        if names[i] not in students:
            newlist.append(names[i])
    names = newlist
    norepeatnames = newlist

print("Welcome to the cold caller!")
print("Is anyone absent today? Type Y if someone is absent")
an = input()
if(an == 'y' or an == 'Y'):
    print('Please enter the students who are absent separated by spaces')
    isAbsent(input())
printMenu()
