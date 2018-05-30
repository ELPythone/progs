from random import randint
#creating roulette values-----------
ma=[]
bank = 1000
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

def tree2():
    l = tree()   
    if l == 'c':
            print('dis shit working')
    elif l== 'n':
            print('syka blyat')


def tree():
    ch = input('bet on [c]olor \nbet on [n]umber\n')
    if ch == 'c':
        Bet.color()
    elif ch == 'n':
        Bet.number()
    return ch

def menu():
    b = input('[s]tart game\n[e]xit: \n ')
menu()
tree()

