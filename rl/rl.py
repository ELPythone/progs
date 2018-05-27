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
c = True
#def check():


def bet():
 lol=randint(0,36)
 q = input('how much will you bet?\n')
 ch= input('Type: \n1.To bet on color \n2. To bet on value\n')
 if ch =='1':
  clr = input('What color?(red,black)\n')
  return clr
 elif ch =='2':
  n = input('type value(1-36)\n')
  return n
 return q
def start():
 print('you have: '+str(bank))
 bet()


def menu():
    b = input('type\' start\' to start a game,\n \'exit\' to exit: \n ')
    if b == 'start':
        start()
menu()
print(bet(q))

