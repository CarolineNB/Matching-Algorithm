#The following is the scoring metric for the modified basic Gale-Shapley algorithm that lets
#students list their top “k” preferences of “n” internships. Again, the randomizing algorithm is
#included in this code as well. 

import numpy as np
from numpy import random
cap = 1
n = 5
k = 3

employeeNames3 = []
for i in np.arange(0,n):
 employeeName = "Emp" + str(i)
 employeeNames3.append(employeeName)

projectNumbers3 = np.arange(0,n).tolist()

shuffledProject = np.copy(projectNumbers3)
shuffledEmployee = np.copy(employeeNames3)

np.array(random.shuffle(shuffledProject))
np.array(random.shuffle(shuffledEmployee))

employeeRankings3 = np.empty([n, n],dtype = 'object')
for i, employeee in enumerate(employeeNames3):
 random.seed(2)
 random.shuffle(shuffledProject)
 employeeRankings3[i] = shuffledProject
 showOnlyEmployeeRankings3 = employeeRankings3[:, :k]
  
projectRankings3 = np.empty([n, n],dtype = 'object')
for i in projectNumbers3:
 random.seed(23)
 random.shuffle(shuffledEmployee)
 projectRankings3[i] = shuffledEmployee
emplRankings3 = np.ndarray.tolist(showOnlyEmployeeRankings3)
projRankings3 = np.ndarray.tolist(projectRankings3)
print(emplRankings3)
print(projRankings3)

def rankofEmployee(employee, project, employeeRankings, projectRankings, projectNumbers, employeeNames):
 projectIndex = projectNumbers.index(project)
 return (projectRankings[projectIndex].index(employee))

def galeShapley(employeeNames, projectNumbers, employeeRankings, projectRankings, cap):
 k = len(employeeRankings[0])
 n = len(employeeNames)
 r = len(projectNumbers)
 cap
  
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

 employeeScore = []
 projectScore = []
 for i, matched in enumerate(matched):
   matchedEmployeeIndex = employeeNames.index(matched)
   matchedEmployeeRows = employeeRankings[matchedEmployeeIndex]
   projectMatch = finalMatch[i][0]
   projectMatchIndex = projectNumbers.index(projectMatch)
   employeePlacement = matchedEmployeeRows.index(projectMatch)
   employeeScore.append(employeePlacement)
   supposedEmployeeScore = sum(employeeScore) * 10
   finalEmployeeScore = (i + 1) * (n * 10) - supposedEmployeeScore

   projectPlacement = projectRankings[projectMatchIndex].index(matched)
   projectScore.append(projectPlacement)
   supposedProjectScore = sum(projectScore) * 10
   finalProjectScore = (i + 1) * (n * 10) - supposedProjectScore

 print(finalEmployeeScore)
 print(finalProjectScore)
 print(unmatched)
 return finalMatch
