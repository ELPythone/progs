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

class Bet():
    def __init__(self, q, n, clr):
        self.q = q
        self.n = n
        self.clr = clr
    def color():
        clr = input('[r]ed/[b]lack?\n')
        return clr
    def number():
        n = input('Number?(1-36)\n') 
        return n
    def qty():
        q = input('How much money do you bet?\n')
        return q


class bank():
    def __init__(self, nalik):
        self.nalik = nalik

cs = bank(1000)

def roll():
    x=randint(0, 37)
    return x
    
def nbr_4ek():
    c = False
    if roll()==Bet.number():
        c = True
    else: 
        c = False
    return c

def clr_4ek():
    c = False
    if roll() in red and Bet.color() == 'r':
        c = True
    elif roll() in black and Bet.color == 'b':
        c = False
    return c
    
def tree2():
    print('Your money: '+ str(cs.nalik))
    l = tree()   
    if l == 'c':
        clr_4ek()
    elif l== 'n':
        nbr_4ek()
    return l

def tree():
    Bet.qty()
    ch = input('bet on [c]olor \nbet on [n]umber\n')
    if ch == 'c':
        Bet.color()
    elif ch == 'n':
        Bet.number()
    return ch
def cash():
    if nbr_4ek or clr_4ek:
        cs.nalik += int(Bet.qty())
        print(roll())
        print('You win!\n Your money: '+ str(cs.nalik))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            loop()
        
    else:
        cs.nalik-=int(Bet.qty())
        print('You lost!\n Your money: '+ str(cs.nalik))
        f = input('\nPlay again?[y/n]\n')
        if f == 'y':
            loop()
        
def menu():
    b = input('[s]tart game\n[e]xit: \n ')
    loop()

def loop():
    tree2()
    cash()
menu()
