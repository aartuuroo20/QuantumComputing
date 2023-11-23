

# =======  HEADER =========
from qat.lang.AQASM import Program, H
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
H(qubits[0])

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

#La superposicion explicar que un qbit puede exitir en multiples estados a la vez, 
# con diferentes probabilidades de ser medido en cada uno de ellos.

#La puerta de Hadamard realiza la superposicion de los estados,
# redistribuyendo la probabilidad de ambos sea 50% y 50%, los decimales que se pierden es por el HW.

#Por principios de mecanica cuantica es probabilistico, hciendo que se colapse a un estado dado 
# intentando hacer que colapse a 1, valoramos resultado.


#LIBRO BIBLIA CUANTICA