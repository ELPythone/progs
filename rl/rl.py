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

"""
def bet():
    #lol=randint(0,36)
    q = input('how much will you bet?\n')
    ch= input('To bet on [c]olor \nTo bet on [v]alue\n')
    if ch =='c':
        clr = input('What color?(red,black)\n')
        return clr
    elif ch =='c':
        n = input('value(1-36):\n')
        return n
    return q
"""
class Bet():
    def __init__(self, q, n, clr):
        self.q = q
    def bet_color():
        clr = input('[r]ed/[b]lack?\n')
        return clr
       def bet_number():
           n = input('Number?(1-36)\n')


def start():
    print('you have: '+str(bank))
 


def menu():
    b = input('[s]tart game\n [e]xit: \n ')
    if b == 's':
        start()
menu()



