
MAX_LINeS = 3
import random
rows = 3
cols = 3
symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 7,
}

def slot_machine(rows):
    all_symbols = []
    for symbol, symbolcount in symbol_count.items():
        for _ in range(symbolcount):
            all_symbols.append(symbol)
            

def deposit():
    while True:
        amount = input("Enter your Deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid number:")
                continue
        else:
            print("Enter a valid number: ")
            continue
    return amount

def lines_Input():
    while True:
        lines = input("Enter the Number of lines that you would like to bet on (1-3):")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <=3:
                break
            else:
                print("Please Enter the number of lines between 1 to",MAX_LINeS,":")
                continue
        else:
            print("Please Enter the number of lines between 1 to",MAX_LINeS,":")
            continue
    return lines

def bet():
    while True:
        bet = input("Enter the bet on each line: ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= 1 and bet <=100:
                break
            else:
                print("Please Enter the Bet amount between 1 - 100")
                continue
        else:
            print("Please Enter the Bet amount between 1 - 100")
            continue
    return bet

def main():
    balance = deposit()
    lines = lines_Input()
    bets = bet()
    total_bet = lines * bets
    print("You are betting $",bets,"on",lines,"lines. Total Bet is equal to:",total_bet)

main()
