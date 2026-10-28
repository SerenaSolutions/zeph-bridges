// ZEPH-GATE JavaScript — decisao trivalente com recibo selado.
// Canon desta ponte: JSON compacto com chaves ordenadas; selo sha3-256.
const crypto = require("crypto");
function canon(o){ if(Array.isArray(o))return "["+o.map(canon)+"]";
  if(o===null||typeof o!=="object")return JSON.stringify(o);
  return "{"+Object.keys(o).sort().map(k=>JSON.stringify(k)+":"+canon(o[k])).join(",")+"}"; }
function seal(rec){ return crypto.createHash("sha3-256").update(canon(rec)).digest("hex"); }
function decideZeph(p, shots, opts){
  opts = opts || {};
  const margin = opts.margin !== undefined ? opts.margin : 0.15; // declarada ANTES do dado
  let verdict;
  if (shots < 1) verdict = "REFUSED_INSUFFICIENT_CONFIDENCE";
  else if (p >= 1 - margin) verdict = "1";
  else if (p <= margin) verdict = "REFUSED_BALANCED";
  else verdict = "REFUSED_INSIDE_NOISE_BAND";
  const rec = { modulo: "zeph_gate_js", p: p, shots: shots, margem_declarada: margin, veredito: verdict };
  rec.selo_sha3_256 = seal(rec);
  return rec;
}
module.exports = { decideZeph, canon, seal };
