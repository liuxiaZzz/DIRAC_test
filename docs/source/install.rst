Installation guide
==================

************
Main package
************

The ``DIRAC`` package can be installed via conda using one of the following commands:

.. code-block:: bash
    :linenos:

    conda install -c conda-forge -c bioconda sodirac

Or, it can also be installed via pip:

.. code-block:: bash
    :linenos:

    pip install sodirac

.. note::
    To avoid potential dependency conflicts, installing within a
    `conda environment <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`__
    is recommended.


*********************
Optional dependencies
*********************

Some functions in the ``DIRAC`` package use metacell aggregation via k-Means clustering,
which can receive significant speed up with the `faiss <https://github.com/facebookresearch/faiss>`__ package.

You may install ``faiss`` following the official `guide <https://github.com/facebookresearch/faiss/blob/main/INSTALL.md>`__.

Now you are all set. Proceed to `tutorials <tutorials.rst>`__ for how to use the ``DIRAC`` package.
