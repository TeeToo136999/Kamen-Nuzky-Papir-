import time
import os


def kvadr(DN):
    try:
        a = int(input('Zadej velikost strany a: '))
        b = int(input('Zadej velikost strany b: '))
        c = int(input('Zadej velikost strany c: '))
        if DN == 'V':
            return f'Objem kvádru je {a * b * c}'
        elif DN == 'S':
            return f'Obsah kvádru je {2 * (a * b + b * c + c * a)}'
    except:
        return "Neplatná hodnota"


def licho(DN):
    try:
        if DN == 'S':
            a = int(input('Zadej velikost strany a: '))
            c = int(input('Zadej velikost strany c: '))
            v = int(input('Zadej velikost výšky v: '))
            return f'Obsah lichoběžníku je {v * (a + c) / 2}'
        elif DN == 'O':
            a = int(input('Zadej velikost strany a: '))
            b = int(input('Zadej velikost strany b: '))
            c = int(input('Zadej velikost strany c: '))
            d = int(input('Zadej velikost strany d: '))
            return f'Obvod lichoběžníku je {a + b + c + d}'
    except:
        return "Neplatná hodnota"


def main():
    print('Co chcete vypočítat?')
    print('1 >> Objem kvádru')
    print('2 >> Obsah kvádru')
    print('3 >> Obsah lichoběžníku')
    print('4 >> Obvod lichoběžníku')

    Input = input('Chci vypočítat: ')
    if Input == "1":
        print(kvadr('V'))

    elif Input == "2":
        print(kvadr('S'))

    elif Input == "3":
        print(licho('S'))

    elif Input == "4":
        print(licho('O'))
    else:
        print("Neplatná hodnota")
    time.sleep(3)
    os.system('cls')
    main()


if __name__ == '__main__':
    main()
