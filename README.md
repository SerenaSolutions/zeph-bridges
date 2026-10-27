# zeph-bridges

**ZEPHIRUM universal bridges — trivalent decisions (1 / 0 / REFUSED) with sealed
receipts for quantum AND classical stacks.**

Every bridge declares the margin BEFORE the data, returns a trivalent verdict,
and seals a Z-QEA receipt (SHA3-256 canonical). No binary green-washing.

## Quantum bridges
- `cirq_bridge` — Cirq circuits -> trivalent verdict + receipt
- PennyLane -> https://github.com/SerenaSolutions/pennylane-zephirum
- Qiskit + OpenQASM 3 -> native in https://github.com/SerenaSolutions/zephirum-lang

## Classical bridges
- `numpy_bridge` — samples/threshold decisions from any numeric pipeline
- `csv_bridge` — plain spreadsheets: column in, sealed verdict out
- `sklearn_bridge` — statistical sign-off of model claims ("accuracy >= X")

## Usage
```python
from zeph_bridges.numpy_bridge import decide_numpy
r = decide_numpy(samples, threshold=0.5)
print(r["veredito"], r["selo_sha3_256"])   # 1 / 0 / REFUSED + seal
```

MIT. Author: Maria Clara dos Anjos (SerenaSolutions).
