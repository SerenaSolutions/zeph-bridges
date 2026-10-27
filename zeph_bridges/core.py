# -*- coding: utf-8 -*-
"""Núcleo comum das pontes ZEPHIRUM: margem declarada ANTES do dado,
veredito trivalente e recibo selado Z-QEA (SHA3-256, canon)."""
import hashlib, json, math
from datetime import datetime, timezone

def declare(margin=0.15, epsilon=0.05, family=1):
    """Sela a regra antes de qualquer dado. Anti-peeking por construção."""
    return {"margin": margin, "epsilon": epsilon, "family": family,
            "min_shots_hoeffding": math.ceil(math.log(1 / (epsilon / family)) / (2 * margin * margin))}

def trivalent(p, rule, shots):
    if shots < 1: return "REFUSED_INSUFFICIENT_CONFIDENCE"
    m = rule["margin"]
    if p >= 1 - m: return "1"
    if p <= m: return "REFUSED_BALANCED"
    return "REFUSED_INSIDE_NOISE_BAND"

def seal(verdict, p, shots, rule, source):
    rec = {"veredito": verdict, "p": round(float(p), 6), "shots": shots,
           "regra": rule, "fonte": source,
           "data": datetime.now(timezone.utc).isoformat()[:19]}
    canon = json.dumps(rec, sort_keys=True, ensure_ascii=True, default=str)
    rec["selo_sha3_256"] = hashlib.sha3_256(canon.encode()).hexdigest()[:16]
    return rec
