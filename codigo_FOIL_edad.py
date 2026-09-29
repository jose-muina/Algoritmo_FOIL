import math

# Datos
datos = [
    {"edad": 20, "ocupacion": "estudiante", "educacion": "secundaria", "alumno": True},
    {"edad": 22, "ocupacion": "estudiante", "educacion": "terciario", "alumno": True},
    {"edad": 19, "ocupacion": "estudiante", "educacion": "terciario", "alumno": True},
    {"edad": 35, "ocupacion": "ingeniero", "educacion": "universidad", "alumno": False},
    {"edad": 40, "ocupacion": "profesor", "educacion": "maestria", "alumno": False},
    {"edad": 28, "ocupacion": "administrativo", "educacion": "universidad", "alumno": False},
    {"edad": 21, "ocupacion": "estudiante", "educacion": "terciario", "alumno": True},
    {"edad": 23, "ocupacion": "estudiante", "educacion": "universidad", "alumno": False},
]

# Valores antes de aplicar la condición
P = sum(1 for d in datos if d["alumno"])
N = sum(1 for d in datos if not d["alumno"])

# Aplicar condición: ocupación == "estudiante"
filtrados = [d for d in datos if d["ocupacion"] == "estudiante"]
p = sum(1 for d in filtrados if d["alumno"])
n = sum(1 for d in filtrados if not d["alumno"])

# Cálculo FOIL Gain
def log2_safe(x):
    return math.log2(x) if x > 0 else float('-inf')

foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print(f"P = {P}, N = {N}")
print(f"p = {p}, n = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")
