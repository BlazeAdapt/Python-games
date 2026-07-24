import tkinter as tk
import numpy as np
import random

ROBOT=True


currentstate = np.zeros((6, 7))
depthF=3+1
depth=depthF-1
currentstatecount = np.zeros(7)

hoverprev = -1
jprev = 1
turn =-1
number=3
strong=0

def checkwin(y, x,arr):
    wins = ""

    if (x > 2 and (arr[y, x] == arr[y, x - 1]
                   and arr[y, x] == arr[y, x - 2]
                   and arr[y, x] == arr[y, x - 3])):
        wins += "L"
    if (x > 1 and x < 6
            and (arr[y, x] == arr[y, x - 1]
                 and arr[y, x] == arr[y, x - 2]
                 and arr[y, x] == arr[y, x + 1])):
        wins += "l"
    if (x < 4 and (arr[y, x] == arr[y, x + 1]
                   and arr[y, x] == arr[y, x + 2]
                   and arr[y, x] == arr[y, x + 3])):
        wins += "R"
    if (x < 5 and x > 0
            and (arr[y, x] == arr[y, x + 1]
                 and arr[y, x] == arr[y, x + 2]
                 and arr[y, x] == arr[y, x - 1])):
        wins += "r"
    if (y < 3 and (arr[y, x] == arr[y + 1, x]
                   and arr[y, x] == arr[y + 2, x]
                   and arr[y, x] == arr[y + 3, x])):
        wins += "D"
    if (y < 3 and x > 2
            and (arr[y, x] == arr[y + 1, x - 1]
                 and arr[y, x] == arr[y + 2, x - 2]
                 and arr[y, x] == arr[y + 3, x - 3])):
        wins += "1"
    if (y < 4 and x > 1 and x < 6 and y > 0
            and (arr[y, x] == arr[y + 1, x - 1]
                 and arr[y, x] == arr[y + 2, x - 2]
                 and arr[y, x] == arr[y - 1, x + 1])):
        wins += "2"
    if (y < 5 and x > 0 and x < 5 and y > 1
            and (arr[y, x] == arr[y + 1, x - 1]
                 and arr[y, x] == arr[y - 1, x + 1]
                 and arr[y, x] == arr[y - 2, x + 2])):
        wins += "3"
    if (x < 4 and y > 2
            and (arr[y, x] == arr[y - 3, x + 3]
                 and arr[y, x] == arr[y - 1, x + 1]
                 and arr[y, x] == arr[y - 2, x + 2])):
        wins += "4"
    if (y < 3 and x < 4
            and (arr[y, x] == arr[y + 1, x + 1]
                 and arr[y, x] == arr[y + 2, x + 2]
                 and arr[y, x] == arr[y + 3, x + 3])):
        wins += "5"
    if (y < 4 and x < 5 and x > 0 and y > 0
            and (arr[y, x] == arr[y + 1, x + 1]
                 and arr[y, x] == arr[y + 2, x + 2]
                 and arr[y, x] == arr[y - 1, x - 1])):
        wins += "6"
    if (y < 5 and x < 6 and x > 1 and y > 1
            and (arr[y, x] == arr[y + 1, x + 1]
                 and arr[y, x] == arr[y - 1, x - 1]
                 and arr[y, x] == arr[y - 2, x - 2])):
        wins += "7"
    if (x > 2 and y > 2
            and (arr[y, x] == arr[y - 3, x - 3]
                 and arr[y, x] == arr[y - 1, x - 1]
                 and arr[y, x] == arr[y - 2, x - 2])):
        wins += "8"

    if len(wins):
        return wins
    return False


def drawwin(x, event):
    global number
    global ROBOT
    hover = int(event.x / 154)
    if ROBOT == True:
        if turn == 1:
            hover = number
    print(ROBOT)
    print(hover)
    j = currentstatecount[hover] - 1
    if x == 'L':
        canvas.create_line(154 * hover + 77,
                           660 - 120 * j,
                           154 * hover - 385,
                           660 - 120 * j,
                           fill='green',
                           width=5)
    if x == 'R':
        canvas.create_line(154 * hover + 77,
                           660 - 120 * j,
                           154 * hover + 539,
                           660 - 120 * j,
                           fill="green",
                           width=5)
    if x == 'l':
        canvas.create_line(154 * hover + 231,
                           660 - 120 * j,
                           154 * hover - 231,
                           660 - 120 * j,
                           fill='green',
                           width=5)
    if x == 'r':
        canvas.create_line(154 * hover - 77,
                           660 - 120 * j,
                           154 * hover + 385,
                           660 - 120 * j,
                           fill="green",
                           width=5)
    if x == 'D':
        canvas.create_line(154 * hover + 77,
                           660 - 120 * j,
                           154 * hover + 77,
                           1020 - 120 * j,
                           fill="green",
                           width=5)

    if x == '1':
        canvas.create_line(154 * hover + 77,
                           660 - 120 * j,
                           154 * hover - 385,
                           1020 - 120 * j,
                           fill="green",
                           width=5)
    if x == '2':
        canvas.create_line(154 * hover + 231,
                           540 - 120 * j,
                           154 * hover - 231,
                           900 - 120 * j,
                           fill="green",
                           width=5)
    if x == '3':
        canvas.create_line(154 * hover + 385,
                           420 - 120 * j,
                           154 * hover - 77,
                           780 - 120 * j,
                           fill="green",
                           width=5)
    if x == '4':
        canvas.create_line(154 * hover + 539,
                           300 - 120 * j,
                           154 * hover + 77,
                           660 - 120 * j,
                           fill="green",
                           width=5)

    if x == '5':
        canvas.create_line(154 * hover + 77,
                           660 - 120 * j,
                           154 * hover + 539,
                           1020 - 120 * j,
                           fill="green",
                           width=5)
    if x == '6':
        canvas.create_line(154 * hover - 77,
                           540 - 120 * j,
                           154 * hover + 385,
                           900 - 120 * j,
                           fill="green",
                           width=5)
    if x == '7':
        canvas.create_line(154 * hover - 231,
                           420 - 120 * j,
                           154 * hover + 231,
                           780 - 120 * j,
                           fill="green",
                           width=5)
    if x == '8':
        canvas.create_line(154 * hover - 385,
                           300 - 120 * j,
                           154 * hover + 77,
                           660 - 120 * j,
                           fill="green",
                           width=5)


def displaymove(event):
    global hoverprev
    global jprev
    global turn

    hover = int(event.x / 154)

    j = currentstatecount[hover]
    if not hover == hoverprev:
        if turn == 1:
            canvas.create_oval(154 * hover + 1,
                               720 - 120 * j - 1,
                               154 * (hover + 1) - 1,
                               720 - 120 * (j + 1) + 1,
                               fill='#9e443e')
            canvas.create_oval(154 * hoverprev,
                               720 - 120 * jprev,
                               154 * (hoverprev + 1),
                               720 - 120 * (jprev + 1),
                               fill='#3244a8')
        else:
            canvas.create_oval(154 * hover + 1,
                               720 - 120 * j - 1,
                               154 * (hover + 1) - 1,
                               720 - 120 * (j + 1) + 1,
                               fill='#948f46')
            canvas.create_oval(154 * hoverprev,
                               720 - 120 * jprev,
                               154 * (hoverprev + 1),
                               720 - 120 * (jprev + 1),
                               fill='#3244a8')
        hoverprev = hover
        jprev = j


def click(event):
    global ROBOT
    global hoverprev
    global jprev
    global turn
    global number
    if button.winfo_exists():
        button.destroy()
        ROBOT=False
    hover = int(event.x / 154)
    if ROBOT==True:
        if turn==-1:
            hover=number
    j = int(currentstatecount[hover])
    if j > 5:
        return
    currentstate[(5 - j), hover] = turn
    if turn == 1:
        canvas.create_oval(154 * hover + 1,
                           720 - 120 * j - 1,
                           154 * (hover + 1) - 1,
                           720 - 120 * (j + 1) + 1,
                           fill='red')
    else:
        canvas.create_oval(154 * hover + 1,
                           720 - 120 * j - 1,
                           154 * (hover + 1) - 1,
                           720 - 120 * (j + 1) + 1,
                           fill='yellow')
    currentstatecount[hover] += 1
    j += 1

    if ROBOT==True:
        if turn == -1:
            canvas.create_oval(154 * int(event.x / 154) + 1,
                               720 - 120 * currentstatecount[int(event.x / 154)] - 1,
                               154 * (int(event.x / 154) + 1) - 1,
                               720 - 120 * (currentstatecount[int(event.x / 154)] + 1) + 1,
                               fill='#9e443e')
    else:
        if turn == 1:
            canvas.create_oval(154 * hover + 1,
                               720 - 120 * j - 1,
                               154 * (hover + 1) - 1,
                               720 - 120 * (j + 1) + 1,
                               fill='#948f46')
        else:
            canvas.create_oval(154 * hover + 1,
                               720 - 120 * j - 1,
                               154 * (hover + 1) - 1,
                               720 - 120 * (j + 1) + 1,
                               fill='#9e443e')
    jprev = j
    turn *= (-1)

    if checkwin(6 - j, hover,currentstate):
        for k in checkwin(6 - j, hover,currentstate):
            drawwin(k, event)
        label = tk.Label(window,
                         text=("GG " + ("RED" if turn == -1 else "YELLOW") +
                               " won"),
                         font=("Arial", 40))
        label.pack()
        canvas.create_oval(154 * hover + 1,
                           720 - 120 * j - 1,
                           154 * (hover + 1) - 1,
                           720 - 120 * (j + 1) + 1,
                           fill='#3244a8')
        window.unbind('<Motion>' )
        window.unbind('<Button-1>')
        return
    hoverprev = hover
    if ROBOT==True:
        if turn==-1:
            bmove(event)
    print(currentstate)

def bmove(event):
    global number
    number=bot()
    click(event)

def checkopp(x,arr1,arr2):
    global depth
    value=[]
    r=arr1.copy()
    r2=arr2.copy()
    depth -= 1
   # print("r= ",r)
    if r2[x] == 6:
        return (0)

    r[int(5-r2[x]),x]=1
    r2[x]+=1

    if checkwin(int(6-r2[x]),x,r):
        return (-10)

    tempstrong=0
    if depth>0:
        for i in range(7):
            tempstrong+=fakemove(x,r,r2)
        return(tempstrong)
    else:
        return (1)/((depthF-depth)**6)


def fakemove(x,arr1,arr2):
    global depth
    value=[]
    currentdepth=depth
    temp = arr1.copy()
    tempcount = arr2.copy()
    if tempcount[x] == 6:
        return(0)

    temp[int(5-tempcount[x]),x]=-1
    tempcount[x]+=1
    if checkwin(int(6-tempcount[x]),x,temp):
        #print("temp= ", temp)
        return 10/((depthF-depth)**6)
    tempstrong=0
    for i in range(7):
        strength=(checkopp(i,temp,tempcount))
        if strength==-100:
            return(-100)
        tempstrong+=strength
        depth=currentdepth

    return tempstrong


def bot():
    movestrong=[]
    global strong
    global depth
    for i in range(7):
        strong=fakemove(i,currentstate,currentstatecount)
        if strong==0:
            strong=-9999
        movestrong.append(strong)
        print(movestrong)
        strong=0
        depth=depthF-1
    return movestrong.index(max(movestrong))



def funcb(event):
    global ROBOT
    button.destroy()
    ROBOT=True
    print("robot")
    click(event)

window = tk.Tk()
window.title("connect4")
window.geometry("1080x760")
button =tk.Button(window, text="Play With Bot")
button.bind("<Button-1>", funcb)
button.pack()
canvas = tk.Canvas(window, width=1080, height=720, bg="blue")
canvas.pack()

for i in range(6):
    canvas.create_rectangle(0, 120 * i, 1080, 120 * i, outline="dark blue")
    for j in range(7):
        canvas.create_oval(154 * j,
                           120 * i,
                           154 * (j + 1),
                           120 * (i + 1),
                           fill="#3244a8")
        canvas.create_rectangle(154 * (j + 1),
                                0,
                                154 * (j + 1),
                                720,
                                outline="black")
window.bind('<Motion>', displaymove)
window.bind('<Button-1>', click)
window.mainloop()
