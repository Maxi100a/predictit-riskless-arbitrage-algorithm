#Importing the necessary libraries
import requests
import sys
import json
from bet import Bet
import math
import sched
import time
import schedule
import time

markets = []
scheduler = sched.scheduler(time.time, time.sleep)

def marketLoopLoader():
    runMarketLoop()
    schedule.every(30).minutes.do(runMarketLoop)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
def runMarketLoop():
    t = time.localtime()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    outputString = (current_time)
    
    for i in range(0, len(markets) - 1):
        market = markets[i]
        api_url = "https://www.predictit.org/api/marketdata/markets/"  + market
        r = requests.get(api_url)
        
        data = r.json()
        contracts = [] 
        yesList = []
        noList = []
        for i in data['contracts']:
            yesCost = i["bestBuyYesCost"]
            noCost = i["bestBuyNoCost"]
            name = i['name']
                        
            if yesCost is None:
                yesList.append(-1)
            else:
                yesList.append(yesCost)
                
            if noCost is None:
                noList.append(-1)
            else:
                noList.append(noCost)
                
               
        yesList = sorted(yesList)
        noList = sorted(noList)
        
        yesProfit = []
        noProfit = []
        for i in yesList:            
            if (i != -1):
                yesProfit.append(round((1-i)*0.9, 4))
            else:
                yesProfit.append(-1)
                
        for i in noList:
            if (i != -1): 
                noProfit.append(round((1-i)*0.9, 4))
            else:
                noProfit.append(-1)
           

        #Calculating the yes profit
        yesSum = 0;
        for i in range (0, len(yesList) - 1):
            yesSum += yesList[i] if yesList[i] != -1 else yesSum
            
        yesSum = yesProfit[len(yesProfit) - 1] - yesSum
        
        
        #Calculating the no profit
        noSum = 0;
        for i in range (0, len(noProfit) - 1):
            noSum += noProfit[i] if noProfit[i] != -1 else noSum
            
        noSum = noSum - noList[len(noList) - 1]
        outputString += ("\n\nMarket: " + market)
        outputString += ("\nYes profit")
        outputString += ("\n\t single: " + str(yesSum) + " \t max: " + str(math.floor(yesSum * (850/yesList[len(yesList) - 1]))))
        outputString += ("\nNo profit")
        outputString += ("\n\t single: " + str(noSum) + "\t max: " + str(math.floor(noSum * (850/noList[len(noList) - 1]))))
    outputString += ("\n____________________________________________________________________________")
    print(outputString)
    requests.post("WEBHOOK_HERE", {"content": outputString})
        
def handelMarkets():
        #adds markets requested to market list
        market = ''
        while market != '-q' and market != '-e':
            market = input("\nEnter a valid market: ")
            markets.append(market)
        if(market == '-e'):
            marketLoopLoader()
            



#Parse command-line arguments
print("\nPlease enter market IDs for tracking\nEnter -q to quit\nEnter -e to execute\n")
handelMarkets()

