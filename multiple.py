#Import the necessary libraries
import requests;
import json
from bet import Bet

def analyzeMarket(market):
    contracts = [] 
    yesList = []
    noList = []
    for i in market['contracts']:
        yesCost = i["bestBuyYesCost"]
        noCost = i["bestBuyNoCost"]
        name = i['name']
        
        bet1 = Bet(name, yesCost, noCost)
        contracts.append(bet1)
            
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
    outputString = "Market: " + str(market['id'])
    outputString += "\nYes profit"
    outputString += "\n\t single: " + str(yesSum) + " \t max: " + str(yesSum * (850/yesList[len(yesList) - 1]))
    outputString += "\nNo profit"
    outputString += "\n\t single: " + str(noSum) + "\t max: " + str(noSum * (850/noList[len(noList) - 1])) + "\n\n"
    
    requests.post("WEBHOOK_LINK_HERE", {"content": outputString})
    
def analyzeAll():
    #Make the HTML request
    api_url = "https://www.predictit.org/api/marketdata/all"
    r = requests.get(api_url)
    
    #Put the data into a JSON object
    data = r.json()
    
    #Loop through all the markets 
    min_threshold = 3
    markets = []
    for i in data['markets']:
        if (len(i['contracts']) >= min_threshold):
            analyzeMarket(i)

analyzeAll()
            
