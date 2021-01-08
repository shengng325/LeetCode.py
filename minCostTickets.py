class Solution:
    def mincostTickets(self, days, costs):
        return self.minCostHelper(days, costs, 0, 0, {})
        
    def minCostHelper(self, days, costs, dayIdx, dayAvailability, cache):
        if (dayIdx, dayAvailability) in cache:
            return cache[(dayIdx, dayAvailability)]
        if dayIdx >= len(days):
            return 0
        cost = float("inf")
        if days[dayIdx] <= dayAvailability:
            cost = self.minCostHelper(days, costs, dayIdx+1, dayAvailability, cache)
        else:
            for i in range(len(costs)):
                dayAvailability = self.getDaysAvailable(days[dayIdx], i)
                potentialCost = costs[i] + self.minCostHelper(days, costs, dayIdx+1, dayAvailability, cache)
                cost = min(cost, potentialCost)
        cache[(dayIdx, dayAvailability)] = cost
        return cost

    def getDaysAvailable(self, curDay, costIdx):
        if costIdx == 0:
            return curDay
        elif costIdx == 1:
            return curDay + 6
        else:
            return curDay + 29

sol = Solution()
days =  [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
results = sol.mincostTickets(days, costs)
print(results)