"""
limpiar_hemoglobina.py
Script para limpiar secuencia FASTA de hemoglobina (Ejercicio 2).
- Elimina: header (>...), espacios, saltos de línea.
- Deja solo aa continuos.
- Verifica longitud 147.
"""

sec_limpia = ""
with open('hemoglobin_seq.txt', 'r') as f:
    for linea in f:
        linea = linea.strip()  # Quita espacios/saltos
        if not linea.startswith('>'):  # Salta header FASTA
            sec_limpia += linea.upper()  # Concatena, mayúsculas

# Guarda archivo limpio (una sola línea)
with open('hemoglobin_clean.txt', 'w') as f:
    f.write(sec_limpia)

print(f"Secuencia limpia guardada: {len(sec_limpia)} aa")
print(f"¿147 aa correctos? {len(sec_limpia) == 147}")
print(f"Primeros 50 aa: {sec_limpia[:50]}")
print("Contenido de hemoglobin_clean.txt:")
print(sec_limpia)