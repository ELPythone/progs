from random import randint
#creating roulette values-----------
ma=[]
i=0
while i < 36:
 i+=1
 ma.append(i)
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
red = []
i=1


while i<=36:
 if i not in black:
        red.append(i)
        i+=1
 else: 
        i+=1

#---------------------------------
#gameplay
def color_ch():
    global clrch
    clrch = input('[r]ed/[b]lack?\n')
    tree2()

def number_ch():
    global nch
    nch = input('Number?(1-36)\n') 
    tree2()
    
def qty():
    global q
    q = input('How much money do you bet?\n')

global bank
bank = 1000

def roll():
   global x 
   x = randint(0, 37)
   return x
    
def nbr_4ek():
    global n4
    if x==nch:
        n4 = 't'
    else: 
        n4 = 'f'
    nbrcash()


def clr_4ek():
    global c4
    c4 = 'f'
    if x in red and clrch == 'r':
        c4 = 't'
    elif x in black and clrch == 'b':
        c4 = 't'
    else:
            c4 = 'f'
    clrcash()

def tree2():
    print('Your money: '+ str(bank))  
    if ch == 'c':
        clr_4ek()
    elif ch == 'n':
        nbr_4ek()



def tree():
    roll()
    qty()
    global ch
    ch = input('bet on [c]olor \nbet on [n]umber\n')
    if ch == 'c':
        color_ch()
    elif ch == 'n':
        number_ch()

def nbrcash():
    if n4== 't':
        global bank
        bank+= int(qty())*5
        print(x)
        print('You win!\n Your money: '+ str(bank))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            tree()
    else:
        bank-=int(q)
        print(x)
        print('You lost!\n Your money: '+ str(bank))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            tree()

def clrcash():
    if c4== 't':
        global bank
        bank += int(q)
        print(x)
        print('You win!\n Your money: '+ str(bank))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            tree()
        else:
            tree()
    elif c4 == 'f':
        bank-=int(q)
        print(x)
        print('You lost!\n Your money: '+ str(bank))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            tree()
    
def menu():
    b = input('[s]tart game\n[e]xit: \n ')
    if b == 's':
        tree()
    
menu()
