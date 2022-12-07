from coeff import *

def pred(coeff,rho):
    #Temporary function for predictions
    #Directly computes trace instead of using k-RDMs
    sum = 0
    for P in coeff:
        prod = coeff[P]
        obs = 1
        for i in range(len(P)):
            obs = obs * pauli_obs[int(P[i])]
        sum+= prod*np.trace(obs@rho)
    return sum
        