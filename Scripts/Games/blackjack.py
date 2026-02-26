import random

player      = 0
playerTable = 0
pBank       = 5000

dealer      = 0
dealerTable = 0
dBank       = 5000

bid         = 0


# stand - hit - bust (over) - ace is 1 or 11 - natural blackjack (start 21) - 2nd dealer card face down

def checkAce(card):
    if card in(1, 11):
        while True:
            try:
                card = int(input("Choose Ace value 1/11: ").strip())
                break
            except Exception as e:
                print(f'Error {e}. Choose a valid value')

    return card

def hit(requester):
    
    wantToHit= str(input("Hit or Pass: y/n ")).strip().lower()

    if wantToHit in ('y', 'yes'):
        draw = random.randint(1, 11) 

        checkAce(draw)

        if requester == "player":
            global playerTable
            playerTable += draw
        elif requester == "dealer":
            global  dealerTable
            dealerTable += draw

    elif wantToHit in ('n', 'no'):
        global turn
        turn = False
    return turn


def startingHand():

    card1   = random.randint(1, 11)
    card2   = random.randint(1, 11)

    print(f'Starting hand: {card1,card2}')

    if card1+card2 == 21:
        print(f'Natural Black Jack')
    else: 
        card1   = checkAce(card1)
        card2   = checkAce(card2)

    return card1, card2


pStartingHand   = startingHand()
# dStartingHand   = startingHand()


print(f'Current hand: {pStartingHand}')
playerTable = pStartingHand[0] + pStartingHand[1]

turn = True

while turn:

    print(f'playerTable {playerTable}')

    if playerTable == 21:
        print(f'Black Jack!')
    elif playerTable < 21:
        hit("player")

    else:
        print(f'Busted: {playerTable}')
        break
    
