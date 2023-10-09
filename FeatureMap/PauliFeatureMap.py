from typing import Optional, Callable, List, Union
import numpy as np
from functools import reduce

from qat.core import Variable
from qat.lang.AQASM import Program
from h import HGate


class PauliFeatureMap:
    
    def __init__(
        self,
        feature_dimension: Optional[int] = None,
        reps: int = 2,
        entanglement: Union[str, List[List[int]], Callable[[int], List[int]]] = "full",
        alpha: float = 2.0,
        paulis: Optional[List[str]] = None,
        data_map_func: Optional[Callable[[np.ndarray], float]] = None,
        parameter_prefix: str = "x",
        insert_barriers: bool = False,
        name: str = "PauliFeatureMap",
    ) -> None:
                
        super().__init__(
            num_qubits=feature_dimension,
            reps=reps,
            rotation_blocks=HGate(),
            entanglement=entanglement,
            parameter_prefix=parameter_prefix,
            insert_barriers=insert_barriers,
            skip_final_rotation_layer=True,
            name=name,
        )

        self._data_map_func = data_map_func or self.self_product
        self._paulis = paulis or ["Z", "ZZ"]
        self._alpha = alpha
    
    help(__init__)
    
    def _parameter_generator(self, rep: int, block: int, indices: List[int]) -> Optional[List[Variable]]:
        params = [self.ordered_parameters[i] for i in indices]
        return params
    
    @property
    def num_parameters_settable(self):
        return self.feature_dimension

    @property
    def paulis(self) -> List[str]:
        return self._paulis
    
    @paulis.setter
    def paulis(self, paulis: List[str]) -> None:
        self._invalidate()
        self._paulis = paulis

    @property
    def alpha(self) -> float:
        return self._alpha
    
    @alpha.setter
    def alpha(self, alpha: float) -> None:
        self._invalidate()
        self._alpha = alpha
    
    @property
    def entanglement_blocks(self):
        return [self.pauli_block(pauli) for pauli in self._paulis]
    
    @entanglement_blocks.setter
    def entanglement_blocks(self, entanglement_blocks):
        self._entanglement_blocks = entanglement_blocks
    
    @property
    def feature_dimension(self) -> int:
        return self.num_qubits
    
    @feature_dimension.setter
    def feature_dimension(self, feature_dimension: int) -> None:
        self.num_qubits = feature_dimension
    
    def _extract_data_for_rotation(self, pauli, x):
        where_non_i = np.where(np.asarray(list(pauli[::-1])) != "I")[0]
        x = np.asarray(x)
        return x[where_non_i]
    
    def pauli_block(self, pauli_string):
        params = pauli_string.get_variables() #getVariables()?
        variablesList = list(params)
        time = self._data_map_func(np.asarray(variablesList))
        return self.pauli_evolution(pauli_string, time)

    def pauli_evolution(self, pauli_string, time):
        # for some reason this is in reversed order
        pauli_string = pauli_string[::-1]

        # trim the pauli string if identities are included
        trimmed = []
        indices = []
        for i, pauli in enumerate(pauli_string):
            if pauli != "I":
                trimmed += [pauli]
                indices += [i]

        program = Program()
        evo = program.to_circ()
    
        if len(trimmed) == 0:
            return evo
    
        def basis_change(circuit, inverse=False):
            for i, pauli in enumerate(pauli_string):
                if pauli == "X":
                    circuit.h(i)
                elif pauli == "Y":
                    circuit.rx(-np.pi / 2 if inverse else np.pi / 2, i)
        
        def cx_chain(circuit, inverse=False):
            num_cx = len(indices) - 1
            for i in reversed(range(num_cx)) if inverse else range(num_cx):
                circuit.cx(indices[i], indices[i + 1])
        
        basis_change(evo)
        cx_chain(evo)
        evo.p(self.alpha * time, indices[-1])
        cx_chain(evo, inverse=True)
        basis_change(evo, inverse=True)
        return evo
    
    def self_product(x: np.ndarray) -> float:
        coeff = x[0] if len(x) == 1 else reduce(lambda m, n: m * n, np.pi - x)
        return coeff
    

    