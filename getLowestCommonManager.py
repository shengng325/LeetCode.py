def getLowestCommonManager(topManager, reportOne, reportTwo):
	orgInfo = OrgInfo()
	getManagerHelper(topManager, reportOne, reportTwo, orgInfo)
	return orgInfo.commonManager.name

def getManagerHelper(current, reportOne, reportTwo, orgInfo):
	if current is None or orgInfo.commonManager is not None:
		return 0
	reportsFound = 0
	if current == reportOne or current == reportTwo:
		reportsFound+=1	
	for directReport in current.directReports:
		reportsFound += getManagerHelper(directReport, reportOne, reportTwo, orgInfo)
	if reportsFound == 2 and orgInfo.commonManager is None:
		orgInfo.commonManager = current
	return reportsFound
	
class OrgInfo:
	def __init__(self, commonManager=None, reportsFound=0):
		self.commonManager = commonManager
		self.reportsFound = reportsFound

class OrgChart:
	def __init__(self, name):
		self.name = name
		self.directReports = []

nodeA = OrgChart("A")
nodeB = OrgChart("B")
nodeC = OrgChart("C")
nodeD = OrgChart("D")
nodeE = OrgChart("E")
nodeF = OrgChart("F")
nodeG = OrgChart("G")
nodeH = OrgChart("H")
nodeI = OrgChart("I")
nodeA.directReports = [nodeB, nodeC]
nodeB.directReports = [nodeD, nodeE]
nodeD.directReports = [nodeH, nodeI]
nodeC.directReports = [nodeF, nodeG]

results = getLowestCommonManager(nodeA, nodeH, nodeD)
print(results)