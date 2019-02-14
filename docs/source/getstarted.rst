RECTE Model Primer
==================

How effective is RECTE?
-----------------------

RECTE is effective in three ways:

    1. RECTE correction results in photon-noise limited light curves
    2. RECTE correct the entire light curve (including the first orbit) in a consistent manner. It saves precious HST time
    3. RECTE correction is not sensitive to the assumption on the baseline of the light curve, thus the is less degenerated with astrophysical signals.


RECTE Mechanisms Explanined
---------------------------

.. todo::
   add one paragraph of description of the mechnism

Our model is based on the charge carrier trapping theory of `Smith et al. (2008a) <http://proceedings.spiedigitallibrary.org/proceeding.aspx?doi=10.1117/12.789372>`_. However, instead of fitting empirically derived exponential functions, our model enables us to quantitatively model the charge carrier trapping processes, so that we can precisely calibrate ramp-effect-impacted time-resolved observations made with WFC3.A summary of the principle of RECTE model is presented in the following.

1. The detector pixels have two populations of charge carrier traps: a slow trap population that releases trapped particles with a long trapping lifetime and a fast trap population that releases trapped particles with a short trapping lifetime. The total numbers of traps per pixel for the two population are :math:`E_{\mathrm{s,tot}}` and :math:`E_\mathrm{f,tot}`.
   
2. Charge carriers stimulated by incoming photon fluxes can fill the two populations of traps with efficiencies of :math:`\eta_\mathrm{s}` and :math:`\eta_{\mathrm{f}}`.

3. The two populations of trapped charge particles have lifetimes of :math:`\tau_\mathrm{s}` and :math:`\tau_\mathrm{f}`. With no incoming radiation, the number of trapped charges follows exponential decay.

4. The observed flux (:math:`f_\mathrm{obs}`) is the intrinsic flux (:math:`f`) subtracted by the charge carriers that are trapped.

   
   .. math::
      f^{\prime} (t) = f - \frac { \mathrm { d } E _ { \mathrm { s } } ( t ) } { \mathrm { d } t } - \frac { \mathrm { d } E _ { \mathrm { f } } ( t ) } { \mathrm { d } t }
      = f - \left[ \eta _ { \mathrm { s } } f - E _ { \mathrm { s } , 0 } ( t ) \left( \frac { \eta _ { \mathrm { s } } f } { E _ { \mathrm { s } , \mathrm { tot } } } + \frac { 1 } { \tau _ { \mathrm { s } } } \right) \right] \mathrm { e } ^ { - \left( \frac { \eta _ { \mathrm { s } } f } { E _ { \mathrm { s } , \mathrm { tot } } } + \frac { 1 } { \tau _ { \mathrm { s } } } \right) t } \\
      - \left[ \eta _ { \mathrm { f } } f - E _ { \mathrm { f } , 0 } ( t ) \left( \frac { \eta _ { \mathrm { f } } f } { E _ { \mathrm { f } , \mathrm { tot } } } + \frac { 1 } { \tau _ { \mathrm { f } } } \right) \right] \mathrm { e } ^ { - \left( \frac { \eta _ { \mathrm { f } } f } { E _ { \mathrm { f } } , { \mathrm { tot } } } + \frac { 1 } { \tau _ { \mathrm { f } } } \right) t } 

RECTE Mechanism Demonstration
-----------------------------

To demonstrate ramp effect introduced by charge trapping, we created an intractive Jupyter notebook. You can download the notebook at `charge trapping demonstration <https://github.com/YifZhou/RECTE/blob/master/RECTE_Demonstration.ipynb>`_ and run it locally. The Jupyter notebook allow to adjust model parameters and see the changes in the ramp profile in real time. For the detailed systematics mechanism, please refer to `Zhou et al. (2017) <http://stacks.iop.org/1538-3881/153/i=6/a=243?key=crossref.d8632f701456202d40ec5de454a41fff>`_.

      
.. toctree::
   :maxdepth: 2
   :caption: Jupyter notebook Demonstration:
             
   ipython_notebook/RECTE_Mechanisms.rst

