import random
number=random.randint(0,20)
print('find random int')
e=number
str(e)
x='fi2121n21d321321 3213random 21321int3232131231248348328420 hereiii',str(e),'22321321312'
print("211 3124324324$#$#$#$#43213213123a384327481274&*@#@!*323 ".join(x))
flag=0
while flag==0:
    guess=int(input('Enter an i'))
    if guess== number:
        # new
        print ('Congrats right')
        print (number)
        print('(but you do not win)')
        flag=1
    elif guess< number:
        print('no its higher')
       
    else:
        print('No ,it is little lower than that')
        print (number)
print('Done')
