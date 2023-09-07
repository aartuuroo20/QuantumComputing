# ----------------------------------------------------------------------
# myQLM - Hello Quantum World
# ----------------------------------------------------------------------
# Andrés Bravo Montes
# Atos Iberia
# BDS HPC & Quantum
# Curso de Formación Básico
# Created 21/02/2023
# Version: v1.0 
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Puerta Cuántica CNOT (Declaración del circuito cuántico)
# ----------------------------------------------------------------------

# =======  HEADER =========
from qat.lang.AQASM import Program, CNOT, X
from qat.qpus import get_default_qpu


# =======  BEGIN =========
# Declaramos un programa
qprogram = Program()

# Inicializamos el número de qubits y cbits
nqubits = 2

# =======  BODY =========
# Asignamos los qubits
qubits=qprogram.qalloc(nqubits)

# Asignamos las puertas cuánticas 
#X(qubits[0])
#X(qubits[1])
CNOT(qubits[0], qubits[1])

# Exportamos este programa a un circuito cuántico
circuit = qprogram.to_circ()

# Visualizamos el circuito
circuit.display()

# Creamos una unidad de proceso cuántico
qpu = get_default_qpu()

# =======  BODY =========
# Creamos un job
job = circuit.to_job()

# Enviamos el job a la QPU
result = qpu.submit(job)

# Iteramos sobre el vector de estado para obtener la probabilidad
for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

#La puerta CNOT solo puede actuar cuando tenemos como minimo dos qubits,
#uno actua como control y el otro como objetivo, 
# unicamente actua cuando control vale 1 realizando una operacion X en el objetivo.

#Al tener dos qbits y unicamente actuar cuando control es 1 sabemos que la probabilidad sera del 100% 
#de que el estado final sea 11, ya que el estado inicial es 00 y al aplicar la puerta CNOT el estado final es 11.
