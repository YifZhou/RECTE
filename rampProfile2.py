import numpy as np

from RECTE import RECTE


def rampProfile2(crate1, slope1, crate2, slope2, dTrap_s, dTrap_f,
                 trap_pop_s, trap_pop_f, tExp, expTime, scanDirect):
    """Ramp profile for bi-directional scan And ackbar model

    :param crate1: average count rate in electron/second for the upward direction
    :param slope1: visit-long slope for upward direction
    :param crate2: average count rate in electron/second for downward direction
    :param slope2: visit-long slope for downward direction
    :param dTrap_s: extra trapped slow charges between orbits
    :param dTrap_f: extra trapped fast charges between orbits
    :param trap_pop_s: initially trapped slow charges
    :param trap_pop_f: initially trapped fast charges
    :param tExp: beginning of each exposure
    :param expTime: exposure time
    :param scanDirect: scan direction (0 or 1) for each exposure
    :returns: observed counts
    :rtype: numpy.array

    """
    tExp = (tExp - tExp[0])
    upIndex, = np.where(scanDirect == 0)
    downIndex, = np.where(scanDirect == 1)
    cRates = np.zeros_like(tExp, dtype=float)
    cRates[upIndex] = (
        crate1 * (1 + tExp * slope1 / 1e7) / expTime)[upIndex]
    cRates[downIndex] = (
        crate2 * (1 + tExp * slope2 / 1e7) / expTime)[downIndex]
    obsCounts = RECTE(
        cRates,
        tExp,
        expTime,
        trap_pop_s,
        trap_pop_f,
        dTrap_f=[dTrap_f],
        dTrap_s=[dTrap_s],
        dt0=[0],
        lost=0,
        mode='scanning')
    return obsCounts
