# ZEPH-GATE Julia — decisao trivalente com recibo selado (SHA stdlib: sha3_256).
using SHA
canon_scalar(x::AbstractString) = "\"$(x)\""
canon_scalar(x::Number) = string(x)
canon(rec::Dict) = "{" * join(["\"$(k)\":$(canon_scalar(v))" for (k,v) in sort(collect(pairs(rec)))], ",") * "}"
function decide_zeph(p::Float64, shots::Int, margin::Float64=0.15)  # margem declarada ANTES do dado
    v = shots < 1 ? "REFUSED_INSUFFICIENT_CONFIDENCE" :
        p >= 1 - margin ? "1" :
        p <= margin ? "REFUSED_BALANCED" : "REFUSED_INSIDE_NOISE_BAND"
    rec = Dict{String,Any}("modulo"=>"zeph_gate_julia", "p"=>p, "shots"=>shots,
                           "margem_declarada"=>margin, "veredito"=>v)
    rec["selo_sha3_256"] = bytes2hex(sha3_256(canon(rec)))
    rec
end
