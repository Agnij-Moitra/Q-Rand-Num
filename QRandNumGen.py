import qiskit as q
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
        qc.h(i)
        qc.measure(i, i)

    # executing circuit
    result = q.execute(qc, bk, shots=1).result()

    # the bitstring
    counts = result.get_counts(qc)
    ans = int(list(counts)[0])

    if len(str(ans)) < bitstring - 1:
        buffer = ""
        for i in range(bitstring):
            buffer += "0"
        ans = buffer + str(ans)
        ans = int(ans)

    return ans
