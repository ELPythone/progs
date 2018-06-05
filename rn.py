from random import randint
def main():
    global x
    x = randint(1, 101)
    def game():
        print('Угадай число(1-100)\n')
        ch = input()
        if ch == str(x):
            print('Ты угадал. Играть снова?')
            c = input()
            if c == 'y':
                main()
        elif int(ch) == 228:
            print('Введен чит-код. Загаданное число: '+ str(x))
            game()
        elif int(ch) > x:
            print('Слишком много\r')
            game()
        elif int(ch) < x:
            print('Слишком мало')
            game()
    game()

main()
