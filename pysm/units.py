""" This submodule contains the code used for the units
system in PySM. We use the `astropy.units` module for
the infrastructure of unit conversion. We add a unit,
thermodynamic temperature, which is not in the standard
set of units included with the package.
"""
import numpy as np
from astropy.units import *
from astropy.modeling.blackbody import blackbody_nu
import astropy.constants as const
# Note that this is a bit of a hack, since we must include the
# '1. * ' in order to make this work.
def_unit(r'K_CMB', namespace=globals(), prefixes=True,
         doc='Kelvin CMB: Thermodynamic temperature units.',
         format={'generic': r'K_CMB'})
add_enabled_units(K_CMB)
def_unit(r'K_RJ', namespace=globals(), prefixes=True,
        doc='Kelvin Rayleigh-Jeans:  brightness temperature.',
         format={'generic': r'K_RJ'})
add_enabled_units(K_RJ)

@quantity_input(freqs=Hz)
def RJ_CMB_equiv(freqs):
    """ This function defines an equivalency between
    thermodynamic units and brightness units. This is
    function may be passed to the `Quantity.to` method
    in order to convert between equivalent units.

    Parameters
    ----------
    freqs: Quantity.GHz

    Returns
    -------
    tuple
        Returns tuple accepted by astrpy equivalencies.
    """
    cmb_mono = 2.7225 * K
    prefactor = 2. * freqs ** 2. * const.k_B / const.c ** 2
    prefactor *= 1. / planck_bb_der(cmb_mono, freqs)
    def RJ_to_CMB(T_RJ):
        return prefactor * T_RJ
    def CMB_to_RJ(T_CMB):
        return T_CMB / prefactor
    return [(K_RJ, K_CMB, RJ_to_CMB, CMB_to_RJ)]

@quantity_input(temp=K, freqs=Hz)
def planck_bb_der(temp, freqs):
    """ Function to calculate the first derivative of the Planck
    function for a given temperature.
    """
    ex = const.h * freqs / const.k_B / temp
    return ex * np.exp(ex) / np.expm1(ex) * blackbody_nu(freqs, temp) / temp
