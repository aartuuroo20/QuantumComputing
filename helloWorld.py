from qat.lang import Program, H, CNOT
from qat.qpus import get_default_qpu


prog = Program() 
qbits = prog.qalloc(2)  # Reservamos memoria para 2 qbits
H(qbits[0]) #Creamos una puerta H en qbit0
CNOT(qbits[0], qbits[1]) #Creamos una puerta CNOT en qbit0(control) y qbit1(objetivo)

circ = prog.to_circ() #Creamos el circuito

qpu = get_default_qpu() #Creamos un ordenador quantico
job = circ.to_job() #Creamos un trabajo
result = qpu.submit(job) #Cargamos el trabajo a la QPU

for sample in result:
        print("State %s amplitude %s" % (sample.state, sample.amplitude))

circ.display() #Mostramos el circuito


