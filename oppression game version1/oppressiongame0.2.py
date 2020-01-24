from tkinter import *
#from playsound import playsound
import sys
import os
import playsound
import pygame
import time
import  tkinter.messagebox


def doNothing():
    print("function")
root= Tk()
menu=Menu(root)
root.config(menu=menu)
subMenu= Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project...",command=doNothing())
subMenu.add_command(label="New...",command=doNothing())
subMenu.add_separator()
#**************
subMenu.add_command(label="Login",command=doNothing())
subMenu.add_command(label="New...",command=doNothing())
subMenu.add_separator()
#8888888888888registration
subMenu.add_command(label="Show account",command=doNothing())
subMenu.add_command(label="New...",command=doNothing())
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing())
root.geometry("900x900")
root.title("Oppression Game")
photo=PhotoImage(file="titled.png")
label= Label(root,image=photo)
label.pack()


print("Level one")
hp=3
mp2=5
ovl=hp+mp2
print(ovl)
"""
secured
enter exit hacker
tab 
charcters= ['ric' ,
         'cas',
         'greeen'
         ]

"""
a= 1+ 2 + \
   4 +5+6 +\
   + 1 + 1
print(a)
#this is single comment

'''j
l
'''
sstin="This is string "                                                            
print(int(10.20))

print(sstin)
sstin="youre being attacked by imperial guards  "
exNum1=-5
print(abs(exNum1))
print(sstin)



exList=[5,2,1,6,7,8]
largest= max(exList)
print("you defeated")

print(largest)
print("guards")
smallest= min(exList)
print(smallest)
root.mainloop()

#root.close()

#root.quit() #doesnt stop use when work after
#root.destroy() use at end
x=5.622
x=round(x)
print(x)

y=2.256
y=round(y)
print(y)

a= input("enter value  of health portions1 ")
b= input("enter valueof revive ")
l=a+b
print("you r level")
print(l)

#root.destroy()
a1= float(input("enter value 1 "))
b1= float(input("enter value 2 "))
c1=a+b
#print(c1)
x=str(c1)
print(x)
print("You wake up in abandoned lab, waves of android corpses lay in the area")
#playsound.playsound('you-must-live.mp3')
pygame.init()

pygame.mixer.music.load("b.mid")

pygame.mixer.music.play(4,0)
#pygame.mixer.music.play(4,0)

time.sleep(15)
#play(loops=0, maxtime=0, fade_ms=0) -> Channel
root=Tk()
photo=PhotoImage(file="sewage1.png")
label= Label(root,image=photo)
label.pack()

root.mainloop()

#playsound('you-must-live.mp3')
#root.quit()


print( "You decided to walk")
for number in range(5):
 print("Walked in steps ")
 x = 'System files upload'
y = {1:'a',2:'b'}
print(" the computers systems file have to be uploaded to move forward")
    
      
print('H'in x)
print(1 in y)
n=1
m=2
l=3
num=0
num1=6
while (num < 10):
# function doesnt work without num1 loop keeps on going in pi and idle

    num=num1
    a2 = input("switch board panel ")
    if a2 == '1':
        print("door shifted to the right")
        num1 += 1

    elif a2 == '2':
                 print("door shifted to the left")
                 num1 -= 1

    elif a2 == '3':
                print("growling noise")
                num *= 2
                break;
#used break on just to stop the loop forever
    elif num1=='10':
        #doesnt work without this one
                break;
    else:
             print("Youre trapped")
             num += 1

'''
while(num <10):
                a2= input("switch board panel ")
                if a2==n:
                    print("door shifted to the right")
                    num+=1
         
         
               elif a2==m:  
                    print("door shifted to the left")
                    num-=1
            
               elif a2==l:
                   num*=2
             
               else:
               print("Youre trapped")

'''
print("You have escaped")
pygame.mixer.music.stop()
print("but rebel leader arrived")
#pygame.mixer.music.load("f:/Gamesandstudy19summer/oppression game/advanceon.mp3")
#No music system works root.quit() doesnt work,,,.,..,
#pygame.mixer.music.play()
#time.sleep(10)
os.system("advancedon.m4a")
root=Tk()
photo=PhotoImage(file="dolores.png")
label= Label(root,image=photo)
label.pack()

root.mainloop()

def jeff():
        
    print('quick attack the enemy press a to attack b to block c for super ')
    bob=10
    alice=60
    turn1=0
    turn2=2
    spr=5
    mod1=0
    mod2=0
    speed=0

    c1=print('bob health is ',bob)
    c2=print('alice health is ',alice)
    print(c1,c2)
    while(alice>0):
        
        print(spr,'spr is')
        print('bob health is ',bob)
        print('alice health is ',alice)
        a4=input("a to attack b to block c for super")
        if a4=='a':
            print('bob attacks alice')
            alice-=10
            turn1+=1
            spr+=1
            mod1=turn1%2
            print('bob health is ',bob)
            print('alice health is ',alice)

            if mod1 > 0:
                print("Alice counter attacks")
                bob-=1
                spr+=1
                speed-=1
                print('bob health is ',bob)
                print('alice health is ',alice)

            else:
                print("successful attack")
                print('bob health is ',bob)
                print('alice health is ',alice)

        elif bob < 0:
                print('''game over Bob died
                        press 1 to continue anything else to
                        quit''')
                a5= input("1 or quit")
                if a5 == '1' :
                        jeff()
                else:
                        sys.exit(0)
                #break            
        elif a4=='b':
            print('Bob blocks')
            if speed=='0':
                print('Block unsucessful')
                bob-=2
                print('bob health is ',bob)
                print('alice health is ',alice)

            speed+=1
            turn2+=1
            spr+=1
            mod2=turn1%2
            
            print('bob health is ',bob)
            print('alice health is ',alice)

            if mod2>0:
                print('Bob counterattacks')
                alice-=10
                spr+=1
                print('bob health is ',bob)
                print('alice health is ',alice)
        elif(a4=='c'):
                if spr != 0 :#have to be un quoted
                        print('super attack')
                        alice-=15
                        spr=0
                        speed=0
                        print(spr,'spr is')
                else:
                        print("No super attack charge up")
                        print("alice attacks")
                        bob-=1
                        speed+=1
                        turn1+=1
                        turn2+=1
        
        else:
                print("please select a proper option")
                turn1+=1
                mod1=turn1%2
                if mod1 >0 :
                        print('recovered 2 HP')
                        bob+=2
                        mod1=turn2
                        turn1=turn2
                        turn2=mod1
                        print('bob health is ',bob)
                        print('alice health is ',alice)
            
                                
                 
                
                      
                
        
jeff()


a3=input("QUICK DRAW YOU gun and shoot 1 for left and 2 for right")
if a3 == '1':
    print("you died")
elif a3 == '2':
    print("You killed rebel leader and escaped the facility")
else:
    print("a swordsman appeared and killed the guard and took  your character out")
    a = """
    A rebellion is rising                                  
    i neeed your help
    Then you followed him
    """
    print(a)



print("game over")
try:
    os.system('level2.py')
        #fh=open('pin.txt')
except IOError as e:
        print('Could not open file')
else:
    print("opened file")
#

"""
                    if a3=='1':
                    print("you died")

                elif a3=='2':
                                print("You killed rebel leader and escaped the facility")
                else:
                        print("a swordsman appeared and killed the guard and took your character out")
                        a="""
'''
                        A rebellion is rising
                        i neeed your help
                         Then you followed him
                         """
print("game over")
    """
   '''     
root=Tk()
photo=PhotoImage(file="bi.png")
label= Label(root,image=photo)
label.pack()

root.mainloop()


'''

 #!/usr/bin/python
import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('SendEmail.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()

'''

































