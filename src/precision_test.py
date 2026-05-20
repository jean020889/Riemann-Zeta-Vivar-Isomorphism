import mpmath

def test_stability(n_ceros=100):
    """
    Verifies that the spectral values remain invariant 
    across different floating-point precision levels.
    """
    precision_levels = [20, 40, 60]
    print(f"{'DPS':<10} | {'Sample Zero 100'}")
    
    for dps in precision_levels:
        mpmath.mp.dps = dps
        zero = mpmath.zetazero(n_ceros).imag
        print(f"{dps:<10} | {zero}")

if __name__ == "__main__":
    test_stability()
  
