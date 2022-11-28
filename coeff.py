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

# n = 4
# k = 2
# N = 3
# U = np.eye(2**n)
# inp, out = construct_dataset(U,N,n)
# for i in range(N):
#     print(inp[i])
# paulis = generate_paulis(inp,n,k)
# print(paulis)