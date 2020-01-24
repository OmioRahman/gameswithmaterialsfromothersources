import sys
import os
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
            alice-=5
            turn1+=1
            spr+=1
            mod1=turn1%2
            print('bob health is ',bob)
            print('alice health is ',alice)

            if mod1 > 0:
                print("Alice counter attacks")
                bob-=5
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
                        bob-=13
                        speed+=1
                        turn1+=1
                        turn2+=1
                        if bob < 0:
                                print('''game over Bob died
                                press 1 to continue anything else to
                                quit''')
                        a5= input("1 or quit")
                        if a5 == '1' :
                                        jeff()
                        else:
                                sys.exit(0)
                        
        
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
