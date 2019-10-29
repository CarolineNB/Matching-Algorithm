#The following is the original Gale-Shapley algorithm along with the scoring metric 2.3.1. 

import numpy as np

def rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers,
employeeNames):
 projectIndex = projectNumbers.index(project)
 temp = np.ndarray.tolist(projectRankings[projectIndex])
 return temp.index(employee)
 
def galeShapley(employeeNames, projectNumbers, employeeRankings, projectRankings):
 n = len(employeeNames)
 unmatched = employeeNames
 currentProjIndex = n*[0]
 proposals = np.zeros((n, n), dtype=bool)
 
 while not not unmatched:
  for i, employee in enumerate(employeeNames):
   project = employeeRankings[i][currentProjIndex[i]]
   projectIndex = projectNumbers.index(project)
   colIndex = rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers, employeeNames)
   proposals[projectIndex][colIndex] = True
  matched = []
  for i, project in enumerate(projectNumbers):
   data = proposals[i]
   if any(data):
     x = [i for i, x in enumerate(data) if x]
     colIndex = x[0]
     matchedEmployee = projectRankings[i][colIndex]
     matched.append(matchedEmployee)
     unmatched = list(set(employeeNames) - set(matched))
  for i, employee in enumerate(unmatched):
   unmatchedEmployee = employeeNames.index(employee)
   currentProjIndex[unmatchedEmployee] = currentProjIndex[unmatchedEmployee] + 1
 match = []
 finalMatch = []
 employeeScore = []
 projectScore = []
 finalEmployeeScore = 0
 finalProjectScore = 0
 for i, matched in enumerate(matched):
   match = [projectNumbers[i], matched]
   finalMatch.append(match)

 matchedEmployeeIndex = employeeNames.index(matched)
 matchedEmployeeRows = employeeRankings[matchedEmployeeIndex]
 matchedEmployeeRowList = np.ndarray.tolist(matchedEmployeeRows)
 employeePlacement = matchedEmployeeRowList.index(projectNumbers[i])
 employeeScore.append(employeePlacement)
 supposedEmployeeScore = sum(employeeScore) * 10
 finalEmployeeScore = (i + 1) * (n * 10) - supposedEmployeeScore

 matchedProjectRowList = np.ndarray.tolist(projectRankings[i])
 projectPlacement = matchedProjectRowList.index(matched)
 projectScore.append(projectPlacement)
 supposedProjectScore = sum(projectScore) * 10
 finalProjectScore = (i + 1) * (n * 10) - supposedProjectScore
 print(finalProjectScore)

print((i+1) * (n *10))
print(finalEmployeeScore)
print(finalProjectScore)
return finalMatch
