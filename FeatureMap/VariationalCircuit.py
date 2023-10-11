from qat.core import Observable as Obs, Term
from qat.lang import Program, RY, CSIGN, RZ
from qat.qpus import get_default_qpu
from qat.plugins import ScipyMinimizePlugin

class VariationalCircuit:
    def __init__(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)
        self.theta = self.qprogram.new_var(float, '\\theta')
        self.CreateVariationalCircuit()

    def CreateVariationalCircuit(self):
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])
        CSIGN(self.qubits[0], self.qubits[1])
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])
        CSIGN(self.qubits[0], self.qubits[1])
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])

    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()


'''
# we instantiate the Hamiltonian we want to approximate the ground state energy of
hamiltonian = (
    Obs.sigma_z(0) * Obs.sigma_z(1)
    + Obs.sigma_x(0) * Obs.sigma_x(1)
    + Obs.sigma_y(0) * Obs.sigma_y(1)
)

# we construct the variational circuit (ansatz)
prog = Program()
reg = prog.qalloc(2)
thetas = [prog.new_var(float, '\\theta_%s'%i) for i in range(2)]
RY(thetas[0])(reg[0])
RY(thetas[1])(reg[1])
CNOT(reg[0], reg[1])
circ = prog.to_circ()

# construct a (variational) job with the variational circuit and the observable
job = circ.to_job(observable=hamiltonian)

# we now build a stack that can handle variational jobs
qpu = get_default_qpu()
optimizer_scipy = ScipyMinimizePlugin(method="COBYLA",
                                        tol=1e-6,
                                        options={"maxiter": 200},
                                        x0=[0, 0])
stack = optimizer_scipy | qpu

# we submit the job and print the optimized variational energy (the exact GS energy is -3)
result = stack.submit(job)
# the output of the optimizer can be found here
print(result.meta_data['optimizer_data'])
print(f"Minimum VQE energy = {result.value}")
'''