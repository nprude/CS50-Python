def main():
    print("Amount Due: 50")
    coin = calculate_coins("Insert Coin: ")
    

def calculate_coins(prompt):
    coin = int(input(prompt))
    amountdue = 50
    coins = 0
    
    if coin == 25 or coin == 10 or coin == 5:
        
        addcoin(amountdue,coin, coins)   
    else:
        waivecoin(amountdue, coin, coins)
def addcoin(amountdue, coin, coins):
    amountdue = amountdue
    coins = coins
    coin = coin
    while coin == 25 or coin == 10 or coin == 5:
        coins += coin
        amountdue = amountdue - coin
        
        if coins < 50:
            print("Amount Due: " + str(abs(amountdue)))
            coin = int(input("Insert Coin: "))
           
        elif coins > 50:
            print("Change Owed: " + str(abs(amountdue)))
            break
        elif coins == 50:
            print("Change Owed: " + str(abs(amountdue)))
            break   
      
    else:
        waivecoin(amountdue, coin, coins)
def waivecoin(amountdue, coin, coins):
    amountdue = amountdue
    coins = coins
    coin = coin
    
    if coin != 25 or coin != 10 or coin != 5: 
        print("Amount Due: " + str(amountdue))
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            addcoin(amountdue, coin, coins)
        else:
            waivecoin(amountdue, coin, coins)
        
main()