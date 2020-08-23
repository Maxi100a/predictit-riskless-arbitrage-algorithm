#Import the necessary libraries
import requests;
import json
from bet import Bet
import math

def analyzeMarket(market):
    contracts = [] 
    yesList = []
    noList = []
    bestYesList = []
    bestNoList = []
    for i in market['contracts']:
        yesCost = i["bestBuyYesCost"]
        noCost = i["bestBuyNoCost"]
        name = i['name']
        
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
    outputString += "\n\t single: " + str(yesSum) + " \t max: " + str(math.floor(yesSum * (850/yesList[len(yesList) - 1])))
    outputString += "\nNo profit"
    outputString += "\n\t single: " + str(noSum) + "\t max: " + str(math.floor(noSum * (850/noList[len(noList) - 1]))) + "\n\n"
    
<<<<<<< HEAD
    requests.post("https://discord.com/channels/746834133778694165/746834133778694168/746901208723357826", {"content": outputString})
=======
    requests.post("WEBOOK_LINK", {"content": outputString})
>>>>>>> cb4f2ce458be17c4c641050b87e644ad84034aa7
    
def analyzeAll():
    requests.post("WEBOOK_LINK", 
        {"content": "---------------------------------------------------------------------------------------------------------------------"})
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
            
