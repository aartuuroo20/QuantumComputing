import numpy as np
import random
import time
import qat.lang.AQASM as qlm

from qat.lang.models import KPTree
from scipy.stats import norm

def get_theoric_probability(n_qbits: int) -> (np.ndarray, np.ndarray, float, float, float, int):  # type: ignore
    """
    Get the discretization of the PDF for N qubits
    """
    # Randomly generate the mean and sigma
    mean = random.uniform(-2., 2.)
    sigma = random.uniform(0.1, 2.)

    # Create the normal distribution
    norma = norm(loc=mean, scale=sigma)

    # Set the number of intervals depending on the number of qubits       
    intervals = 2 ** n_qbits

    #Create an array of x values with min and max values depending on the number of intervals
    ppf_min = 0.005
    ppf_max = 0.995

    x_ = np.linspace(norma.ppf(ppf_min), norma.ppf(ppf_max), num=intervals)

    # Calculate the width of array
    step = x_[1] - x_[0]

    #Creates de probability density function using array X (each value of X)
    data = norma.pdf(x_)

    # Normalize the data
    data = data/np.sum(data)
    
    #Calculate the number of shots
    mindata = np.min(data)
    shots = min(1000000, round(100/mindata)) #Duda de porque es max(10000, round(100/mindata) y no solo round(100/mindata)

    return x_, data, mean, sigma, float(step), shots, norma

def load_probability(
    probability_array: np.array,
    method: str = "KPTree",
    id_name: str = str(time.time_ns())
):
    """
    Creates a QLM Abstract gate for loading a given discretized probability
    distribution using Quantum Multiplexors.

    Parameters
    ----------
    probability_array : numpy array
        Numpy array with the discretized probability to load. The arity of
        of the gate is int(np.log2(len(probability_array))).
    method : str
        type of loading method used:
            multiplexor : with quantum Multiplexors
            brute_force : using multicontrolled rotations by state
    id_name : str
        name for the Abstract Gate

    Returns
    ----------

    P_Gate :  AbstractGate
        Customized Abstract Gate for Loading Probability array using
        Quantum Multiplexors
    """
    number_qubits = int(np.log2(probability_array.size))

    @qlm.build_gate("P_{" + id_name + "}", [], arity=number_qubits)
    def load_probability_gate():
        """
        QLM Routine generation.
        """
        routine = qlm.QRoutine()
        register = routine.new_wires(number_qubits)
        # Now go iteratively trough each qubit computing the
        # probabilities and adding the corresponding multiplexor
        for m_qbit in range(number_qubits):
            # print(m)
            # Calculates Conditional Probability
            conditional_probability = left_conditional_probability(
                m_qbit, probability_array
            )
            # Rotation angles: length: 2^(i-1)-1 and i the number of
            # qbits of the step
            thetas = 2.0 * (np.arccos(np.sqrt(conditional_probability)))
            if m_qbit == 0:
                # In the first iteration it is only needed a RY gate
                routine.apply(qlm.RY(thetas[0]), register[number_qubits - 1])
            else:
                # In the following iterations we have to apply
                # multiplexors controlled by m_qbit qubits
                # We call a function to construct the multiplexor,
                # whose action is a block diagonal matrix of Ry gates
                # with angles theta
                routine.apply(
                    #multiplexor_ry(thetas),
                    load_angles(thetas, method),
                    register[number_qubits - m_qbit : number_qubits],
                    register[number_qubits - m_qbit - 1],
                )
        return routine

    #Depending on the method, it will return the corresponding routine
    if method == "multiplexor":
        return load_probability_gate()
    elif method == "brute_force":
        return load_probability_gate()
    elif method == "KPTree":
        return KPTree(np.sqrt(probability_array)).get_routine()
    else:
        error_text = "Not valid method argument."\
            "Select between: multiplexor, brute_force or KPTree"
        raise ValueError(error_text)

def get_qlm_probability(data, shots, qpu):
    tick = time.time()
    job = data.to_job(nbshots=shots)
    result = qpu.submit(job)
    #Creame un array con las probabilidades
    data = np.array([])
    for sample in result:
        data = np.append(data, sample.probability)
    
    tack = time.time()
    quantum_time = tack - tick

    return data, quantum_time

    