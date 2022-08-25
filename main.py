User = 0,0,0

import sys
import random as rn

try:
    UserInput = int(input('Pls Entery Your number: '))

except ValueError:
    print('You can\'t use Any Symbole and String')
    sys.exit()


while True:

    N = -1
    X = User[0]
    y = User[1]
    z = User[2]
    threeDimintonal = 3

    if threeDimintonal == 3:
        X = int(input('Input Your datasets: '))
        y = int(input ("Input Enter Your Target Variable: "))

        if X >= UserInput:
            print('you can\'t put Number in X Larger UserInput')
            sys.exit()
            break

        elif y >= X:
              print(f'you can\'t put Number in y Larger X', y)
              break
        elif y == 0:
         print('your target variable is 0')
         y = int(input("Input Enter Your Target Variable: "))

        else:
            pass

        Z = print('Your Shape: \n', 'Datasets: ',X , '\n','Target Variable: ',y)

        print('==========Pls Select Number Options========== \n'
              ' 1: Loop Your Target Variable, \n'
              ' 2: Change Your X, \n'
              ' 3: Change Your Target Variable,\n','4: Calculate your X and y, \n'
               '5 Exit ')
        UserInput = int(input('Pls Entery Number Options: '))
        def TargetLoop():
            pass
        def ChangeX():
            pass
        def Changey():
            pass
        def CalcZ():
            pass
        if UserInput == 1:
            TargetLoop()

        elif UserInput == 2:
            pass

        elif UserInput == 3:
            ChangeX()

        elif UserInput == 4:
            Changey()

        elif UserInput == 5:
            message = ['GoodBey','See you later','Bey']
            print(rn.choice(message))
            sys.exit()

        else:
            print(1)
