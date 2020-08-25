# predictit-riskless-arbitrage-algorithm
Predictit Riskless Arbitrage Algorithm (PRAA)

## Predictit.org
Predictit.org is a betting website that is exclusively aimed at politics.

**How does it work?** <br>
Predictit has multiple markets on the site. Each market is comprised of at least one contract. There are two sides to any contract: yes and no. The contracts sell for anywhere between $0.01 and $0.99. If a bet is right, your bet is returned and 90% of the difference between the contract cost and $1 (or (1-bet)*.9 + bet). Additionally, you can’t bet on both sides of one contract and the maximum bet on any contract can’t exceed $850.

**What is a riskless trade?** <br>
A riskless trade, the focus of this algorithm, in this case, is where no matter the outcome money is made and no capital is ever truly at risk. There are a few good examples of riskless trades on Predictit. The best and most common riskless trade is comprised of all no contracts. Because no market can have two contracts win, only one contract will ever lose. So the way to check if a market has a riskless no trade is to take sum of all profits excluding the most expensive contract’s profit and subtract the cost of the most expensive contract from it. If the calculation results in a positive number, then the trade is riskless and profitable if not then it is still riskless, but you will lose money in any outcome. 

**How does the algorithm work?** <br>
The algorithm first checks all markets with 3 or more contracts. This is because a market with a single contract can not be hedged, the odds of a market with two contracts having the right prices are low, so we found that 3 is the best. Next, the algorithm takes all yes and no contract prices in the market and finds the profits from each contract. Then it uses the previously mentioned equation to see if the trade is profitable and returns that it is profitable and the lowest profit, if it isn’t profitable it returns the cumulative amount the contracts must fall to be profitable. Finally, it moves on to the next market and repeats. 

---
# Files
## Set up 
Replace **line 66** of multiple.py with a valid webhook link. It will post the results to that link. If this is not desired, modify the code to just have the results be outputted.

## Usage
```
py indvidual.py -[h|i|a] [id]
Options
  -h: display the help menu
  -i ID: display the contracts for the specified market
  -a ID: display the analysis for the specified market
```
This was the prototype file for multiple.py. Running the file without any arguments will output all the markets that surpass the **min_threshold** variable. Adding arguments will act according to the description above, allowing the user to individually analyze markets.
<br>

```
py multiple.py
```
This file will analyze all of the markets that surpass the **min_threshold** variable using the same technique as in individual.py. It will upload its analysis to a shared Discord server between the contributors.

```
py multiple_repeating_search.py
```
This file will execute a repeating search and analyzation using the same methodology as previous files for the markets inputed by user. It will then upload this list of user inputed market data to a shared discord server between the contributors. 

--- 
**Authors** <br>
Maximiliano Aedo Espicto<br>
Phillip Roth <br>
Maxwell Stevens <br>

