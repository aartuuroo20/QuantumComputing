from typing import Optional, Callable, List, Union
from qat.lang.AQASM import Program, S, T, CNOT, PH, H,CustomGate
import numpy as np

class HGate():
    def __init__(self, label: Optional[str] = None, duration=None, unit=None, _condition=None):
        if unit is None:
            unit = "dt"
        super().__init__(
            #"h", 1, [], label=label, _condition=_condition, duration=duration, unit=unit
        )
    
    def _define(self):
        qprogram = Program()
        q = qprogram.qalloc(1)
        qc = qprogram.to_circ()

        complejo = 1j
        euler = np.exp(np.pi * complejo)

        matrix = np.matrix([[1, -euler], [1, euler]])
        u2Gate = CustomGate(matrix)

        rules = [(u2Gate(q[0]))]
        for instr, qargs, cargs in rules:
            qc._append(instr, qargs, cargs)

        self.definition = qc

    '''
    def control(
        self,
        num_ctrl_qubits: int = 1,
        label: Optional[str] = None,
        ctrl_state: Optional[Union[int, str]] = None,
    ):
        if num_ctrl_qubits == 1:
            gate = CHGate(label=label, ctrl_state=ctrl_state, _base_label=self.label)
            return gate
        return super().control(num_ctrl_qubits=num_ctrl_qubits, label=label, ctrl_state=ctrl_state)
    '''
    
    def inverse(self):
        r"""Return inverted H gate (itself)."""
        return HGate()  # self-inverse

'''
class CHGate():

    def __init__(
        self,
        label: Optional[str] = None,
        ctrl_state: Optional[Union[int, str]] = None,
        _base_label=None,
    ):
        super().__init__(
            "ch",
            2,
            [],
            num_ctrl_qubits=1,
            label=label,
            ctrl_state=ctrl_state,
            base_gate=HGate(label=_base_label),
        )

    def _define(self):
        qprogram = Program()
        q=qprogram.qalloc(2)
        circ = qprogram.to_circ()
        rules = [
            (S(q[0])),
            (HGate(), [q[1]], []),
            (T(q[0])),
            (CNOT(q[0], q[1])),
            (PH(-np.pi/4)(q[1])),
            (HGate(), [q[1]], []),
            (PH(-np.pi/2)(q[1])),
        ]
        for instr, qargs, cargs in rules:
            circ._append(instr, qargs, cargs)

        self.definition = circ

    def inverse(self):
        """Return inverted CH gate (itself)."""
        return CHGate(ctrl_state=self.ctrl_state)  # self-inverse
'''