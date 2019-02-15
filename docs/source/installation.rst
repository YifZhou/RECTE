.. _install:

Installation and Usage
======================

Required packages
-----------------

* numpy
* scipy
* matplotlib

For fitting/optimization

* lmfit
* emcee

For Jupyter notebooks demonstration

* jupyter
* ipywidgets


You may download the ``requirements.txt`` file and do

.. code-block:: bash
                
   pip install -r requirement.txt

to ensure all requirements are satisfied.

Installations
-------------

Ramp profile calculation is done by function ``RECTE`` in ``RECTE.py`` Please download the file ``RECTE.py`` and place it in your analysis directory. You may then simply import the function and calculate/fit the ramp profile.

.. code-block:: python
                
                from RECTE import RECTE


We created convenience functions for ramp effect modeling and corrections. These functions are in ``RECTECorrector.py``. Functions ``RECTECorrector1`` and ``RECTECorrector2`` are for correcting ramp effect in the light curves observed using forward-scanning and round-trip-scanning mode, respectively.

Detailed explanation of the code are in Section :ref:`API`. 

We created a Jupyter notebook to demonstrate the usage of RECTE. Please refer it in :ref:`cookbook_label` section.

