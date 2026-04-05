#### Yours -> Right    | Opponent -> Left
#### Yours -> Left     | Opponent -> Middle
#### Yours -> Middle   | Opponent -> Right
import random

desk = {1: 'left [X][][]', 2: 'middle [][X][]' , 3: 'right [][][X]'}
randint = random.randint(1,3)

player = desk[randint]
opponent = desk[randint+1 if not randint+1 > 3 else 1]

print(f'Player {player} -- Opponent {opponent}')