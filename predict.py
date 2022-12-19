from coeff import *

def pred(coeff,rho):
    #Temporary function for predictions
    #Directly computes trace instead of using k-RDMs
    sum = 0
    for P in coeff:
        prod = coeff[P]
        obs = 1
        for i in range(len(P)):
            obs = np.kron(obs,pauli_obs[int(P[i])])
        sum+= prod*np.trace(obs@rho)
    return sum.real

def actual_value(O,U,rho):
    #This function computes trace(O(U * rho * U^dag))
    #O in the input is given as a dictionary
    Udg = U.conjugate().transpose()
    output_state = U @ rho @ Udg
    sum = 0
    for P in O:
        prod = O[P]
        obs = 1
        for i in range(len(P)):
            obs = np.kron(obs,pauli_obs[int(P[i])])
        
        sum+= prod*np.trace(obs@output_state)
    return sum.real



        