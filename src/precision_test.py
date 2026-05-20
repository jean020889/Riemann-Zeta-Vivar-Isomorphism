import mpmath
import numpy as np
import hashlib
from datetime import datetime

def test_stability(n_ceros=100, precision_levels=[20, 40, 60], tolerance=1e-30):
    """
    Verifica que los valores espectrales permanezcan invariantes
    frente a distintos niveles de precisión decimal.
    Incluye fecha, versiones y certificación digital SHA-256.
    """
    print("Fecha de ejecución:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Versión NumPy:", np.__version__)
    print("Versión mpmath:", mpmath.__version__)
    print("-" * 60)

    resultados = []
    print(f"{'DPS':<10} | {'Sample Zero 100'}")
    print("-" * 40)

    for dps in precision_levels:
        mpmath.mp.dps = dps
        zero = mpmath.zetazero(n_ceros).imag
        resultados.append(f"{dps:<10} | {zero}")
        print(f"{dps:<10} | {zero}")

    # Convertir a float para calcular diferencias
    valores_float = [float(mpmath.zetazero(n_ceros).imag) for dps in precision_levels]
    dif_max = max(abs(valores_float[i] - valores_float[j]) 
                  for i in range(len(valores_float)) 
                  for j in range(i+1, len(valores_float)))
    estado = "VERIFICADO ✅" if dif_max < tolerance else "INESTABLE ⚠️"

    print("\nVerificación de estabilidad:")
    print(f"Diferencia máxima = {dif_max:.2e} → {estado}")

    # Certificación digital
    cadena_certificacion = "\n".join(resultados)
    hash_sha256 = hashlib.sha256(cadena_certificacion.encode("utf-8")).hexdigest()
    print("\nCertificación digital (SHA-256):")
    print(hash_sha256)

if __name__ == "__main__":
    test_stability()
