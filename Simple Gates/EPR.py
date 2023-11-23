# =======  HEADER =========
from qat.lang.AQASM import Program, H, CNOT
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
H(qubits[0])
CNOT(qubits[0], qubits[1])
#CNOT(qubits[1], qubits[0])

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

# El EPR permite realizar una entrelazamiento entre dos qubits.

# El estado inicial es 00, al aplicar la puerta H en el primer qubit, el estado pasa a ser 01 o 00 
# con una probabilidad del 50% para cada uno de ellos, al aplicar la puerta CNOT el estado final es 00 o 11
# con una probabilidad del 50% para cada uno de ellos debido a que al haber  superposicion el qbit 0 
# puede encontrase en 0 o en 1 con la misma probabilidad haciendo que se aplique o no la CNOT.

