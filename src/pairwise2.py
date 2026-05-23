from itertools import combinations, product

# =========================
# FACTORES DEL SISTEMA
# =========================
parametros = {
    "Navegador": ["Chrome", "Firefox", "Edge"],
    "SO": ["Windows", "Linux"],
    "Idioma": ["ES", "EN"]
}

# =========================
# OBTENER TODAS LAS PAREJAS POSIBLES
# =========================
def obtener_pares(parametros):
    pares = set()

    keys = list(parametros.keys())

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            p1 = keys[i]
            p2 = keys[j]

            for v1 in parametros[p1]:
                for v2 in parametros[p2]:
                    pares.add(((p1, v1), (p2, v2)))

    return pares


# =========================
# GENERAR CASOS BASE
# =========================
def generar_candidatos(parametros):
    keys = list(parametros.keys())
    valores = list(parametros.values())
    return list(product(*valores))


# =========================
# ELEGIR CASOS QUE CUBRAN PARES
# =========================
def pairwise_selection(parametros):
    pares_objetivo = obtener_pares(parametros)
    candidatos = generar_candidatos(parametros)

    seleccionados = []
    cubiertos = set()

    while pares_objetivo:
        mejor = None
        mejor_cobertura = set()

        for caso in candidatos:
            cobertura = set()

            for i in range(len(parametros)):
                for j in range(i + 1, len(parametros)):
                    k1 = list(parametros.keys())[i]
                    k2 = list(parametros.keys())[j]

                    par = (
                        (k1, caso[i]),
                        (k2, caso[j])
                    )

                    if par in pares_objetivo:
                        cobertura.add(par)

            if len(cobertura) > len(mejor_cobertura):
                mejor = caso
                mejor_cobertura = cobertura

        if not mejor:
            break

        seleccionados.append(mejor)
        pares_objetivo -= mejor_cobertura

    return seleccionados


# =========================
# EJECUCIÓN
# =========================
casos = pairwise_selection(parametros)

print("\n=== CASOS PAIRWISE GENERADOS ===\n")

for i, caso in enumerate(casos, 1):
    print(f"Caso {i}")
    for key, value in zip(parametros.keys(), caso):
        print(f"  {key}: {value}")
    print()

print("=================================")
print("Total casos Pairwise:", len(casos))
