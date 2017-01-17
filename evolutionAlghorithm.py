import random
import matplotlib.pyplot as plt

N = 30
ilosc = 100



def prepareU():
    u = []
    for i in range(0,ilosc):
        randomNumbers = []
        for x in range(0,N):
            while True:
                correct = True
                randomNumber = random.uniform(-N,N)
                for j in xrange(len(randomNumbers)):
                    if randomNumber == randomNumbers[j]:
                        correct = False
                if correct:
                    randomNumbers.append(randomNumber)
                    break
        u.append(randomNumbers)
    return u

def calculateVariables(u):
    x1 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
    x2 = [[0 for i in xrange(N)] for i in xrange(ilosc)]
    J = []
    sum_u = []
    adaptation = []
    distribution = []
    for i in range(0,ilosc):
        uPower = []
        for j in range(0,N):
            uPower.append(u[i][j]**2)
        for k in range(0,N-1):
            x1[i][k+1] = x2[i][k]
            x2[i][k+1] = 2*x2[i][k]-x1[i][k]+ float(u[i][k])/float((N**2))
        sum_u.append(sum(uPower))
        J.append(x1[i][N-1]-(1/float(2*N))*sum_u[i])
    mod_J = []
    C = abs(min(J)) + 1
    for i in J:
        mod_J.append(i + C)
    f = abs(sum(mod_J))
    for i in mod_J:
        adaptation.append(i / f)
        distribution.append(sum(adaptation))
    return distribution, J


def roulette(u, distribution):
    parents = []
    for i in range(0,ilosc):
        r = random.uniform(0,1)
        for j in xrange(len(distribution)):
            if r<=distribution[j]:
                parents.append(u[j])
                break
    return parents
'''
def CX(chromosom1, chromosom2):
    chromosom1_new = [0 for i in xrange(N)]
    chromosom1_new[0] = chromosom1[0]
    x = 0
    while True:
        y = chromosom2[x]
        for i in xrange(len(chromosom1)):
            if chromosom1[i] == y:
                x = i
                break
        if chromosom1_new[x] != 0:
            break
        chromosom1_new[x] = chromosom1[x]
    for i in xrange(len(chromosom1_new)):
        if chromosom1_new[i] == 0:
            chromosom1_new[i] = chromosom2[i]
    return chromosom1_new

def crossover(parents):
    childs = []
    for i in xrange(len(parents)/2):
        chromosom1 = parents[2*i]
        chromosom2 = parents[2*i+1]
        chromosom1_new = CX(chromosom1,chromosom2)
        chromosom2_new = CX(chromosom2,chromosom1)
        childs.append(chromosom1_new)
        childs.append(chromosom2_new)
    return childs
'''

def crossover(parents):
    childs = [[] for i in xrange(ilosc)]
    randomNumber = random.uniform(0,1)
    for i in xrange(len(parents)/2):
        for j in range(0,N):
            childs[2*i].append(randomNumber*parents[2*i][j]+(1-randomNumber)*parents[2*i+1][j])
            childs[2*i+1].append(randomNumber*parents[2*i+1][j]+(1-randomNumber)*parents[2*i][j])
    return childs


def inversion(chromosom):
    chromosom_new = []
    a = random.randint(0, N-1)
    while True:
        b = random.randint(0, N-1)
        if b != a:
            break
    if b < a:
        buf = a
        a = b
        b = buf
    for i in range(0,a):
        chromosom_new.append(chromosom[i])
    iterator = 1
    for i in range(a,b):
        chromosom_new.append(chromosom[b-iterator])
        iterator += 1
    for i in range(b,N):
        chromosom_new.append(chromosom[i])
    return chromosom_new

def inserting(chromosom):
    chromosom_new = []
    a = random.randint(0, N-1)
    while True:
        b = random.randint(0, N-1)
        if b != a:
            break
    if b < a:
        buf = a
        a = b
        b = buf
    for i in range(0,a):
        chromosom_new.append(chromosom[i])
    for i in range(a,b):
        chromosom_new.append(chromosom[i+1])
    chromosom_new.append(chromosom[a])
    for i in range(b+1,N):
        chromosom_new.append(chromosom[i])
    return chromosom_new

def transfer(chromosom):
    chromosom_new = []
    a = random.randint(0, N-1)
    while True:
        b = random.randint(0, N-1)
        if b != a:
            break
    if b < a:
        buf = a
        a = b
        b = buf
    while True:
        c = random.randint(0,N-1)
        if (N-b) > c:
            break
    for i in range(0, a):
        chromosom_new.append(chromosom[i])
    for i in range(a, b):
        chromosom_new.append(chromosom[i + c])
    iterator = 0
    for i in range(b, b+c):
        chromosom_new.append(chromosom[a+iterator])
        iterator += 1
    for i in range(b+c, N):
        chromosom_new.append(chromosom[i])
    return chromosom_new

def swap(chromosom):
    chromosom_new = []
    a = random.randint(0, N-1)
    while True:
        b = random.randint(0, N-1)
        if b != a:
            break
    if b < a:
        buf = a
        a = b
        b = buf
    for i in range(0,a):
        chromosom_new.append(chromosom[i])
    chromosom_new.append(chromosom[b])
    for i in range(a+1,b):
        chromosom_new.append(chromosom[i])
    chromosom_new.append(chromosom[a])
    for i in range(b+1,N):
        chromosom_new.append(chromosom[i])
    return chromosom_new

def mutation(parents):
    childs = []
    for i in xrange(len(parents)):
        chromosom = parents[i]
        '''
        x = random.uniform(0,1)
        if x>0.2:
            chromosom_new = transfer(chromosom)
        else:
            chromosom_new = chromosom

        '''
        x = random.randint(1,4)
        if x == 1:
            chromosom_new = inversion(chromosom)
        elif x == 2:
            chromosom_new = inserting(chromosom)
        elif x == 3:
            chromosom_new = transfer(chromosom)
        elif x == 4:
            chromosom_new = swap(chromosom)


        childs.append(chromosom_new)
    return childs


def run():
    Jmax = []
    Javg = []
    u = prepareU()
    for i in range(0, 100):
        distribution, J = calculateVariables(u)
        parents = roulette(u, distribution)
        childs = crossover(parents)
        childs2 = mutation(childs)
        u = childs2
        Jmax.append(max(J))
        Javg.append(sum(J)/len(J))
    print max(Jmax)
    plt.plot(xrange(len(Jmax)), Jmax, 'r')
    plt.plot(xrange(len(Javg)), Javg, 'b')
    plt.title("Najlepsze kryteria jakosci sterowania w kolejnych iteracjach")
    plt.xlabel("Iteracje")
    plt.ylabel("Jmax")
    plt.show()

run()
