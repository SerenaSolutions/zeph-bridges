# -*- coding: utf-8 -*-
"""Ponte QUÂNTICA Cirq: circuito Cirq → veredito trivalente selado."""
from .core import declare, trivalent, seal

def decide_cirq(circuit, qubits, shots=8192, margin=0.15, epsilon=0.05):
    import cirq, numpy as np
    rule = declare(margin, epsilon)  # regra selada ANTES do dado
    sim = cirq.Simulator(dtype=np.complex128)
    sv = sim.simulate(circuit).final_state_vector
    p0 = float(abs(sv[0]) ** 2)  # amplitude do estado |0...0> nos qubits de decisao
    v = trivalent(p0, rule, shots)
    return seal(v, p0, shots, rule, "cirq")
