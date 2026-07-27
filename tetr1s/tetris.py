import random
import tkinter as tk
import numpy as np
import copy
import time
import pygame
pygame.mixer.init()
speed=0.3
block=[[]]
nextblock=[0,0,0,0,0,0,0]
score=0
currentblocks=np.zeros((20,10))
finstate=[]
tempstate=[]
blinkstate=[]
clearing=False
lostg=False
colors = ['#ad0a36', '#700622','#0051c9','#0c326b','#169605','#17610e','#7d0bba','#4a1269','#039c82','#0f6355','#9ba105','#6a6e12']
click = pygame.mixer.Sound("move.wav")
explosion = pygame.mixer.Sound("rotate.wav")
clean=pygame.mixer.Sound("clean.wav")
land=pygame.mixer.Sound("land.wav")
falld=pygame.mixer.Sound("falld.wav")
over=pygame.mixer.Sound("over.mp3")
def checkline():
    global score
    global currentblocks
    global finstate
    global blinkstate
    global tempstate
    global clearing
    global animtime
    global speed
    sums=(np.sum(np.sign(currentblocks),axis=1))
    fulls=[]
    slic=[]
    tempstate=copy.deepcopy(currentblocks)
    blinkstate=copy.deepcopy(currentblocks)
    for i in range(20):
        #print(sums[i])
        if sums[i]==10:
            fulls.append(i)
            tempstate[i]=0
            slic.append(tempstate[i])
    if len(fulls)>0:
        clearing = True
        score+=1
        clean.play()
        finstate=np.delete(tempstate,fulls,axis=0)
        finstate=np.vstack([slic,finstate])
        currentblocks = tempstate
        animtime=time.time()
        speed=0.05
        return True
    return False
def checkleft():
    global block
    for i in block:
        if type(i) is int:
            break
        if i[1]==0 or (currentblocks[i[0],i[1]-1]!=0 and not currentblocks[i[0],i[1]-1]>9):
            return False
    return True
def checkright():
    global block
    for i in block:
        if type(i) is int:
            break
        if i[1]==9 or (currentblocks[i[0],i[1]+1]!=0 and not currentblocks[i[0],i[1]+1]>9):
            return False
    return True
def movement(event):
    global device2
    global speed
    if clearing or lostg:
        return
    pressed=event.keysym
    if pressed=="Left":
        if checkleft():
            click.play()
            for i in block:
                if type(i) is int:
                    break
                currentblocks[i[0],i[1]]=0
                i[1]-=1
            for i in block:
                if type(i) is int:
                    break
                currentblocks[i[0],i[1]]=block[5]
    elif pressed=="Right":
        if checkright():
            click.play()
            for i in block:
                if type(i) is int:
                    break
                currentblocks[i[0],i[1]]=0
                i[1]+=1
            for i in block:
                if type(i) is int:
                    break
                currentblocks[i[0],i[1]]=block[5]
    elif pressed=="Down":
        speed=0.01
    elif pressed=="Up":
        for i in block:
            if type(i) is int:
                break
            currentblocks[i[0], i[1]] = 0
        rotcheck()
        for i in block:
            if type(i) is int:
                break
            currentblocks[i[0], i[1]] = block[5]

    draw()
def rotcheck():
    global block
    tempblock=copy.deepcopy(block)
    if block[4]==3:
        return True
    elif block[4]==0:
        if tempblock[2][1]<2:
            temp =tempblock[2][1]
            for i in tempblock:
                if type(i) is int:
                    break
                i[1]+=(2- temp)
        elif tempblock[2][1]==9:
            for i in tempblock:
                if type(i) is int:
                    break
                i[1]-=1
    else:
        if tempblock[1][1]==0:
            for i in tempblock:
                if type(i) is int:
                    break
                i[1]+=1
        elif tempblock[1][1]==9:
            for i in tempblock:
                if type(i) is int:
                    break
                i[1]-=1
    rotate(tempblock)
    for i in tempblock:
        if type(i) is int:
            break
        #print(currentblocks[i[0],i[1]])
        if currentblocks[i[0],i[1]]!=0 and currentblocks[i[0],i[1]]<9:
            #print("here")
            return
    #print("NN")
    explosion.play()
    block=tempblock
    return
def rotate(block):
    if block[4]==0:
        if block[6]==0:
            #print("AA")
            for i in block:
                if type(i) is int:
                    break
                i[1] = block[2][1] - (block[2][0] - i[0])
                i[0]=block[2][0]

            block[6]=1
        elif block[6]==1:
            for i in block:
                if type(i) is int:
                    break
                i[0]=block[2][0]-(block[2][1] - i[1])
                i[1]=block[2][1]
            block[6]=0
    elif block[4]==3:
        return
    else:
        for i in block:
            if type(i) is int:
                break
            temp = i[1]
            i[1] = block[1][1] - (i[0] - block[1][0])
            i[0] = block[1][0] + (temp - block[1][1])
def checkplace():
    global block
    global speed
    for i in block:
        if type(i) is int:
            break
        if i[0]==19 or (currentblocks[i[0]+1,i[1]]!=0 and not currentblocks[i[0]+1,i[1]]>9):
            for r in block:
                if type(r) is int:
                    break
                currentblocks[r[0],r[1]]=(block[5]-10)
            speed=0.3
            land.play()
            return True
    return False
def movedown():
    global block
    if clearing or lostg:
        return
    if checkplace() and checkline():
        return
    elif checkplace():
        spawnblock(random.randint(0, 6), random.randint(1, 6))
        return
    for i in block:
        if type(i) is int:
            break
        currentblocks[i[0],i[1]]=0
        i[0] = i[0] + 1
    for i in block:
        if type(i) is int:
            break
        currentblocks[i[0],i[1]]=(block[5])
    draw()
#a-[0,1,2,3,4,5,6]-[line,Lmirror,L,square,Zmirror,T,Z]
def spawnblock(a,b):
    global score
    global block
    global nextblock
    global currentblocks
    print(score)
    block=copy.deepcopy(nextblock)
    nextblock=[]
    if a == 0:
        nextblock.append([0, 4])
        nextblock.append([1, 4])
        nextblock.append([2, 4])
        nextblock.append([3, 4])

    elif a == 1:
        nextblock.append([0, 5])
        nextblock.append([1, 5])
        nextblock.append([2, 5])
        nextblock.append([2, 4])
    elif a == 2:
        nextblock.append([0, 4])
        nextblock.append([1, 4])
        nextblock.append([2, 4])
        nextblock.append([2, 5])
    elif a == 3:
        nextblock.append([0, 5])
        nextblock.append([0, 4])
        nextblock.append([1, 5])
        nextblock.append([1, 4])

    elif a == 4:
        nextblock.append([0, 5])
        nextblock.append([1, 5])
        nextblock.append([0, 6])

        nextblock.append([1, 4])

    elif a == 5:
        nextblock.append([0, 5])
        nextblock.append([1, 5])
        nextblock.append([1, 4])
        nextblock.append([1, 6])
    elif a == 6:
        nextblock.append([0, 5])
        nextblock.append([1, 5])
        nextblock.append([0, 4])

        nextblock.append([1, 6])
    for i in nextblock:
        if currentblocks[i[0],i[1]]!=0:
            lost()
            return
    for i in block:
        if type(i) is int:
            break
        currentblocks[i[0],i[1]]=block[5]
    nextblock.append(a)
    nextblock.append(b+10)
    nextblock.append(0)
    draw()
def draw():
    canvas.delete("all")
    canvas.create_line(199, 0, 199, 800, fill='white', width=2)
    canvas.create_line(602, 0, 602, 800, fill='white', width=2)
    for i in range(9):
        canvas.create_line(240+i*40, 0, 240+i*40, 800, fill='#1a0138', width=1)
    for i in nextblock:
        if type(i) is int:
            break
        canvas.create_rectangle(485 + i[1] * 40, i[0] * 40 + 61, 523 + i[1] * 40,
                                i[0] * 40 + 99, fill=colors[2*(nextblock[5]-10)-2])
        canvas.create_rectangle(492 + i[1] * 40, i[0] * 40 + 68, 516 + i[1] * 40,
                                i[0] * 40 + 92, fill=colors[2*(nextblock[5]-10)-1])
    canvas.create_image(690, 35, image=img2)
    for i in range(200):
        k=currentblocks[int(i/10),i%10]
        if currentblocks[int(i/10),i%10]>9:
            k=int(currentblocks[int(i/10),i%10]-10)
        if k==0:
            canvas.create_rectangle(201+(i%10)*40,int(i/10)*40+1,239+(i%10)*40,int(i/10)*40+39,fill='#34026e')
        else:
            canvas.create_rectangle(201+(i%10)*40,int(i/10)*40+1,239+(i%10)*40,int(i/10)*40+39,fill=colors[int(2*k-2)])
            canvas.create_rectangle(208+(i%10)*40,int(i/10)*40+8,232+(i%10)*40,int(i/10)*40+32,fill=colors[int(2*k-1)])


    return
def main():
    if tick():
        #print("mobve")
        if not clearing:
            movedown()
        else:
            animate()
    window.after(10, main)
def animate():
    global clearing
    global speed
    global currentblocks
    #print(animtime-time.time())
    if time.time()-animtime<0.4 and time.time()-animtime>0.2:
        currentblocks=blinkstate
    elif time.time()-animtime<0.6:
        currentblocks=tempstate
    elif time.time()-animtime<0.8:
        currentblocks=blinkstate
    elif time.time()-animtime<1:
        currentblocks=tempstate
    elif time.time()-animtime>1:
        falld.play()
        currentblocks=finstate
        clearing = False
        speed = 0.3
        spawnblock(random.randint(0,6),random.randint(1,6))

    draw()
def lost():
    global lostg
    canvas.create_image(400,300,image=img)
    lostg=True
    pygame.mixer.music.stop()
    over.play()
    return
def tick():
    global prevtime
    if time.time() - prevtime > speed:
        prevtime=time.time()
        return True
    else:
        return False
def released(event):
    if clearing:
        return
    global speed
    speed=0.3
prevtime=time.time()
animtime=time.time()
window=tk.Tk()
window.geometry('800x800')
window.title('tetris')
canvas=tk.Canvas(window,width=800,height=800,bg='black')
canvas.pack()
img=tk.PhotoImage(file="img.png")
img2=tk.PhotoImage(file="nextb.png")
window.bind("<KeyPress>",movement)
window.bind("<KeyRelease>",released)
spawnblock(random.randint(0,6),random.randint(1,6))
spawnblock(random.randint(0,6),random.randint(1,6))
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
window.after(10,main)
window.mainloop()
