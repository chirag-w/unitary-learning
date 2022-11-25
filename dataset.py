#Construct the database of input states and outputs described in Eq. 7 of 'Learning to predict arbitrary quantum processes',Huang, Chen and Preskill
from util import *
from qiskit import QuantumCircuit
from qiskit.extensions import UnitaryGate
from qiskit import Aer

def construct_dataset(U,N,n):
    #Returns a dataset containing the classical description of states before and after the unknown unitary is applied
    #U provided as a matrix
    U = UnitaryGate(U)
    input_states = np.random.randint(0,6,(N,n))
    output_states = apply_unitary_measure(U,input_states)
    return input_states,output_states

def apply_unitary_measure(U,input_states):
    #Apply the unitary gate U
    #and perform random pauli measurement on each qubit
    N = len(input_states)
    n = len(input_states[0])
    bases = np.random.randint(0,3,(N,n)) #Randomly select Pauli measurement bases
    result = np.zeros((N,n), dtype = int)
    for i in range(N):
        qc = QuantumCircuit(n)
        for qubit in range(n):
            state = input_states[i][qubit]
            #Construct state
            if state%2 == 1:
                qc.x(qubit)
            if int(state/2) == 1:
                qc.h(qubit)
            elif int(state/2) == 2:
                qc.h(qubit)
                qc.s(qubit)
        #Apply unitary
        qc.append(U, range(n))
        for qubit in range(n):
            #Apply random Pauli measurement
            if bases[i][qubit] == 1: #Measurement in Z basis
                qc.h(qubit)
            elif bases[i][qubit] == 2: #Measurement in Y basis
                qc.sdg(qubit)
                qc.h(qubit)
            else: #Measurement in X basis
                pass 
        #Measure qubits
        qc.measure_all()
        backend = Aer.get_backend('qasm_simulator')
        job = backend.run(qc, shots=1)
        counts = job.result().get_counts()
        outcome = list(counts.keys())[0][::-1] #Get the outcome and reverse to fix qiskit ordering
        for qubit in range(n):
            if(outcome[qubit] == '1'):
                result[i][qubit] = 2*bases[i][qubit]+1 #Result is already in the right basis, adjust for measurement outcome
            else:
                result[i][qubit] = 2*bases[i][qubit]
    return result

n = 8
N = 10
U = np.eye(2**n)
inp, out = construct_dataset(U, N, n)
for i in range(N):
    print(inp[i])
    print(out[i])
    print()