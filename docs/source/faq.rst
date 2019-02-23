Frequent Asked Questions
========================

1. Q: Should I adjust charge trapping related parameters (`nTrap`, `eta`, `tau`) for my observations.

   A: The set of parameters that are hard coded in the python script work for datasets taken in multiple instrument configurations. They should also work for your observations. These parameters are also more updated than those listed in Zhou et al. (2017).

2. Q: Does the correction work equally well on the first orbit of the observation? Should I keep those data in my analysis?
   A: The correction performances are the same in the first orbits and the rest of the observations. The amplitude and gaussianity of the fitting residuals in the first orbit light curves and the other parts fo the light curves agree. You should keep those light curves as part of your analysis.

3. Q: How should I set the count rate?
   A: To model the ramp profile for the light curve a wavelength channel, the average count rate of all pixels within that channel should be used. 


4. Q: What I should do if my observation is done in Staring mode?
   A: There are large variance of fluence in images observed in staring mode. As a consequences, the ramp profiles are significantly different for different pixels. The average fluence will not be a good input parameter to calculate the ramp. Instead, you should consider feeding the PSF into RECTE to forward model the systematic profiles.

5. Q: What is the limitation of RECTE?
   A: Additional systematic effect are clearly visible if the observation fluence approaches saturation limit (70000 :math:`e^-`). This could be due to significantly stronger image persistence in these regime. Currently, RECTE does not include this rise of persistence as part of the model and may not provide the most accurate correction when fluence is above 50000 :math:`e^-`.
