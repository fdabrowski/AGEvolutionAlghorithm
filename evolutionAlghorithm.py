import random

N = 10
ilosc = 100
x1 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
x2 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
u = []
J = []
sum_u = []

def prepareU():
    for i in range(0,ilosc):
        randomNumbers = []
        for x in range(0,N):
            randomNumbers.append(random.uniform(1,10))
        u.append(randomNumbers)
        sum_u.append(sum(randomNumbers))

def calculateVariables():
    prepareVariablesAndU()
    for i in range(0,ilosc):
        for k in range(0,N-1):
            x1[i][k+1] = x2[i][k]
            x2[i][k+1] = 2*x2[i][k]-x1[i][k]+ u[i][k]/(N*N)
        J.append(x1[i][N-1]-(1/(2*N))*sum_u[i])

calculateVariables()


