.. RECTE documentation master file, created by
   sphinx-quickstart on Thu Jan  3 12:44:34 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentations for RECTE
========================

RECTE (Ramp Effect Charge Trapping Eliminator) models and corrects one of the most prominent HST/WFC3/IR systematics -- the so-called "ramp effect". The goals of this model are to improve the precision and efficiency in HST/WFC3/IR time-resolved observations. We detailed the motivations, assumptions, derivations, and applications in `Zhou et al. (2017) <http://stacks.iop.org/1538-3881/153/i=6/a=243?key=crossref.d8632f701456202d40ec5de454a41fff>`_.

We also provide a python package for RECTE. This python package can be easily incorporated with exisiting HST/WFC3/IR time-resolved data reduction pipelines. This document demonstrate the installation, usage, and applications for this package. We have also prepared a few Jupyter notebooks for cookbook-style demonstrations.

If you have any questions, comments, or suggestions, please file an issue on github or drop the developer an `email <mailto:yifzhou@email.arizona.edu>`_.

If you find this model useful, please consider citing

.. code:: latex
          
          @article{Zhou2017,
          author = {Zhou, Yifan and Apai, D{\'{a}}niel and Lew, Ben W. P. and Schneider, Glenn H},
          doi = {10.3847/1538-3881/aa6481},
          issn = {1538-3881},
          journal = {AJ},
          month = {mar},
          number = {6},
          pages = {243},
          title = {{A Physical Model-based Correction for Charge Traps in the Hubble Space Telescope's Wide Field Camera 3 Near-IR Detector and Applications to Transiting Exoplanets and Brown Dwarfs}},
          volume = {153},
          year = {2017}
          }

          
.. toctree::
   :maxdepth: 4
   :caption: Document Contents:
   
   getstarted
   installation
   api
   applications
   
