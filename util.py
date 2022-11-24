import numpy as np

def density_matrix(pure_states):
    #Convert an array of pure states to their density matrix representation
    N = len(pure_states)
    S = []
    for i in range(N):
        S.append(np.outer(pure_states[i],pure_states[i].conjugate()))
    return S

pauli_states = density_matrix([np.array([1,0],dtype = complex),np.array([0,1],dtype = complex),np.array([1/np.sqrt(2),1/np.sqrt(2)],dtype = complex),
    np.array([1/np.sqrt(2),-1/np.sqrt(2)],dtype = complex),np.array([1/np.sqrt(2),1j/np.sqrt(2)],dtype = complex),np.array([1/np.sqrt(2),-1j/np.sqrt(2)],dtype = complex)
    ])