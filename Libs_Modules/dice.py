from typing import List
import random
import sys


def menu(entries : List) -> int:
    maxLen = len(entries) + 1
    while True:
        print('\nMENU')
        print('----')
        for num, label in enumerate(entries):
            print(f'{num + 1:2} - {label}')
        print(' 0 - Quitter')
        try:
            choice = int(input('\nVotre choix :'))
            if choice < 0 or choice > maxLen:
                raise Exception()
            return choice
        except:
            print('Choix invalide !')


def dice(n : int) -> int:
    print(f'Résultat : {random.randint(1, n)}')


if __name__ == '__main__':
    print('Petit script de test !')
    while True:
        n = menu(('Lancer un D4', 'Lancer un D6', 'Lancer un D8', 'Lancer un D12', 'Lancer un D20'))
        if n == 0:
            print('Au revoir')
            sys.exit(0)
        if n == 1:
            dice(4)
        elif n == 2:
            dice(6)
        elif n == 3:
            dice(8)
        elif n == 4:
            dice(12)
        elif n == 5:
            dice(20)
        
