Installation
============

Prerequisites
*************

* OpenDXL Python Client library installed
   `<https://github.com/opendxl/opendxl-client-python>`_

* The OpenDXL Python Client prerequisites must be satisfied
   `<https://opendxl.github.io/opendxl-client-python/pydoc/installation.html>`_

* The IR-Flow Python Client must be installed
    `<https://github.com/Syncurity/irflow-sdk-python>`_

* Python 2.7.9 or higher installed within a Windows or Linux environment. (Python 3 is not supported at this time)

Installation
************


This distribution contains a ``lib`` sub-directory that includes the application library files.

Use ``pip`` to automatically install the library:

    .. parsed-literal::

        pip install irflowservice-\ |version|\-py2-none-any.whl

Or with:

    .. parsed-literal::

        pip install irflowservice-\ |version|\.zip

As an alternative (without PIP), unpack the irflowservice-\ |version|\.zip (located in the lib folder) and run the setup
script:

    .. parsed-literal::

        python setup.py install
