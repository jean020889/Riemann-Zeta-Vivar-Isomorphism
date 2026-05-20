import mpmath

mpmath.mp.dps = 40

def generate_vivar_spectrum(n_limit=500):
    """
    Generates the spectral set of the Vivar Operator 
    representing the Riemann zeta zeros.
    """
    spectrum = [float(mpmath.zetazero(k).imag) for k in range(1, n_limit + 1)]
    return spectrum
