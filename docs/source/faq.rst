Frequent Asked Questions
========================

1. Q: Does the RECTE correction match or exceed the accuracy of the empirical exponential ramp correction?
   
   
2. Q: Can RECTE be used for scanning-mode observations?

3. Does RECTE have many parameters that must be optimized?

4. Has the RECTE model been used in refereed publications?

5. Should I still take an additional extra orbit in the beginning of my observations to allow for “instrumental settling”?

1. Q: Should I adjust charge trapping related parameters (`nTrap`, `eta`, `tau`) for my observations?

   A: The set of parameters that are hard coded in the python script work for datasets taken in multiple instrument configurations. They should also work for your observations. These parameters are also more up-to-date than those listed in Zhou et al. (2017).

2. Q: Does the correction work equally well on the first orbit of the observation? Should I keep those data in my analysis?
   
   A: The correction performance is the same in the first orbits as in the rest of the observations. The amplitude and gaussianity of the fitting residuals in the first orbit light curves and the other parts fo the light curves agree. You should keep those light curves as part of your analysis.

3. Q: How should I set the count rate?
   
   A: To model the ramp profile for the light curve a wavelength channel, the average count rate of all pixels within that channel should be used. 


4. Q: How should I correct staring mode observations?
   
   A: In images taken in staring mode, there are large spatial variances of fluence. As a consequence, the ramp profiles are significantly different for different pixels. The average fluence will not be a good input parameter to calculate the ramp. Instead, you should consider feeding the PSF into RECTE to forward model the ramp effect profiles.

5. Q: What is the limitation of RECTE?
   
   A: Additional systematic effects are clearly visible if the observation fluence approaches saturation limit (70,000 :math:`e^-`). This could be due to significantly stronger image persistence in these regime. Currently, RECTE does not include this rise of persistence as part of the model and may not provide the most accurate correction when fluence is above 50,000 :math:`e^-`.
