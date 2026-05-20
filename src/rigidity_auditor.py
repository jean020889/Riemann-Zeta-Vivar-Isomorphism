import numpy as np
import mpmath
import hashlib
from datetime import datetime

def compute_delta3_table_sha(n_limit=500, L_values=[5, 10, 20, 50, 100]):
    """
    Calcula la estadística Dyson-Mehta Delta_3 para los ceros de Riemann.
    Presenta resultados en tabla y genera un hash SHA-256 como certificación digital.
    Incluye fecha y versiones de librerías.
    """
    # Información de auditoría
    print("Fecha de ejecución:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Versión NumPy:", np.__version__)
    print("Versión mpmath:", mpmath.__version__)
    print("-" * 50)

    mpmath.mp.dps = 40
    ceros = [float(mpmath.zetazero(k).imag) for k in range(1, n_limit + 1)]
    
    def n_bar(t):
        return (t / (2 * np.pi)) * (np.log(t / (2 * np.pi * np.e)))
    
    ceros_norm = np.array([n_bar(c) for c in ceros])
    
    resultados = []
    print(f"{'Window L':<15} | {'Delta_3 Statistic'}")
    print("-" * 40)
    
    for L in L_values:
        delta3_vals = []
        step = max(1, len(ceros_norm)//200)  # muestreo adaptativo
        for i in range(0, len(ceros_norm) - L, step):
            ventana = ceros_norm[i : i + L]
            x = np.arange(L)
            a, b = np.linalg.lstsq(np.vstack([x, np.ones(L)]).T, ventana, rcond=None)[0]
            delta3_vals.append(np.mean((ventana - (a * x + b))**2))
        delta3_value = np.mean(delta3_vals)
        resultados.append(f"{L:<15} | {delta3_value:.6f}")
        print(f"{L:<15} | {delta3_value:.6f}")
    
    # Concatenar resultados y generar hash SHA-256
    cadena_certificacion = "\n".join(resultados)
    hash_sha256 = hashlib.sha256(cadena_certificacion.encode("utf-8")).hexdigest()
    
    print("\nCertificación digital (SHA-256):")
    print(hash_sha256)

if __name__ == "__main__":
    compute_delta3_table_sha()
