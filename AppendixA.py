#The following is the coded basic stable matching algorithm. 

import numpy as np


def rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers, employeeNames):
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
for i, matched in enumerate(matched):
 match = [projectNumbers[i], matched]
 finalMatch.append(match)
return finalMatch
 
