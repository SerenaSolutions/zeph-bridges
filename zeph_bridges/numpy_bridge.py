# -*- coding: utf-8 -*-
"""Ponte CLÁSSICA NumPy: amostras numéricas → veredito trivalente selado.
Qualquer pipeline clássico (log, sensor, telemetria) decide com banda declarada."""
from .core import declare, trivalent, seal

def decide_numpy(samples, threshold, shots=None, margin=0.15, epsilon=0.05):
    import numpy as np
    x = np.asarray(samples, dtype=float)
    n = int(x.size) if shots is None else int(shots)
    rule = declare(margin, epsilon)
    hit = float(np.mean((x >= threshold).astype(float)))
    v = trivalent(hit, rule, n)
    return seal(v, hit, n, rule, "numpy")
