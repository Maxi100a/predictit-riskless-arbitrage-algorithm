#Import the necessary libraries
import requests;
import json
from bet import Bet
import math
from operator import attrgetter
import sched
import time

contracts = []

def analyzeMarket(market):
    yesList = []
    noList = []
    bestYesList = []
    bestNoList = []
    for i in market['contracts']:
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
    #stopping incorrect display of data  
    if(-850 != math.floor(noSum * (850/noList[len(noList) - 1]))):
        contract = Bet(market['id'], yesSum, noSum, math.floor(yesSum * (850/yesList[len(yesList) - 1])), math.floor(noSum * (850/noList[len(noList) - 1])))
        contracts.append(contract)
        

        outputString = "Market: " + str(market['id'])
        outputString += "\nYes profit"
        outputString += "\n\t single: " + str(yesSum) + " \t max: " + str(math.floor(yesSum * (850/yesList[len(yesList) - 1])))
        outputString += "\nNo profit"
        outputString += "\n\t single: " + str(noSum) + "\t max: " + str(math.floor(noSum * (850/noList[len(noList) - 1]))) + "\n\n"
        requests.post("WEBHOOK_HERE", {"content": outputString})
    
def analyzeAll():
    requests.post("WEBHOOK_HERE", 
    {"content": "---------------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------------"})
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
    
    
    
    yesContracts = sorted(contracts, key=attrgetter('yesSingle'), reverse=True)
    noContracts = sorted(contracts, key=attrgetter('noSingle'), reverse=True)
    
    outputString = "____________________________________________________"
    outputString += "\nBest Yes contracts"
    for i in range (0, 5):
        outputString += "\n" + str(yesContracts[i])
    outputString += "\n____________________________________________________"
    outputString += "\nBest no contracts: "
    for i in range (0,8):
        outputString += "\n" + str(noContracts[i])
    requests.post("WEBHOOK_HERE", {"content": outputString})
    print(outputString)
analyzeAll()
            
