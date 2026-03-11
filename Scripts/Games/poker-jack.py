import random

player      = 0
playerTable = 0
pBank       = 5000

dealer      = 0
dealerTable = 0
dBank       = 5000

bid         = 500
bidTable    = 0

round       = 0

game = 'On'


def checkAce(card, table):
    if card in (1, 11):
        if table + 11 <= 21:
            return 11
        else:
            return 1
    return card


def hit():
    
    global playerTable, turn
    wantToHit= str(input("\n🎰 Hit or Pass: y/n ")).strip().lower()

    if wantToHit in ('y', 'yes', 'hit'):
        draw = checkAce(random.randint(1, 11), playerTable)
        print(f'🐒 Drawing: {draw} + {playerTable} = {playerTable + draw}\n')
        playerTable += draw
        
        bidding(bid,"player")

    else: 
        turn = False


def startingHand():

    global playerTable, turn, pBank, bidTable

    card1   = random.randint(1, 11)
    card2   = random.randint(1, 11)

    print(f'🐒 Player starting hand: {card1}, {card2}')



    if {card1, card2} == {1,10} or {card1, card2} == {11,10}:
        print(f'\n💰 Player natural Black Jack. GGs {card1} {card2}')
        pBank += int(bidTable * 1.5)
        playerTable = 21
        bidTable = 0
        turn = False

    else: 
        card1 = checkAce(card1, 0)
        playerTable = card1
        card2 = checkAce(card2, playerTable)
        playerTable += card2





def dealerStart():
    global dealerTable , turn, pBank, dBank, bidTable
    
    dealer_card1   = random.randint(1, 11)
    dealer_card2   = random.randint(1, 11)

    if dealer_card1 in (1,11):
        dealer_card1 = 11

    if dealer_card2 in (1,11) and not dealer_card1 in (1,11):
        dealer_card2 = 11

    if {dealer_card1, dealer_card2} == {1,10} or {dealer_card1, dealer_card2} == {11,10}:
        print(f'💰 Dealer natural Black Jack. GGs {dealer_card1} {dealer_card2}')
        dBank += int(bidTable  * 1.5)
        bidTable = 0
        turn = False
    else:
        print(f'🤖 Dealer 1st card: {dealer_card1}') ####  {dealer_card2}

    dealerTable = dealer_card1 + dealer_card2


def dealerTurn():
    global dealerTable

    dealer_draw = checkAce(random.randint(1, 11), dealerTable)
    dealerTable += dealer_draw

    print(f'\n🃏 Dealer draw: {dealer_draw}\tCurrent table: {dealerTable}')
    bidding(bid,"dealer")



#### Each hit costs one bid
def bidding(bid, bidder):

    global pBank, dBank, bidTable, game

    if bidder == 'player':
        if pBank < bid:
            print(f"💸 Player's bankrupt!") ####  🏦 Dealer's remaining funds: {dBank}
            
            if playerTable <= dealerTable:
                print(f'Player table: {playerTable} -- Dealer table {dealerTable}')
                game = 'Over'
        else:
            print(f"🏦 Player remaining funds: {pBank}")
            pBank -= bid

    elif bidder == 'dealer':
        if dBank < bid:
            print(f"💸 Dealer's bankrupt!") #### 🏦 Player's remaining funds: {pBank}
            
            if dealerTable < playerTable:
                print(f'Dealer table {dealerTable} -- Player table: {playerTable}')
                game = 'Over'
            
        else:
            print(f"🏦 Dealer remaining funds: {dBank}")
            dBank -= bid

    bidTable += bid 

    return bidTable, pBank, dBank



while game != 'Over':
    
    round += 1
    turn = True
    # print(f'\n{'_'*25}\n  Round: {round}')
    print(f'\n_________________________ \n  Round: {round}')
    dealerTable = 0
    playerTable = 0
    bidTable = 0

    #### Player and dealer pay for the cards
    if game != "Over": 
        bidding(bid,"player")   
        bidding(bid,"dealer")   
        dealerStart()
        startingHand()

    
    #### Player turn
    while turn:

        print(f"💰 Pot: {bidTable}") 
        if game != "Over":
            if dealerTable == 21 or playerTable == 21:

                if dealerTable == 21 and playerTable == 21:
                    print(f'‼️ Tie! Player: {playerTable} = Dealer: {dealerTable}')
                    pBank += bidTable // 2
                    dBank += bidTable // 2
                    break
                
                elif dealerTable == 21:
                    print(f'🏆 Dealer wins! Black Jack! Player: {playerTable}')
                    dBank += bidTable
                    break

                elif playerTable == 21:
                    print(f'🏆 Player wins! Black Jack! {playerTable}')
                    pBank += bidTable
                    break


            elif playerTable < 21: # and pBank > bid
                print(f'🐒 Player table: {playerTable}\n')
                hit()

            else:
                print(f'❌ Busted: {playerTable}')
                dBank += bidTable
                break

            
            #### Dealer's automatic turn
            while not turn:

                if dealerTable == 21:
                    print(f'💰 Dealer wins! Black Jack!')
                    dBank += bidTable
                    break
                
                #### In standard black jack the dealer MUST hit until 17 and stop at 17 or higher,
                #### the dealer cannot actually gamble or take decisions.
                #### Also there are some rules (like soft 17) that were intentionally ignored 
                if dealerTable < playerTable and playerTable < 21: #  and dBank > bid 
                    dealerTurn()
                
                elif dealerTable > 21:
                    print(f'❌ Dealer busted: {dealerTable}')
                    pBank += bidTable
                    break

                elif dealerTable >= playerTable:
                    print(f'🏆 Dealer wins! {dealerTable} > {playerTable}')
                    dBank += bidTable
                    break
            
        else:
            print(f'☠️ Game Over!')
            break