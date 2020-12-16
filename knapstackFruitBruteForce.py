def knapstackFruit(weight, profit, capacity):
    return knapstackRecursion(weight, profit, capacity, 0)

def knapstackRecursion(weight, profit, capacity, idx):
    if capacity <= 0 or idx >= len(weight):
        return 0
    includeCurProfit = 0
    if weight[idx] <= capacity:
        includeCurProfit = profit[idx] + knapstackRecursion(weight, profit, capacity - weight[idx], idx + 1)
    excludeCurProfit = knapstackRecursion(weight, profit, capacity, idx + 1)
    return max(includeCurProfit, excludeCurProfit)
    


weight = [1, 2, 3, 5]
profit = [1, 6, 10, 16]
capacity = 6
results = knapstackFruit(weight, profit, capacity)
print(results)