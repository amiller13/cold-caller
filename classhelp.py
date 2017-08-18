from tkinter import *
import random
import time
#array that holds the name of everyone in the class
names = ['Amanda', 'Rishika', 'Avni', 'Anissa', 'Chloe', 'Jennifer',
'Tierra', 'Stefanie', 'Sydney', 'Anna', 'Annabelle', 'Tianna', 'Jessenia', 'Stephanie', 'Christina',
'Ashley', 'Aileen', 'Aneil', 'Aurpita', 'Karina']
norepeatnames = ['Amanda', 'Rishika', 'Avni', 'Anissa', 'Chloe', 'Jennifer',
'Tierra', 'Stefanie', 'Sydney', 'Anna', 'Annabelle', 'Tianna', 'Jessenia', 'Stephanie', 'Christina',
'Ashley', 'Aileen', 'Aneil', 'Aurpita', 'Karina']

def coldcall():
    global names
    cc = Toplevel()
    person = Label(cc, text = "")
    person.pack()
    def press():
        person.config(text = random.choice(names))
        cc.update()
    call = Button(cc, command = press, text = "Cold Call").pack()

def norepeats():
    global names
    nr = Toplevel()
    person = Label(nr, text = "")
    person.pack()
    def press():
        global norepeatnames
        n = random.choice(norepeatnames)
        person.config(text = n)
        norepeatnames.remove(n)
        if(len(norepeatnames)<1):
            norepeatnames = names
    call = Button(nr, command = press, text = "Cold Call").pack()

def randomgroup():
    global names
    global norepeatnames
    rg = Toplevel()
    nclick = False
    sclick = False
    e1 = Entry(rg)
    e2 = Entry(rg)

    def pnum():
        nonlocal nclick
        if(not nclick):
            e1.grid(row = 0, column = 1)
            nclick = True
    def psize():
        nonlocal sclick
        going = True
        if( not sclick):
            e2.grid(row = 1, column = 1)
            sclick = True

    def makegroup():
        nonlocal e1
        nonlocal e2
        global norepeatnames
        global names
        answer = ""
        n = 0
        size = 0
        students = len(names)
        upper = students
        group = ""
        counter = 0
        groups = []
        randomOrder = []
        uneven = False
        making = True
        ask = False
        x = Label(rg, text = "")
        x.grid(row = 4)

        if(e1.get().isdigit()):
                n = int(e1.get())
                size = int(students/n)
        elif(e2.get().isdigit()):
                size = int(e2.get())
                n = int(students/size)
                ask = True
        else:
            x.config(text = "invalid input!")
            making = False

        if(making):
            remainder = students%size
            if(remainder!=0):
                uneven = True
                upper = students - remainder
            for i in range(0,len(names)):
                c = random.choice(norepeatnames)
                randomOrder.append(c)
                norepeatnames.remove(c)
            norepeatnames = names
            for x in range(0,n):
                for z in range(0,size):
                    group = randomOrder[counter] + ' ' + group
                    counter = counter + 1
                groups.append(group)
                group = ''
            if(uneven):
                while(upper < students):
                    b = (upper%len(groups))
                    groups[(b - 1)] = groups[(b- 1)] + ' ' + randomOrder[upper]
                    upper = upper + 1
            g = Toplevel()
            e1.delete(0,'end')
            e2.delete(0, 'end')
            Label(g, text="\n".join(groups)).pack()


    num = Button(rg, command = pnum, text = "Number of Groups").grid(row = 0,column = 0)
    sz = Button(rg, command = psize, text = "Group Size").grid(row = 1, column = 0)
    mg = Button(rg, command = makegroup, text = "Make Groups").grid(row = 2)



root = Tk()
root.geometry("400x30")
Label(root,text = "Girls Who Code Classroom Helper", font = ("Helvetica", 10, "bold italic")).grid(row = 0)
menubar = Menu(root)
menubar.add_command(label = "Cold Call",command = coldcall)
menubar.add_command(label = "Cold Call Without Repeats", command = norepeats)
menubar.add_command(label = "Random Group Generator", command = randomgroup)
root.config(menu = menubar)
root.mainloop()
