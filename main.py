from predict import *

#Unitary to be predicted
n = 6
# U = np.zeros((2**n,2**n))
# for i in range(2**n):
#     U[i][2**n-i-1] = 1

U = np.eye(2**n)

# H = np.array([[1,1],[1,-1]])/np.sqrt(2)
# U = [1]
# for i in range(n):
#     U = np.kron(U,H)

# O = {'111111':1,'222222':1,'333333':1,'000000':1}
O = {'333333':1}

#Target state distribution
D = []
size_D = 100
#Uniformly-random product states
print('D is a set of',size_D,' uniformly random',n,'-qubit BB84 product states')
for i in range(size_D):
    rho = [1]
    indices = np.random.randint(0,6,n)
    for i in range(n):
        rho = np.kron(rho,pauli_states[indices[i]])
    D.append(rho)

#Maximally mixed state
    # rho = np.eye(2**n)/2**n

#GHZ State
    # rho = np.zeros(U.shape, dtype = complex)
    # rho[0][0] = rho[2**n-1][2**n-1] = rho[2**n-1][0] = rho[0][2**n-1] = 0.5

step = 10
N_min = 10
N_max = 500
k = 1

for N in range(N_min,N_max+1,step):
    x = learn(U,O,N,n,k)
    error = 0.0
    for rho in D:
        pred_val = pred(x,rho)
        # print('Predicted value:',pred_val)

        true_val = actual_value(O,U,rho)
        # print('True value:',true_val)
        
        error += (true_val-pred_val)**2
    error /= size_D
    print("N = ",N,", error = ",error)



