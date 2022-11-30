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

def coeff_pauli(P,inp,k,obs_val,sum,eps_tilde = 0.001):
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
            coeff += sign*obs_val[l]
    coeff = coeff/N
    mod = mod_pauli(P)
    
    if (1/3)**mod < 2*eps_tilde or abs(coeff) < (2 * (3**(mod/2)) * np.sqrt(eps_tilde) * sum):
        return 0
    return coeff * (3**mod)

def sum_coeff(O):
    #Sum of absolute values of the coefficients of O in the Pauli basis
    sum = 0
    for obs in O:
        sum+= abs(O[obs])
    return sum

def mod_pauli(P):
    #Number of non-identity terms in a Pauli product observable
    count = 0
    for obs in P:
        if obs!='3':
            count+=1
    return count

def shadow_observable(O,shadow):
    #Placeholder function
    N = len(shadow)
    n = len(shadow[0])
    val = np.zeros(N, dtype = float)
    for l in range(N):
        for obs in O:
            prod = O[obs]
            for i in range(n):
                if obs[i] == '3': #If observable is identity, trace is 1
                    continue
                elif str(int(shadow[l][i]/2)) != obs[i]: #If observable doesn't match, trace is -2
                    prod*= -2
                elif shadow[l][i]%2 == 1: #If observable matches but the eigenvalue is negative,  trace is -5
                    prod*= -5
                else: #Observable matches and positive eigenstate, trace is 1
                    continue
            val[l] += prod
    return val


# n = 6
# k = 1
# N = 50
# U = np.eye(2**n)
# inp, out = construct_dataset(U,N,n)
# O = {'133333':1,'313333':1,'331333':1,'333133':1,'333313':1,'333331':1}
# obs_val = shadow_observable(O,out)
# paulis = generate_paulis(inp,n,k)
# x = {}
# sum = sum_coeff(O)
# for P in paulis:
#     coeff = coeff_pauli(P,inp,k,obs_val,sum)
#     if coeff!= 0 :
#         x[P] = coeff
# print(x)