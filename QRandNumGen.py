import qiskit as q
from numpy import pi
from qiskit import *

bk = q.Aer.get_backend("qasm_simulator")


def main(bitstring):
    """
    bitsring is the number of digits that'll be generated
    """

    # initializing qubits
    qc = q.QuantumCircuit(bitstring + 1, bitstring + 1)

    # applying h gate and measuring
    for i in range(bitstring):
        qc.rz(pi / 2, i)
        qc.sxdg(i)
        qc.rz(pi / 2, i)
        qc.measure(i, i)

    # executing circuit
    result = q.execute(qc, bk, shots=1).result()

    # the bitstring
    counts = result.get_counts(qc)
    ans = str(list(counts)[0])

    return ans
