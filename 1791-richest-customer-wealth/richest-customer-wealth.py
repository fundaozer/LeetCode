class Solution(object):
    def maximumWealth(self, accounts):
        maxWealth=0
        for i in range(len(accounts)):
            currentWealth=0
            for j in range(len(accounts[i])):
                currentWealth+=accounts[i][j]
            if currentWealth > maxWealth :
                maxWealth=currentWealth
        return maxWealth
       
        