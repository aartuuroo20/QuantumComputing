from numpy import *
import math
from qat.lang.AQASM import Program, H, X, Z, QRoutine, CustomGate
from qat.qpus import get_default_qpu

#We create a matrix class which will be initialized with 0 making a matrix of size number x number also 
#we create a function to fill the diagonal of the matrix with -1 and 1 depending if the number is prime or not
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = zeros((rows, columns))

    def print_matrix(self):
        print(self.matrix)

    def fill_diagonal(self):
        for i in range(len(self.matrix)):
            if i in list:
                self.matrix[i][i] = -1
            else:
                self.matrix[i][i] = 1

qubits = 4
number = 2**qubits
list = []
# We create a list with all the prime numbers from 0 to number 
for num in range(number):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list.append(num)
# We print the list of prime numbers
print(list)

matrix = Matrix(number, number) #We initialize the matrix with size number x number and fill of 0
matrix.print_matrix() #We print the matrix with 0

matrix.fill_diagonal() #We fill the diagonal with -1 and 1

matrix_prime = CustomGate(matrix.matrix) #We create a custom gate with the matrix to be able to use it in the oracle
matrix.print_matrix() #We print the matrix with -1 and 1

#We define the oracle 
def oraculo(k, matrix_prime):
    routine = QRoutine()
    wires = routine.new_wires(k)
    matrix_prime(wires)
    return routine

#We define the difusor
def diffusor(k):
    routine = QRoutine()
    wires = routine.new_wires(k)
    with routine.compute():
        for wire in wires:
            H(wire)
            X(wire)
    Z.ctrl(k - 1)(wires)
    routine.uncompute()
    return routine

m = len(list)
n = number

print("Number of solutions: %d" % m)
k = int(math.pi / (4 * arccos(sqrt(1 - m / n))))
print("Number of iterations: %d" % k)

probability = sin((2 * k + 1) * arccos(sqrt((n - m) / n)))**2
print("Probability of finding a solution: %f" %probability)

qprog = Program()
nqbits = qprog.qalloc(qubits)

difusor = diffusor(qubits)
oracle = oraculo(qubits, matrix_prime)

for qbit in nqbits:
    H(qbit)

for _ in range(k):
    oracle(nqbits)
    difusor(nqbits)
    
circuit = qprog.to_circ()
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

circuit.display()












