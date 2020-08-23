#Importing the necessary libraries
import requests
import sys
import json
from bet import Bet

def printAll():
    #Make the HTML request
    api_url = "https://www.predictit.org/api/marketdata/all"
    r = requests.get(api_url)

    #Put the data into a JSON object
    data = r.json()
    
    #Loop through all the markets, printing out only those who's contracts length > min_threshold
    min_threshold = 3
    stringList = []
    for i in data['markets']:
        if (len(i['contracts']) >= min_threshold):
            current = "Contracts: " + str(len(i['contracts'])) + " | ID: " + str(i['id']) + " | " + i['name']
            stringList.append(current)
            
    sorted_list = sorted(stringList)
    for i in sorted_list:
        print(i)
        


def handleArgs():
    #Determine what kind of argument
    argument = sys.argv[1]
    
    #Display the help menu
    if (argument == '-h'):
        print("Usage: python3 script.py -[h|i] [id]")
        print("\t -h: displays the help menu")
        print("\t -i: displays the relevant data for the market id")
        print("\t -a: displays the analysis for the specified market")
        quit()
    
    #Get the data for a specific market using the same technique as in printAll()
    elif (argument == '-i'):
        market = sys.argv[2]
        api_url = "https://www.predictit.org/api/marketdata/markets/"  + market
        r = requests.get(api_url)
        
        data = r.json()
        
        ct = 1
        for i in data['contracts']:
            print(str(ct) + ": " + i['name'])
            print("    Best Offer Yes: " + str(i['bestBuyYesCost']))
            print("    Best Offer No: " + str(i['bestBuyNoCost']) + "\n")
            ct += 1
    
    elif (argument == '-a'):
        market = sys.argv[2]
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
        print("Market: " + market)
        print("Yes profit")
        print("\t single: " + str(yesSum) + " \t max: " + str(yesSum * (850/yesList[len(yesList) - 1])))
        print("No profit")
        print("\t single: " + str(noSum) + "\t max: " + str(noSum * (850/noList[len(noList) - 1])))
        

#Parse command-line arguments
if (len(sys.argv) >= 2):
    handleArgs()
else:
    printAll()
