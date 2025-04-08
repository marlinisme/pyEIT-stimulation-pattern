from pyeit.eit import protocol

# Adjacent stimulation (default in pyEIT)
protocol_adj = protocol.create(
    n_el=16,          # Number of electrodes (e.g., 16)
    dist_exc=1,       # Adjacent excitation (E1→E2, E2→E3, etc.)
    step_meas=1,      # Measure adjacent voltages (skip injection pair)
    parser_meas="std" # Standard measurement parser
)
# Print excitation pairs for adjacent protocol
print("Adjacent excitation pairs:")
print(protocol_adj.ex_mat)

print("Adjacent measurement pairs:")
print(protocol_adj.meas_mat)
## ----------------------------------------------------------------------------
# Adjacent skip stimulation (default in pyEIT)
protocol_adj_skip = protocol.create(
    n_el=16,          # Number of electrodes (e.g., 16)
    dist_exc=4,       # skip 3 (inject into electrodes 3 steps apart)
    step_meas=1,      # Measure adjacent voltages (skip injection pair)
    parser_meas="std" # Standard measurement parser
)
# Print excitation pairs for adjacent protocol
print("Adjacent excitation pairs:")
print(protocol_adj_skip.ex_mat)

print("Adjacent measurement pairs:")
print(protocol_adj_skip.meas_mat)
## ----------------------------------------------------------------------------
# Opposite stimulation (for 16 electrodes, E1→E9, E2→E10, etc.)
protocol_opp = protocol.create(
    n_el=16,          # Number of electrodes (must be even for opposite pairs)
    dist_exc=8,       # Opposite excitation (E1→E9 if n_el=16)
    step_meas=1,      # Measure adjacent voltages
    parser_meas="std"
)
# Print excitation pairs for adjacent protocol
print("Opposite excitation pairs:")
print(protocol_opp.ex_mat)

print("Opposite measurement pairs:")
print(protocol_opp.meas_mat)
## ----------------------------------------------------------------------------
# Opposite skip stimulation (for 16 electrodes, E1→E9, E2→E10, etc.)
protocol_opp_skip = protocol.create(
    n_el=16,          # Number of electrodes (must be even for opposite pairs)
    dist_exc=8,       # Opposite excitation (E1→E9 if n_el=16)
    step_meas=8,      # Measure opposite
    parser_meas="std"
)
# Print excitation pairs for adjacent protocol
print("Opposite excitation pairs:")
print(protocol_opp_skip.ex_mat)

print("Opposite measurement pairs:")
print(protocol_opp_skip.meas_mat)
## ----------------------------------------------------------------------------
import numpy as np
from pyeit.eit import protocol

def quasi_adjacent_pairs(n_el):
    """Generate custom quasi-adjacent excitation and measurement pairs."""
    ex_mat = []
    meas_mat = []
    
    # Generate all possible injection pairs (Ei-Ej, where j > i)
    for i in range(n_el):
        for j in range(i + 1, n_el):
            ex_mat.append([i, j])
            
            # Measurement pair: (E(i-1) mod N, E(j+1) mod N)
            meas_1 = (i - 1) % n_el
            meas_2 = (j + 1) % n_el
            meas_mat.append([meas_1, meas_2])
    
    return np.array(ex_mat), np.array(meas_mat)

# Example: 16 electrodes
n_el = 16
ex_matqa, meas_matqa = quasi_adjacent_pairs(n_el)

# Create the custom protocol
protocol_quasi = protocol.create(
    n_el=n_el,
    dist_exc=1,       # Not used, but required
    step_meas=1,      # Not used, but required
    parser_meas="std"
)

protocol_quasi.ex_mat = ex_matqa    # Assign custom excitation pairs
protocol_quasi.meas_mat = meas_matqa  # Assign custom measurement pairs

# Print excitation pairs for Quasi adjacent protocol
print("Quasi adjacent excitation pairs:")
print(protocol_quasi.ex_mat)
print("Quasi adjacent measurement pairs:")
print(protocol_quasi.meas_mat)

# # Print the first 5 injection-measurement pairs
# print("Excitation Pairs (First 5):")
# print(ex_mat[:5])
# print("\nMeasurement Pairs (First 5):")
# print(meas_mat[:5])


