import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

def polyfit(dates: list, levels: list, p: int) -> tuple:
    """
    Computes a least-squares fit of a polynomial of degere p to 
    water level data and returns a tuple of the polynomial object
    and the shift of the time axis.
    """

    x = matplotlib.dates.date2num(dates)
    y = levels

    # Use shifted x values to find best-fit polynomial to avoid
    # significant floating point round-off errors.
    d0 = x[0]
    p_coeff = np.polyfit(x-d0, y, p)

    # Create a polynomial using the coefficients.
    poly = np.poly1d(p_coeff)

    return (poly, d0)

