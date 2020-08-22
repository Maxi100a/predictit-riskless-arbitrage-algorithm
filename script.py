#Importing the necessary libraries
import requests
import sys
import json

def printAll():
    #Make the HTML request
    api_url = "https://www.predictit.org/api/marketdata/all"
    r = requests.get(api_url)

    #Put the data into a JSON object
    data = r.json()
    
    #Loop through all the markets, printing out only those who's contracts length > min_threshold
    min_threshold = 5
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
        #print(json.dumps(data, indent = 4))
        
    

#Parse command-line arguments
if (len(sys.argv) >= 2):
    handleArgs()
else:
    printAll()






#Display the amount of markets
#print(len(data['markets']))
#print(json.dumps(data, indent = 4))