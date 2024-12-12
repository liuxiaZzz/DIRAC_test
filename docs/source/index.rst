Welcome to DIRAC's documentation!
===================================

.. image:: ../Figs/logo.png
   :width: 150
   :alt: DIRAC icon
   :align: right

``DIRAC`` (**D**\ omain **I**\ nvariant **R**\ epresentation through **A**\ daptive **C**\ alibration), for spatially resolved integration of multi-omics. 

DIRAC is a Python package, written in `PyTorch <https://pytorch.org/>`_ and based on `scanpy <https://scanpy.readthedocs.io/en/stable/>`_ ,

DIRAC is a graph neural network to integrate spatial multi-omic data into a unified domain-invariant embedding space and to automate cell-type annotation by transferring labels from reference spatial or single-cell multi-omic data.

DIRAC primarily includes two integration paradigms: vertical integration and horizontal integration, which differ in their selection of anchors. In vertical integration, multiple data modalities from the same cells are jointly analyzed, using cell correspondences in single-cell data or spot correspondences in spatial data as anchors for alignment. In horizontal integration, the same data modality from distinct groups of cells is aligned using genomic features as anchors.

.. image:: ../Figs/Workflow.png
   :width: 800
   :alt: Model architecture
   :align: center

To get started with ``DIRAC``, check out the `installation guide <install.rst>`__ and `tutorials <tutorials.rst>`__.

For more details about the DIRAC framework, please check out our `publication <https://github.com/boxiangliulab/DIRAC>`__.

.. note::

   This project is under active development.

```{toctree}
:hidden: true
:maxdepth: 3
:titlesonly: true

Documentation home <self>
install
tutorials
api
credits
GitHub <https://github.com/liuxiaZzz/DIRAC_test>
