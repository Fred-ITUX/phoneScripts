import random

player  = 0
pBank   = 5000

dealer  = 0
dBank   = 5000

bid     = 0


# stand - hit - bust (over) - ace is 1 or 11 - natural blackjack (start 21) - 2nd dealer card face down

def hit():
    print(f'')

def checkAce(card):

    if card in(1, 11):
        try:
            while True:
                card = int(input("Choose Ace value 1/11: ").strip())
        except Exception as e:
            print(f'Error {e}. Choose a valid value')


def startingHand():

    card1 = random.randint(1, 11)
    card2 = random.randint(1, 11)

    print(f'Current hand: {card1, card2}')

    if card1 in(1, 11):
        card1 = int(input("Choose Ace value: 1/11"))
    if card2 in(1, 11):
        card2 = int(input("Choose Ace value: 1/11"))




pStartingHand   = startingHand()
dStartingHand   = startingHand()