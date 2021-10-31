""" Program to compare second hand cars by mileage, model and price.
"""

from datetime import datetime as dt
from typing import MutableMapping
today = dt.today().year

# ################################ SETTINGS ####################################

MILES   = {'good': 0,      'bad': 100000 }
MODEL   = {'good': today,  'bad': today-5}
PRICE   = {'good': 0,      'bad': 40000  }

WEIGHT  = {'MI': 5, 'MO': 3, 'PR': 2}

################################################################################

_TOP = sum(WEIGHT.values())
_MI = (WEIGHT['MI']*100/_TOP)
_MO = (WEIGHT['MO']*100/_TOP)
_PR = (WEIGHT['PR']*100/_TOP)

class Auto:
    def __init__(self, name, mil, mod, prc):
        self.name = name
        self.mil = self._score(*MILES.values(),mil)
        self.mod = self._score(*MODEL.values(),mod)
        self.prc = self._score(*PRICE.values(),prc)

    def score(self):
        scr = (
                ( 
                      self.mil * _MI
                    + self.mod * _MO
                    + self.prc * _PR
                )   / 100
            )
        return scr

    def _score(self, maxi, mini, x):
        perc = (x-mini)*100/(maxi-mini)
        return perc

    def __str__(self):
        return self.name
        

def comparar(cars):
    print('\n\n')
    for car in cars:
        nom = car.name
        mil = car.mil
        mod = car.mod
        prc = car.prc
        print(
        f'{nom} scores:\n\tKms => {mil}\n\tModel => {mod}\n\tPrice => {prc}'
        )
    print()
    for car in cars:
        print(f'{car} score: {car.score()}')

if __name__ == '__main__':

    print(
          "\nLet's consider the following comparison parameters:")
    print(f"Mileage -\tBest: {MILES['good']:<8} Worst: {MILES['bad']}")
    print(f"Model   -\tBest: {MODEL['good']:<8} Worst: {MODEL['bad']}")
    print(f"Price   -\tBest: {PRICE['good']:<8} Worst: {PRICE['bad']}")
    print('\nAnd they have the following weight:')
    print(f"Miles: {_MI}%, Model: {_MO}%, Price: {_PR}%\n")
        
    if input('Do you want to redefine the parameters? (y/any): ')[0] == 'y':
        print("\n")
        MILES['good'] = int(input('How much would be the best mileage? '))
        MODEL['good'] = int(input('Which would be the best (year)? '))
        PRICE['good'] = int(input('How much would be the best price? '))
        while (bad:= int(
                    input('How much would be the worst mileage? ')
                )) <= MILES['good']:
            print(f"This value sould be grather than {MILES['good']}")
        MILES['bad'] = bad
        while (bad:= int(
                    input('Which would be the worst (year)? ')
                )) >= MODEL['good']:
            print(f"This year sould be older than {MODEL['good']}")
        MODEL['bad'] = bad
        while (bad:= int(
                    input('How much would be the worst price? ')
                )) <= PRICE['good']:
            print(f"This value sould be grather than {PRICE['good']}")
        PRICE['bad'] = bad
        print('\nDefine they weight:\n')
        WEIGHT['MI'] = int(input('Miles: '))
        WEIGHT['MO'] = int(input('Model: '))
        WEIGHT['PR'] = int(input('Price: '))

        _TOP = sum(WEIGHT.values())
        _MI = (WEIGHT['MI']*100/_TOP)
        _MO = (WEIGHT['MO']*100/_TOP)
        _PR = (WEIGHT['PR']*100/_TOP)

        print(
          "\nSo, Let's consider the following comparison parameters:")
        print(f"Mileage -\tBest: {MILES['good']:<8} Worst: {MILES['bad']}")
        print(f"Model   -\tBest: {MODEL['good']:<8} Worst: {MODEL['bad']}")
        print(f"Price   -\tBest: {PRICE['good']:<8} Worst: {PRICE['bad']}")
        print('\nAnd they have the following weight:')
        print(f"Miles: {_MI}%, Model: {_MO}%, Price: {_PR}%")

    cars = []
    cond = 'y'
    while cond[0] == 'y':
        print("\n")
        cars.append(
            Auto(
                name:= input('Enter Car Name: '),
                int(input(f'Enter {name} Mileage: ')),
                int(input(f'Enter {name} Model: ')),
                int(input(f'Enter {name} Price: '))
            )
        )
        
        cond = input('Add another Car? (y/any) ')

    comparar(cars)

    input('\n\nPress Enter to exit. ')
