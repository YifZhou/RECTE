.. RECTE documentation master file, created by
   sphinx-quickstart on Thu Jan  3 12:44:34 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for RECTE
=======================
.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. todo::
   two paragraphs to introduce RECTE

   What is RECTE? What does RECET stand for

How effective is RECTE?
***********************

RECTE is effective in three ways:

    1. RECTE correction results in photon-noise limited light curves
    2. RECTE correct the entire light curve (including the first orbit) in a consistent manner. It saves precious HST time
    3. RECTE correction is not sensitive to the assumption on the baseline of the light curve, thus the is less degenerated with astrophysical signals.

Usage
-----

.. todo::
   describe the deployment of RECTE, which include
   - what file are useful
   - where to place the file
   - how to incorporate RECTE in my data reduction pipeline
   

Getting Started
---------------

How is ramp effect systematics introduced by charge trapping?
*************************************************************

.. todo::
   add one paragraph of description of the mechnism

To demonstrate ramp effect introduced by charge trapping, we created an intractive Jupyter notebook. You can download the notebook at `charge trapping demonstration <https://github.com/YifZhou/RECTE/blob/master/RECTE%20Demonstration.ipynb>`and run it locally. The Jupyter notebook allow to adjust model parameters and see the changes in the ramp profile in real time. For the detailed systematics mechanism, please refer to Zhou et al. (2017).

.. todo::
   add more documentations to the jupyter notebook


How can I incorporate RECTE in my data reduction pipeline?
**********************************************************

We created a Jupyter notebook to demonstrate the usage of RECTE. You can also find detailed descriptions in the :ref:`cookbook_label` section.

.. todo::
   1. add one paragraph to summarize the the principle of incorporation
   2. create another jupyter notebook for data reduciton

   
.. cookbook_label:
Examples and Cookbook
---------------------

.. todo::
   provide three examples and write them up
   example 1: trappist
   example 2: HN Peg B
   example 3: WASP 19 (for buffer down load)

Modules
-------

.. todo::
   add two paragraphs to describe the usages of these two files
   improve the docstrings for python files

.. include:: RECTE.rst
                                
.. include:: RECTECorrector.rst




