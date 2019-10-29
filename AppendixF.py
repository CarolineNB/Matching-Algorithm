#The following is the scoring metric for the modified basic Gale-Shapley algorithm that matches
#multiple students to a single internship where students are left unmatched. Also included is its
#randomization algorithm

import numpy as np
from numpy import random

n = 62
m = 10
cap = 5
employeeNames3 = []

for i in np.arange(0,n):
 employeeName = "Emp" + str(i)
 employeeNames3.append(employeeName)

projectNames3 = np.arange(0,m).tolist()

shuffledProject = np.copy(projectNames3)
shuffledEmployee = np.copy(employeeNames3)

np.array(random.shuffle(shuffledProject))
np.array(random.shuffle(shuffledEmployee))

employeeRankings3 = np.empty([n, m],dtype = 'object')
for i, employeee in enumerate(employeeNames3):
 random.seed(0)
 random.shuffle(shuffledProject)
 employeeRankings3[i] = shuffledProject
print(employeeRankings3)

projectRankings3 = np.empty([m, n],dtype = 'object')
for i in projectNames3:
 random.seed(1)
 random.shuffle(shuffledEmployee)
 projectRankings3[i] = shuffledEmployee
print(projectRankings3)

emplRankings3 = np.ndarray.tolist(employeeRankings3)
projRankings3 = np.ndarray.tolist(projectRankings3)

def rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers,
employeeNames):
 projectIndex = projectNumbers.index(project)
 return (projectRankings[projectIndex].index(employee))

def galeShapley(employeeNames, projectNumbers, employeeRankings, projectRankings, cap):
 k = len(employeeRankings[0])
 n = len(employeeNames)
 r = len(projectNumbers)
 cap
  
 capLength = np.arange(0,cap)
 capLengthList = np.ndarray.tolist(capLength)

 projectLength = np.arange(0, r)
 projectLengthList = np.ndarray.tolist(projectLength)
  
 employeeLength = np.arange(0, n)
 employeeLengthList = np.ndarray.tolist(employeeLength)

 unmatchedHaveOptions = True
 unmatched = employeeNames
 currentProjIndex = n*[0]
 proposals = np.zeros((r, n), dtype=bool)
  
 while not not unmatched and unmatchedHaveOptions:
  for i, employee in enumerate(employeeNames):
   project = employeeRankings[i][currentProjIndex[i]]
   projectIndex = projectNumbers.index(project)
   colIndex = rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers, employeeNames)
   proposals[projectIndex][colIndex] = True
    
 matched = []
 finalMatch = []
 for i, project in enumerate(projectNumbers):
  data = proposals[i]
  if any(data):
    x = [i for i, x in enumerate(data) if x]
  if len(x) > cap:
    colIndex = x[0:cap]
    for j in np.arange(0, cap):
      matchedEmployee = projectRankings[i][colIndex[j]]
      matched.append(matchedEmployee)
      matches = [project, matchedEmployee]
      finalMatch.append(matches)
  elif len(x) <= cap:
    colIndex = x[:]
    for j in np.arange(len(x)):
    matchedEmployee = projectRankings[i][colIndex[j]]
    matched.append(matchedEmployee)
    matches = [project, matchedEmployee]
    finalMatch.append(matches) 
    unmatched = list(set(employeeNames) - set(matched)) 
    unmatchedHaveOptions = False
    for i, employee in enumerate(unmatched):
      unmatchedEmployee = employeeNames.index(employee)
   if currentProjIndex[unmatchedEmployee] < k-1:
   currentProjIndex[unmatchedEmployee] = currentProjIndex[unmatchedEmployee] + 1
   hasOptions = True
 else:
   hasOptions = False
   unmatchedHaveOptions = unmatchedHaveOptions or hasOptions
  
 idealPScore = []

 for i in projectLengthList:
   idealPIndexScore = sum(capLengthList)
   idealPScore.append(idealPIndexScore)
   supposedIdealPScore = sum(idealPScore) * 10
   idealEmployeeScore = r * 10 * cap * m
   employeeScore = []
   projectScore = []
   for i, matched in enumerate(matched):
     projectMatch = finalMatch[i][0]
     projectMatchIndex = projectNumbers.index(projectMatch)
     matchedEmployeeIndex = employeeNames.index(matched)
     matchedEmployeeRows = employeeRankings[matchedEmployeeIndex]
     employeePlacement = matchedEmployeeRows.index(projectMatch)
     employeeScore.append(employeePlacement)
     finalEmployeeScore = (m * cap * m * 10) - (sum(employeeScore) * 10)
     idealEmployeeScore = m * 10 * cap * m
     projectPlacement = projectRankings[projectMatchIndex].index(matched)
     projectScore.append(projectPlacement)
     supposedProjectScore = sum(projectScore) * 10

 finalProjectScore = (i + 1) * (n * 10) - supposedProjectScore
 idealProjectScore = (i + 1) * (n * 10) - supposedIdealPScore
 projectPercent = finalProjectScore/idealProjectScore
 employeePercent = finalEmployeeScore/idealEmployeeScore

 print(len(unmatched))
 print(employeePercent)
 print(projectPercent)

 return finalMatch
