from typing import Optional, Callable, List, Union
from qat.lang.AQASM import Program


class HGate():
    def __init__(self, label: Optional[str] = None, duration=None, unit=None, _condition=None):
        if unit is None:
            unit = "dt"
        super().__init__(
            "h", 1, [], label=label, _condition=_condition, duration=duration, unit=unit
        )
    
    def _define(self):
        q = QuantumRegister(1, "q")
        qc = QuantumCircuit(q, name=self.name)
        rules = [(U2Gate(0, pi), [q[0]], [])]
        for instr, qargs, cargs in rules:
            qc._append(instr, qargs, cargs)

        self.definition = qc

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

    def inverse(self):
        r"""Return inverted H gate (itself)."""
        return HGate()  # self-inverse
    
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
        q = QuantumRegister(2, "q")
        qc = QuantumCircuit(q, name=self.name)
        rules = [
            (SGate(), [q[1]], []),
            (HGate(), [q[1]], []),
            (TGate(), [q[1]], []),
            (CXGate(), [q[0], q[1]], []),
            (TdgGate(), [q[1]], []),
            (HGate(), [q[1]], []),
            (SdgGate(), [q[1]], []),
        ]
        for instr, qargs, cargs in rules:
            qc._append(instr, qargs, cargs)

        self.definition = qc

    def inverse(self):
        """Return inverted CH gate (itself)."""
        return CHGate(ctrl_state=self.ctrl_state)  # self-inverse