const { decideZeph } = require("./zeph_gate.js");
const r1 = decideZeph(0.9718, 8192);          // acima da banda -> 1
const r2 = decideZeph(0.5159, 8192);          // zona cinzenta -> RECUSA
const r3 = decideZeph(0.125, 4096);           // abaixo da banda -> BALANCED
console.log("forte:", r1.veredito, "| cinzento:", r2.veredito, "| balanceado:", r3.veredito);
if (r1.veredito !== "1" || r2.veredito !== "REFUSED_INSIDE_NOISE_BAND" || r3.veredito !== "REFUSED_BALANCED") { console.log("FALHOU"); process.exit(1); }
console.log("PONTE JS OK — 3/3");
