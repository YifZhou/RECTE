Frequent Asked Questions
========================

1. Q: Does the RECTE correction match or exceed the accuracy of the empirical exponential ramp correction?

   A: Yes. The quality of the corrected light curves approaches the photo-noise limit, for both the first orbit and rest of the observations.

   
2. Q: Can RECTE be used for scanning-mode observations?

   A: Yes. The demosntration can be found at :ref:`cookbook_label`.
   

3. Does RECTE have many parameters that must be optimized?

   A: No. In most cases, parameters that describe the charge traps do not need to be adjusted. Parameters for the initial charge trap states  and the numbers of charges trapped during earth occultations (4 parameters) are the only ones that need to be optimized.

   
4. Has the RECTE model been used in refereed publications?

   A: Yes. You can find them `here <http://adsabs.harvard.edu/cgi-bin/nph-ref_query?bibcode=2017AJ....153..243Z&amp;refs=CITATIONS&amp;db_key=AST>`_.
   

5. Should I still take an additional extra orbit in the beginning of my observations to allow for “instrumental settling”?

   A: No. After RECTE correction, the light curve from the first orbit can be used in subsequent data analysis.
   

6. Q: Should I adjust charge trapping related parameters (`nTrap`, `eta`, `tau`) for my observations?

   A: The set of parameters that are hard coded in the python script work for datasets taken in multiple instrument configurations. They should also work for your observations. These parameters are also more up-to-date than those listed in Zhou et al. (2017).

   
7. Q: Does the correction work equally well on the first orbit of the observation? Should I keep those data in my analysis?
   
   A: The correction performance is the same in the first orbits as in the rest of the observations. The amplitude and gaussianity of the fitting residuals in the first orbit light curves and the other parts fo the light curves agree. You should keep those light curves as part of your analysis.

   
8. Q: How should I set the count rate?
   
   A: To model the ramp profile for the light curve a wavelength channel, the average count rate of all pixels within that channel should be used. 


9. Q: How should I correct staring mode observations?
   
   A: In images taken in staring mode, there are large spatial variances of fluence. As a consequence, the ramp profiles are significantly different for different pixels. The average fluence will not be a good input parameter to calculate the ramp. Instead, you should consider feeding the PSF into RECTE to forward model the ramp effect profiles.

   
10. Q: What is the limitation of RECTE?
   
   A: Additional systematic effects are clearly visible if the observation fluence approaches saturation limit (70,000 :math:`e^-`). This could be due to significantly stronger image persistence in these regime. Currently, RECTE does not include this rise of persistence as part of the model and may not provide the most accurate correction when fluence is above 50,000 :math:`e^-`.
