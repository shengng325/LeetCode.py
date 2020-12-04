def happyNumber(number):
    slow = findSquareSum(number)
    fast = findSquareSum(findSquareSum(number))
    while slow != fast:
        slow = findSquareSum(slow)
        fast = findSquareSum(findSquareSum(fast))
    return slow == 1

def findSquareSum(number):
    squareSum = 0
    while number > 0:
        digit = number % 10
        squareSum+=digit*digit
        number //= 10
    return squareSum

number = 12
results = happyNumber(number)
print(results)