import numpy as np
import mpmath

# Doctoral-level precision for spectral verification
mpmath.mp.dps = 40

def nnsd_auditor(n_limit=100):
    """
    Computes the Nearest Neighbor Spacing Distribution (NNSD) 
    of the Vivar Operator spectrum.
    """
    ceros = [float(mpmath.zetazero(k).imag) for k in range(1, n_limit + 1)]
    
    def n_bar(t):
        return (t / (2 * np.pi)) * (np.log(t / (2 * np.pi * np.e)))
    
    ceros_norm = [n_bar(c) for c in ceros]
    espaciamientos = np.diff(ceros_norm)
    
    print(f"{'Block':<15} | {'Mean Spacing':<20} | {'Variance'}")
    print("-" * 50)
    
    for i in range(0, len(espaciamientos), 20):
        bloque = espaciamientos[i : i + 20]
        print(f"{i+1}-{i+20:<10} | {np.mean(bloque):.6f}               | {np.var(bloque):.6f}")

if __name__ == "__main__":
    nnsd_auditor()
  
