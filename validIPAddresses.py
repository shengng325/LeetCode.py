# def validIPAddresses(string):
# 	ipAddresses = []
# 	validIPAddressesHelper(string, 0, "", 0, ipAddresses)
# 	return ipAddresses

# def validIPAddressesHelper(string, startIdx, curIpString, dotCount, array):
# 	if dotCount >= 4:
# 		if len(curIpString) == len(string) + 3:
# 			array.append(curIpString)
# 		return
# 	for i in range(3):
# 		if startIdx + i + 1 > len(string):
# 			break
# 		currentStr = string[startIdx: startIdx + i + 1]
# 		startWithZero = len(currentStr) > 1 and currentStr[0] == '0'
# 		greaterThanMax = len(currentStr) > 3 or (currentStr[0] != '0' and int(currentStr) > 255)
# 		if startWithZero or greaterThanMax:
# 			continue
# 		if dotCount < 3:
# 			currentStr+= "."
# 		validIPAddressesHelper(string, startIdx + i + 1, curIpString+currentStr, dotCount + 1, array)

def validIPAddresses(string):
	ipAddresses = []
	
	for i in range(3):
		curIP = ["","","",""]
		numberToAdd = string[: i + 1]
		if notValid(numberToAdd):
			continue
		curIP[0] = numberToAdd
		
		for j in range( i + 1, i + 4):
			numberToAdd = string[i + 1: j + 1]
			if notValid(numberToAdd):
				continue
			curIP[1] = numberToAdd
			
			for k in range( j + 1, j + 4 ):
				numberToAdd = string[j + 1: k + 1]
				finalNumberToAdd = string[k + 1:]
				if notValid(numberToAdd) or notValid(finalNumberToAdd):
					continue
				curIP[2], curIP[3] = numberToAdd, finalNumberToAdd
				ipAddresses.append(".".join(curIP))			
	return ipAddresses

def notValid(numberToAdd):
	if len(numberToAdd) == 0:
		return True
	number = int(numberToAdd)
	if number > 255:
		return True
	return len(numberToAdd) != len(str(number))

def addToAddresses(ipArr, ipAddresses):
	curIPStr = ipArr[0] + "." + ipArr[1] + "." + ipArr[2] + "." + ipArr[3]
	ipAddresses.append(curIPStr)			

var = "1921680"
results = validIPAddresses(var)
print(results)		