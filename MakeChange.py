__author__ = 'Toshiki'

import sys, string

change = int(raw_input("Amount of change needed"))
denom = string.split(raw_input("Coin denominations eg. 25 10 5 1 for quarter,dime,nickel,penny"))
stock = string.split(raw_input("Current coins on hand"))
returnchange = []

def makechange(amtchange, denoms, coinstock):
    if(coinstock == []):return      #No more coins
    currentcoin = int(denoms[0])
    count = 0
    if(int(coinstock[0]) > 0):      #Have coins to use otherwise skip
        for coin in range(int(coinstock[0])): #For each available coin in stock
            if(amtchange >= currentcoin):     #If coin is small enough for change
                amtchange -= currentcoin      #Use coin
                count += 1                    #Count usage of coin
    returnchange.append(count)
    makechange(amtchange, denoms[1:],coinstock[1:]) #Move on to next denominator

makechange(change,denom,stock)
print returnchange