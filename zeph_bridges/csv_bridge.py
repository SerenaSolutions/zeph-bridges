# -*- coding: utf-8 -*-
"""Ponte CLÁSSICA CSV: coluna de qualquer planilha → veredito selado.
A linguagem das línguas sem código: o dado entra, a decisão sai."""
import csv
from .core import declare, trivalent, seal

def decide_csv(path, column, threshold, margin=0.15, epsilon=0.05):
    vals = [float(r[column]) for r in csv.DictReader(open(path))]
    rule = declare(margin, epsilon)
    hit = sum(1 for v in vals if v >= threshold) / len(vals)
    v = trivalent(hit, rule, len(vals))
    return seal(v, hit, len(vals), rule, "csv")
