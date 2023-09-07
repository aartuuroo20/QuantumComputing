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
# Puerta Cuántica Hadamard (Declaración del circuito cuántico)
# ----------------------------------------------------------------------

# =======  HEADER =========
from qat.lang.AQASM import Program, X
from qat.qpus import get_default_qpu


# =======  BEGIN =========
# Declaramos un programa
qprogram = Program()

# Inicializamos el número de qubits y cbits
nqubits = 1

# =======  BODY =========
# Asignamos los qubits
qubits=qprogram.qalloc(nqubits)

# Asignamos las puertas cuánticas 
X(qubits[0])

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
    print(sample)
    #Amplitud es un numero complejo formado por parte real e imaginaria, la probabilidad es el modulo al cuadrado de la amplitud
    print("State %s probability %s amplitud %s" % (sample.state, sample.probability, sample.amplitude))

#La puerta Pauli X rota el qubit 180 grados alrededor del eje X, el estado del qbit se inicializa en 0 y al aplicar esta puerta cambia a 1


