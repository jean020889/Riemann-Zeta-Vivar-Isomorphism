import numpy as np
import mpmath

def compute_delta3(n_limit=100):
    """
    Calculates the Dyson-Mehta Delta_3 statistic to verify 
    long-range spectral rigidity of the Vivar Operator.
    """
    mpmath.mp.dps = 40
    ceros = [float(mpmath.zetazero(k).imag) for k in range(1, n_limit + 1)]
    
    def n_bar(t):
        return (t / (2 * np.pi)) * (np.log(t / (2 * np.pi * np.e)))
    
    ceros_norm = np.array([n_bar(c) for c in ceros])
    L_values = [5, 10, 20]
    
    print(f"{'Window L':<15} | {'Delta_3 Statistic'}")
    print("-" * 35)
    
    for L in L_values:
        delta3_sum = 0
        for i in range(len(ceros_norm) - L):
            ventana = ceros_norm[i : i + L]
            x = np.arange(L)
            a, b = np.linalg.lstsq(np.vstack([x, np.ones(L)]).T, ventana, rcond=None)[0]
            delta3_sum += np.mean((ventana - (a * x + b))**2)
        print(f"{L:<15} | {delta3_sum / (len(ceros_norm) - L):.6f}")

if __name__ == "__main__":
    compute_delta3()
