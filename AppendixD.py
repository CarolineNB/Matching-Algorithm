#The following is the original Gale-Shapley algorithm with the scoring metric 2.3.2 and is set to
# giving points to matches that are matched with their first ranked preference. 

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

 for i, matched in enumerate(matched):
     match = [projectNumbers[i], matched ]
     finalMatch.append(match)
     
     matchedEmployeeIndex = employeeNames.index(matched)
     matchedEmployeeRows = employeeRankings[matchedEmployeeIndex] 
     matchedEmployeeRowList = np.ndarray.tolist(matchedEmployeeRows)
     employeePlacement = matchedEmployeeRowList.index(projectNumbers[i])
     employeeScore.append(employeePlacement)

     Escores = []
     for i, rank in enumerate(employeeScore):
       if rank == 0:
         Escore = 100
       elif rank == 1:
         Escore = 100
       else:
         Escore = 0
       Escores.append(Escore)

     matchedProjectRowList = np.ndarray.tolist(projectRankings[i])
     projectPlacement = matchedProjectRowList.index(matched)
     projectScore.append(projectPlacement)

     Pscores = []
     for i, rank in enumerate(projectScore):
       if rank == 0:
        Pscore = 100
       elif rank == 1:
        Pscore = 0
       else:
        Pscore = 0
       Pscores.append(Pscore)

  print(sum(Escores))
  print(sum(Pscores))
  return finalMatch
