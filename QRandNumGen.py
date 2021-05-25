#%%
import qiskit as q
import numpy as np
bk = q.Aer.get_backend("qasm_simulator")
#%%
def main(bitstring):
    """
    bitsring is the number of digits that'll be generated
    """
    li = np.arange(bitstring)
    # initializing qubits
    qc = q.QuantumCircuit(bitstring, bitstring)
    # adding gates
    qc.h(li)
    # measuring     
    qc.measure(li, li)
    # get the bitstring
    result = q.execute(qc, bk, shots = 1).result()
    # the bitstring
    counts = result.get_counts(qc)
    return int(list(counts)[0])
#%%
