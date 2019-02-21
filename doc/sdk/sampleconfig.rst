Samples Configuration
=====================

DXL Client Configuration
************************

The "IR-FLow Service" distribution contains a configuration file (``dxlclient.config``) located
in the ``sample`` sub-directory that must be populated in order for the samples to connect to the DXL fabric.

The steps to populate this configuration file are the same as those documented in the `OpenDXL Python SDK`, see the
`OpenDXL Python SDK Samples Configuration <https://opendxl.github.io/opendxl-client-python/pydoc/sampleconfig.html>`_
page for more information.

The following is an example of a populated configuration file:

   .. code-block:: python

       [Certs]
       BrokerCertChain=c:\\certificates\\brokercerts.crt
       CertFile=c:\\certificates\\client.crt
       PrivateKey=c:\\certificates\\client.key

       [Brokers]
       {5d73b77f-8c4b-4ae0-b437-febd12facfd4}={5d73b77f-8c4b-4ae0-b437-febd12facfd4};8883;mybroker.mcafee.com;192.168.1.12
       {24397e4d-645f-4f2f-974f-f98c55bdddf7}={24397e4d-645f-4f2f-974f-f98c55bdddf7};8883;mybroker2.mcafee.com;192.168.1.13



IR-Flow Service Configuration
*****************************

The "IR-Flow Service" also contains a configuration file calles (``dxlirflowservice.config``) in the ``sample`` sub-directory that must be populated in order to connect to the IR-Flow API.

The steps to populate this configuration are documented in in the `IR-FLow Python SDK`. See the `IR-FLow API <https://syncurity-irflow-sdk-python.readthedocs-hosted.com/en/latest/class.html#irflow_client.irflow_client.IRFlowClient._get_config_args_params>`_ docs for more information.

The following is an exmaple of a populated configuration file:

  .. code-block:: python

        ###############################################################################
        ## "IR-FLow Service" settings
        ###############################################################################

        [IRFlowAPI]
        address: <IP or FQDN of IR-FLow Server>
        api_user: some_api_user
        api_key: some_key
        debug=True
        protocol=https
        verbose=0

