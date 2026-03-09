import random

player      = 0
playerTable = 0
pBank       = 5000

dealer      = 0
dealerTable = 0
dBank       = 5000

bid         = 500
bidTable    = 0

game = 'On'


def checkAce(card):
    if card in(1, 11):
        while True:
            try:
                card = int(input("♠️ Choose Ace value 1/11: ").strip())
                break
            except Exception as e:
                print(f'Error {e}. Choose a valid value')

    return card



def hit():
    
    wantToHit= str(input("🎰 Hit or Pass: y/n ")).strip().lower()

    if wantToHit in ('y', 'yes', 'hit'):
        draw = checkAce(random.randint(1, 11))
        
        bidding(pBank, dBank, bid,"dealer")
        global playerTable
        playerTable += draw

    else: 
        global turn
        turn = False

    return turn


def startingHand():

    card1   = random.randint(1, 11)
    card2   = random.randint(1, 11)

    if card1+card2 == 21:
        print(f'\n💰 Player natural Black Jack. GGs {card1} {card2}')
    else: 
        card1   = checkAce(card1)
        card2   = checkAce(card2)

    return card1, card2




def dealerStart():
    dealer_card1   = random.randint(1, 11)
    dealer_card2   = random.randint(1, 11)

    if dealer_card1 in (1,11):
        dealer_card1 = 11

    if dealer_card2 in (1,11) and not dealer_card1 in (1,11):
        dealer_card2 = 11

    dealerTable = dealer_card1 + dealer_card2

    if dealerTable == 21:
        print(f'💰 Dealer natural Black Jack. GGs {dealer_card1} {dealer_card2}')
    else:
        print(f'🤖 Dealer 1st card: {dealer_card1}')

    return dealerTable


def dealerTurn(dealerTable):
    dealer_draw = random.randint(1, 11)

    bidding(pBank, dBank, bid,"dealer")

    if dealer_draw in (1, 11):
        if dealerTable + 11 < 21:
            dealer_draw = 11
        else:
            dealer_draw = 1

    dealerTable += dealer_draw
    return dealerTable


#### Each hit costs one bid
def bidding(pBank, dBank, bid, bidder):

    if bidder == 'player':
        pBank -= bid
        print(f"🏦 Player remaining funds: {pBank}")
        if pBank <= 0:
            print(f"💸 Player's bankrupt! 🏦 Dealer's remaining funds: {dBank}")
            game = 'Over'
    
    elif bidder == 'dealer':
        dBank -= bid
        print(f"🏦 Dealer remaining funds: {dBank}")
        if dBank <= 0:
            print(f"💸 Dealer's bankrupt! 🏦 Player's remaining funds: {dBank}")
            game = 'Over'

    global bidTable 
    bidTable += bid 

    return bidTable





dealerStart()
pStartingHand   = startingHand()

playerTable = pStartingHand[0] + pStartingHand[1]



turn = True
while turn:

    if game != "Over":
        if dealerTable == 21 or playerTable == 21:

            if dealerTable == 21 and playerTable == 21:
                print(f'🤜🏻🤛🏼 Tie! Player: {playerTable} = Dealer: {dealerTable}')
                break
            
            elif dealerTable == 21:
                print(f'🏆 Dealer wins! Black Jack! Player: {playerTable}')
                break

            elif playerTable == 21:
                print(f'🏆 Player wins! Black Jack! {playerTable}')
                break


        elif playerTable < 21:
            print(f'🐒 Player table: {playerTable}')
            hit()

        else:
            print(f'❌ Busted: {playerTable}')
            break


        while not turn:

            if dealerTable == 21:
                print(f'💰 Dealer wins! Black Jack!')
                break
            
            if dealerTable < playerTable:
                dealerTable = dealerTurn(dealerTable)
            
            elif dealerTable > 21:
                print(f'❌ Dealer busted: {dealerTable}')
                break

            elif dealerTable >= playerTable:
                print(f'🏆 Dealer wins! {dealerTable} > {playerTable}')
                break
        
    else:
        print(f'☠️ Game Over!')