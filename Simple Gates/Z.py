# =======  HEADER =========
from qat.lang.AQASM import Program, Z, X
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
Z(qubits[0])

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