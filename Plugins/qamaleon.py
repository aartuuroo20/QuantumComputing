from qat.core import HardwareSpecs, Topology, TopologyType
from qat.core.quameleon import QuameleonPlugin
from qat.qpus import get_default_qpu

my_custom_specs = HardwareSpecs(nbqbits=12, topology=Topology(type=TopologyType.LNN))

qpu = QuameleonPlugin(specs=my_custom_specs) | get_default_qpu()

qpu_specs = qpu.get_specs()
print("Default specs of LinAlg:", get_default_qpu().get_specs())
print("Our specs:", qpu)