# -*- coding: utf-8 -*-
"""Ponte ZEPHIRUM - AWS Braket: circuitos Braket entram, veredito trivalente sai."""
from .core import declare, trivalent, seal

def decide_braket(circuit, margin=0.15, epsilon=0.05, shots=4096, name="braket_decision"):
    """ circuit: braket.circuits.Circuit ; margem declarada ANTES do dado."""
    from braket.devices import LocalSimulator
    rule = declare(margin=margin, epsilon=epsilon)   # regra selada antes de rodar
    n = circuit.qubit_count
    counts = LocalSimulator().run(circuit, shots=shots).result().measurement_counts
    p0 = counts.get("0" * n, 0) / float(shots)
    v = trivalent(p0, rule, shots)
    return {"modulo": "zeph_bridges.braket", "fonte": "braket", "name": name,
            **seal(v, p0, shots, rule, "braket")}
