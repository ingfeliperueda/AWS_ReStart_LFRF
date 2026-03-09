"""
hemoglobin_analysis.py
Script para analizar la secuencia de hemoglobina humana (subunidad beta, 147 aa).
- Muestra info básica de la secuencia.
- Calcula composición de aminoácidos.
- Calcula peso molecular con función reutilizable.
- Calcula % de aminoácidos hidrofóbicos (A,V,I,L,M,F,W,Y).
- Guarda resultados en hemoglobin_results.json.
Autor: Adaptado para ejercicio bioinformático.
Fecha: Marzo 2026.
"""

import json
from collections import Counter

# Leer secuencia limpia (solo aminoácidos, sin headers/españoles/saltos)
with open('hemoglobin_clean.txt', 'r') as f:
    seq = f.read().strip().upper()  # Limpia residuos, asegura mayúsculas

# Ejercicio 4: Mostrar información importante
print(f"Nombre de la proteína: Hemoglobina humana (subunidad beta)")
print(f"Longitud de la secuencia: {len(seq)} aminoácidos")
print(f"Confirmado 147 aa: {len(seq) == 147}")
print(f"Aminoácidos únicos: {sorted(set(seq))}")
print(f"Secuencia completa: {seq[:50]}... (total {len(seq)} aa)")

# Ejercicio 5: Composición de aminoácidos
todos_aa = 'ACDEFGHIKLMNPQRSTVWY'  # 20 aa estándar
count_aa = Counter(seq)
composicion = {aa: count_aa.get(aa, 0) for aa in todos_aa}
print("\nComposición de aminoácidos:")
for aa, cnt in sorted(composicion.items()):
    print(f"{aa}: {cnt}")

# Diccionario de pesos moleculares (Da, residuos libres estándar)[web:45]
pesos_aa = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09, 'C': 103.14,
    'Q': 128.13, 'E': 129.12, 'G': 57.05, 'H': 137.14, 'I': 113.16,
    'L': 113.16, 'K': 128.17, 'M': 131.19, 'F': 147.18, 'P': 97.12,
    'S': 87.08, 'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13
}

# Ejercicio 7: Función reutilizable para peso molecular
def calcular_peso_molecular(secuencia, pesos):
    """
    Calcula peso molecular total de una secuencia proteica.
    Args:
        secuencia (str): Secuencia de aa.
        pesos (dict): Pesos por aa.
    Returns:
        float: Peso en Da.
    """
    cnt = Counter(secuencia)
    return sum(cnt.get(aa, 0) * peso for aa, peso in pesos.items())

peso_mol = calcular_peso_molecular(seq, pesos_aa)
print(f"\nPeso molecular: {peso_mol:.2f} Da")  # ~15.98 kDa[web:48][code_file:1]

# Ejercicio 9: % aminoácidos hidrofóbicos
hidrofobicos = set('AVILMFWY')
total_hidro = sum(count_aa.get(aa, 0) for aa in hidrofobicos)
porc_hidro = (total_hidro / len(seq)) * 100
print(f"Aminoácidos hidrofóbicos: {total_hidro} ({porc_hidro:.1f}%)")

# Ejercicio 8: Guardar en JSON
resultados = {
    "nombre_proteina": "Hemoglobina humana (subunidad beta)",
    "longitud_secuencia": len(seq),
    "composicion_aminoacidos": dict(composicion),
    "peso_molecular_da": round(peso_mol, 2)
}
with open('hemoglobin_results.json', 'w') as f:
    json.dump(resultados, f, indent=4)
print("\nResultados guardados en hemoglobin_results.json")