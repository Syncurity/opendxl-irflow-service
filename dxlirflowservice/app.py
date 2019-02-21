from __future__ import absolute_import
import logging

from dxlbootstrap.app import Application
from dxlclient.service import ServiceRegistrationInfo
from .requesthandlers import *


# Configure local logger
logger = logging.getLogger(__name__)


class IRFlowService(Application):
    """
    The ""IR-FLow Service"" application class.
    """

    def __init__(self, config_dir):
        """
        Constructor parameters:

        :param config_dir: The location of the configuration files for the
            application
        """
        super(IRFlowService, self).__init__(config_dir, "dxlirflowservice.config")

    @property
    def client(self):
        """
        The DXL client used by the application to communicate with the DXL
        fabric
        """
        return self._dxl_client

    @property
    def config(self):
        """
        The application configuration (as read from the "dxlirflowservice.config" file)
        """
        return self._config

    def on_run(self):
        """
        Invoked when the application has started running.
        """
        logger.info("On 'run' callback.")

    def on_load_configuration(self, config):
        """
        Invoked after the application-specific configuration has been loaded

        This callback provides the opportunity for the application to parse
        additional configuration properties.

        :param config: The application configuration
        """
        logger.info("On 'load configuration' callback.")

    def on_dxl_connect(self):
        """
        Invoked after the client associated with the application has connected
        to the DXL fabric.
        """
        logger.info("On 'DXL connect' callback.")
    
    def on_register_services(self):
        """
        Invoked when services should be registered with the application
        """
        # Register service 'irflow_api_service'
        logger.info("Registering service: %s", "irflow_api_service")
        service = ServiceRegistrationInfo(self._dxl_client, "/syncurity/service/irflow_api")

        # Create Alert in IR-Flow
        logger.info("Registering request callback: %s", "irflow_service_create_alert")
        self.add_request_callback(service,
                                  "/syncurity/service/irflow_api/create_alert",
                                  IRFlowCreateAlertCallback(self),
                                  True)
        # Close Alert in IR-Flow
        logger.info("Registering request callback: %s", "irflow_service_close_alert")
        self.add_request_callback(service,
                                  "/syncurity/service/irflow_api/close_alert",
                                  IRFlowCloseAlertCallback(self),
                                  True)

        self.register_service(service)
