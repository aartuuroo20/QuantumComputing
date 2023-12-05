from qat.lang.AQASM import *
from qat.lang.AQASM.qftarith import add
from qat.plugins import CircuitInliner
from qat.core import Batch
from qat.core.util import extract_syntax

def print_main(circuit):
    for op in circuit.ops:
        print(extract_syntax(circuit.gateDic[op.gate], circuit.gateDic), op.qbits)
        
prog = Program()
qbits = prog.qalloc(4)

H(qbits[0])
X(qbits[1])
prog.apply(add(2, 2), qbits)

circuit = prog.to_circ()

plugin = CircuitInliner()

print("Antes de compilar")
print_main(circuit)
batch = Batch(jobs=[circuit.to_job()])
batch = plugin.compile(batch, None)

print("Despues de compilar")
print_main(circuit)
