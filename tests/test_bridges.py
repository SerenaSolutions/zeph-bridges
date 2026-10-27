import sys, os, csv, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zeph_bridges.core import seal
from zeph_bridges.numpy_bridge import decide_numpy
from zeph_bridges.csv_bridge import decide_csv
from zeph_bridges.sklearn_bridge import decide_sklearn

def test_numpy_forte_confirma():
    r = decide_numpy([1.0]*300, threshold=0.5)
    assert r["veredito"] == "1" and len(r["selo_sha3_256"]) == 16

def test_numpy_cinzento_recusa():
    r = decide_numpy([1.0]*150 + [0.0]*150, threshold=0.5)
    assert r["veredito"] == "REFUSED_INSIDE_NOISE_BAND"

def test_csv_ponte():
    fd, p = tempfile.mkstemp(suffix=".csv"); os.close(fd)
    with open(p, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["valor"])
        for _ in range(200): w.writerow([0.9])
    r = decide_csv(p, "valor", threshold=0.5)
    assert r["veredito"] == "1"

def test_sklearn_recusa_honesta():
    y = [0,1]*50
    yp = [0,1]*50
    for i in range(25): yp[i] ^= 1          # acuracia real 0.75
    r = decide_sklearn(y, yp, claim_accuracy=0.78)  # diferenca 0.03 < banda 0.05
    assert r["veredito"] == "REFUSED_INSIDE_NOISE_BAND"

def test_sklearn_afirmacao_forte_confirma():
    y = [0,1]*50
    r = decide_sklearn(y, y, claim_accuracy=0.90)  # real 1.0, diferenca 0.10 > banda
    assert r["veredito"] == "1"

def test_cirq_ponte_quantica():
    import cirq
    q = cirq.LineQubit.range(3)
    c = cirq.Circuit([cirq.H(q[0]), cirq.H(q[1]), cirq.H(q[2])])  # uniforme: p0=0.125
    from zeph_bridges.cirq_bridge import decide_cirq
    r = decide_cirq(c, q)
    assert r["veredito"] == "REFUSED_BALANCED" and r["fonte"] == "cirq"
    c2 = cirq.Circuit()  # identidade: |000> puro
    r2 = decide_cirq(c2, q)
    assert r2["veredito"] == "1"
