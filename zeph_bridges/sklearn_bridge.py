# -*- coding: utf-8 -*-
"""Ponte CLÁSSICA scikit-learn: o veredito sobre a AFIRMAÇÃO sobre um modelo.
'minha acurácia >= X' -> 1/0/REFUSED com banda; sem green-washing estatístico."""
from .core import declare, trivalent, seal

def decide_sklearn(y_true, y_pred, claim_accuracy, margin=0.05, epsilon=0.05):
    n = len(y_true)
    rule = declare(margin, epsilon)
    acc = sum(1 for t, p in zip(y_true, y_pred) if t == p) / n
    diff = acc - claim_accuracy
    if diff >= rule["margin"]: v = "1"
    elif -diff >= rule["margin"]: v = "REFUSED_CLAIM_REFUTED"
    else: v = "REFUSED_INSIDE_NOISE_BAND"
    return seal(v, diff, n, rule, "sklearn")
