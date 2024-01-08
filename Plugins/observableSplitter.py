from qat.lang.AQASM import *
from qat.core import Observable, Term
from qat.plugins import ObservableSplitter
from qat.qpus import get_default_qpu

prog = Program()
qbits = prog.qalloc(2)
prog.apply(H, qbits[0])
prog.apply(CNOT, qbits)
bell = prog.to_circ()

obs = Observable(2, pauli_terms=[Term(-0.5, "ZZ", [0, 1])],
                 constant_coeff=0.5)
print("Observable:\n", obs)
my_job = bell.to_job(observable=obs)

result = get_default_qpu().submit(my_job)
print("Resultado de ejecuccion directamente por QPU:", result.value)

stack = ObservableSplitter() | get_default_qpu()
print("Resultado con el plugin:", stack.submit(my_job).value)