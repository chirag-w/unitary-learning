#Construct the database of input states and outputs described in Eq. 7 of 'Learning to predict arbitrary quantum processes',Huang, Chen and Preskill
from util import *

def construct_dataset(N,U):
    input_states = np.random.randint(0,6,N)
    output_states = random_pauli_meas(apply_unitary(U,input_states))
    return input_states,output_states

def apply_unitary(U,states):
    out_states = []
    U_dag = U.conjugate().transpose()
    for state in states:
        out_states.append(U @ pauli_states[state] @ U_dag)
    return out_states

def random_pauli_meas(states):
    N = len(states)
    bases = np.random.randint(0,3,N)
    res = []
    for i in range(len(states)):
        ind = [2*bases[i],2*bases[i]+1]
        p0 = np.trace(pauli_states[ind[0]]@states[i]).real
        p1 = np.trace(pauli_states[ind[1]]@states[i]).real
        outcome = np.random.choice([0,1],p = [p0,p1])
        res.append(2*bases[i]+outcome)
    return np.array(res)

U = np.eye(2)
inp,out = construct_dataset(30,U)
print(inp)
print(out)