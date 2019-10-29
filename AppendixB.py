#The following is the coded randomizing algorithm that is set in printing out 100 student rankings
#and 100 project rankings. 

import numpy as np
from numpy import random

n = 100

employeeNames3 = []
for i in np.arange(0,n):
 employeeName = "Emp" + str(i)
 employeeNames3.append(employeeName)

projectNames3 = np.arange(0,n).tolist()

shuffledProject = np.copy(projectNames3)
shuffledEmployee = np.copy(employeeNames3)

np.array(random.shuffle(shuffledProject))
np.array(random.shuffle(shuffledEmployee))

employeeRankings3 = np.empty([n, n],dtype = 'object')
for i, employeee in enumerate(employeeNames3):
 random.seed(0)
 random.shuffle(shuffledProject)
 employeeRankings3[i] = shuffledProject
print(employeeRankings3)

projectRankings3 = np.empty([n, n],dtype = 'object')
for i in projectNames3:
 random.seed(1)
 random.shuffle(shuffledEmployee)
 projectRankings3[i] = shuffledEmployee
print(projectRankings3)

emplRankings3 = np.ndarray.tolist(employeeRankings3)
projRankings3 = np.ndarray.tolist(projectRankings3) 
