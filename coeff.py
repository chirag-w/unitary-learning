from dataset import *
from itertools import *

#Pauli indices
# 0 -> Z
# 1 -> X
# 2 -> Y
# 3 -> I
def generate_paulis(inp,n,k):
    #Generate all Pauli product observables with <= k non-identity terms
    #and tr(P@inp[i])!=0 for some i
    #stored as strings in {0,1,2,3}^n 
    s = ''.join(['3']*n)
    paulis = {s}
    for size in range(k+1):
        for ind in range(len(inp)):
            for posns in combinations(range(n),size):
                s = ['3']*n
                for pos in posns:
                    s[pos] = str(int(inp[ind][pos]/2))
                paulis.add(''.join(s))
    return paulis

def coeff_pauli(P,inp,out,k):
    N = len(inp)
    n = len(inp[0])
    coeff = 0
    for l in range(N):
        zero = False
        sign = 1
        for i in range(n):
            if P[i] != '3' and str(int(inp[l][i]/2)) != P[i]:
                #Trace is zero 
                zero = True
                break
            elif P[i] != '3' and inp[l][i]%2 == 1: 
                #This qubit is in negative eigenstate
                sign *= -1
            else:
                #This state is either in positive eigenstate or the Pauli is identity   
                continue
        if zero:
            continue
        else:
            coeff += sign*quantity()
    coeff = coeff/N
    return coeff

def mod_pauli(P):
    #Number of non-identity terms in a Pauli product observable
    count = 0
    for obs in P:
        if obs!='3':
            count+=1
    return count

def quantity():
    #Placeholder function
    return 0
    


# n = 4
# k = 2
# N = 3
# U = np.eye(2**n)
# inp, out = construct_dataset(U,N,n)
# for i in range(N):
#     print(inp[i])
# paulis = generate_paulis(inp,n,k)
# print(paulis)