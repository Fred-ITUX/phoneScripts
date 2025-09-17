import random

def operatorChoice(lvl):

    if lvl > 0 and lvl < 5:
        operators = [ '+', '-' ] 
    elif lvl >= 5 and lvl < 10:
        operators = [ '+', '-', '*' ] 
    else:
        operators = [ '+', '-', '*', '/' ] 
    
    
    #### operators = [ '+', '-', '/', '*' ] 
    op = random.choice(operators)

    return op



def advLvl():

    n1 = random.randint(10, 200)
    n2 = random.randint(0, 50)

    return n1, n2


def calc(op):
    
    if op == "+":
        result = n1+n2
    elif op == "-":
        result = n1-n2
    elif op == "/":
        result = n1/n2
        result = float(f'{result:.1f}')
    elif op == "*":
        result = n1*n2
    else:
        print(f'Operation error, exiting...')
        exit()
    
    # print(f'result: {n1} {op} {n2} = {result}')
    return result



while True:

    lvl = 0

    while True:        
        
        lvl += 1
        op = operatorChoice(lvl)
        n1, n2 = advLvl()
        result = calc(op)
        
        try:
            userInput = float(input(f'\nLevel: {lvl}\t {n1} {op} {n2} = '))
            userInput = float(f'{userInput:.1f}')
        except Exception as e:
            print(f'Error {e}, resetting...')
            break

        if userInput != float(result):
            print(f'\n❌ Wrong: {n1} {op} {n2} = {result}\n')
            
            again = input('\nTry again? y/n ')
            if again == "y":
                break
            else:
                exit()
