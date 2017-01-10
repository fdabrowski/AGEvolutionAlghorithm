import random

N = 10
ilosc = 100
x1 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
x2 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
u = []
J = []
sum_u = []
adaptation = []
distribution = []
parents = []
childs = [[] for i in xrange(ilosc)]

def prepareU():
    for i in range(0,ilosc):
        randomNumbers = []
        randomNumbersPower = []
        for x in range(0,N):
            randomNumbers.append(random.uniform(0,10))
            randomNumbersPower.append(randomNumbers[x]**2)
        u.append(randomNumbers)
        sum_u.append(sum(randomNumbersPower))

def calculateVariables():
    prepareU()
    for i in range(0,ilosc):
        for k in range(0,N-1):
            x1[i][k+1] = x2[i][k]
            x2[i][k+1] = 2*x2[i][k]-x1[i][k]+ u[i][k]/(N**2)
        J.append(x1[i][N-1]-(1/(2*N))*sum_u[i])
    sum_J = sum(J)
    for i in xrange(len(J)):
        adaptation.append(J[i]/sum_J)
        distribution.append(sum(adaptation))

def roulette():
    for i in range(0,ilosc):
        r = random.uniform(0,1)
        for j in xrange(len(distribution)):
            if r<=distribution[j]:
                parents.append(u[j])
                break

def crossover():
    for i in xrange(len(parents)/2):
        for j in range(0,int(N/3)):
            childs[2*i].append(parents[2*i][j])
            childs[2*i+1].append(parents[2*i+1][j])
        for j in range(int(N/3),N):
            childs[2*i].append(parents[2*i+1][j])
            childs[2*i+1].append(parents[2*i][j])

calculateVariables()
roulette()
crossover()

print "tak"
print childs[1]
