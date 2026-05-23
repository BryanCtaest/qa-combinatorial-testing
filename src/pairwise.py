from itertools import product, combinations

# Parámetros del sistema
parametros = {
    "Navegador": ["Chrome", "Firefox", "Edge"],
    "Sistema Operativo": ["Windows", "Linux"],
    "Idioma": ["Español", "Inglés"]
}

# Generar todas las combinaciones posibles
claves = parametros.keys()
valores = parametros.values()

combinaciones_totales = list(product(*valores))

print("=== CASOS DE PRUEBA GENERADOS ===\n")

for i, caso in enumerate(combinaciones_totales, start=1):
    print(f"Caso {i}:")
    
    for clave, valor in zip(claves, caso):
        print(f"  {clave}: {valor}")
    
    print()

# Mostrar cantidad total
print("=================================")
print(f"Total de casos generados: {len(combinaciones_totales)}")

# Relación matemática
print("\nFundamento lógico:")
print("- Uso de teoría de conjuntos para combinar parámetros.")
print("- Uso de lógica proposicional para validar condiciones.")
