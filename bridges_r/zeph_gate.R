# ZEPH-GATE R — decisao trivalente com recibo selado (sha3-256 via openssl CLI).
# Canon: JSON compacto com chaves ordenadas, sem espaços.
canon_scalar <- function(x) { if (is.character(x)) paste0('"', x, '"') else format(x, digits=15, trim=TRUE, scientific=FALSE) }
canon <- function(rec) paste0("{", paste(sprintf('"%s":%s', names(rec), sapply(rec, canon_scalar)), collapse=","), "}")
zeph_seal <- function(rec) {
  con <- pipe("openssl dgst -sha3-256", "w")
  cat(canon(rec), file=con); close(con) -> h
  h
}
decide_zeph <- function(p, shots, margin=0.15) {  # margem declarada ANTES do dado
  if (shots < 1) v <- "REFUSED_INSUFFICIENT_CONFIDENCE"
  else if (p >= 1 - margin) v <- "1"
  else if (p <= margin) v <- "REFUSED_BALANCED"
  else v <- "REFUSED_INSIDE_NOISE_BAND"
  rec <- list(modulo="zeph_gate_r", p=p, shots=shots, margem_declarada=margin, veredito=v)
  rec$selo_sha3_256 <- zeph_seal(rec)
  rec
}
