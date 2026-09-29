# Simulación de un conjunto de datos realista con personas y sus atributos
datos = [
    {"edad": 20, "ocupacion": "estudiante",     "educacion": "secundaria",  "alumno": True},
    {"edad": 22, "ocupacion": "estudiante",     "educacion": "terciario",   "alumno": True},
    {"edad": 19, "ocupacion": "estudiante",     "educacion": "terciario",   "alumno": True},
    {"edad": 35, "ocupacion": "ingeniero",      "educacion": "universidad", "alumno": False},
    {"edad": 40, "ocupacion": "profesor",       "educacion": "maestria",    "alumno": False},
    {"edad": 28, "ocupacion": "administrativo", "educacion": "universidad", "alumno": False},
    {"edad": 21, "ocupacion": "estudiante",     "educacion": "terciario",   "alumno": True},
    {"edad": 23, "ocupacion": "estudiante",     "educacion": "universidad", "alumno": False},
]

# Separar ejemplos positivos y negativos
positivos = [p for p in datos if p["alumno"]]
negativos = [p for p in datos if not p["alumno"]]

# Algoritmo FOIL simplificado: inducir condiciones que aparecen en positivos pero no en negativos
def inducir_regla(positivos, negativos):
    atributos = ["edad", "ocupacion", "educacion"]
    regla = {}

    for atributo in atributos:
        valores_pos = set(p[atributo] for p in positivos)
        valores_neg = set(p[atributo] for p in negativos)
 
        # Para edad, usamos valores numéricos, así que buscamos intersección mínima
        if atributo == "edad":
            valores_validos = [v for v in valores_pos if v not in valores_neg]
        else:
             valores_validos = list(valores_pos - valores_neg)

        if valores_validos:
            regla[atributo] = valores_validos

    return regla

# Ejecutar el algoritmo
regla_inducida = inducir_regla(positivos, negativos)

# Mostrar la regla
print("Regla inducida para identificar a un alumno:")
for atributo, valores in regla_inducida.items():
    print(f"- {atributo} debe ser uno de: {valores}")

