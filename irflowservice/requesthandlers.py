from __future__ import absolute_import
import logging
import json

from dxlclient.callbacks import RequestCallback
from dxlclient.message import Response, ErrorResponse
from dxlbootstrap.util import MessageUtils

# Syncurity
from irflow_client import IRFlowClient

# Configure local logger
logger = logging.getLogger(__name__)


class IRFlowBaseCallback(RequestCallback):

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(IRFlowBaseCallback, self).__init__()
        self.irfc = IRFlowClient(config_file='config/irflowservice.config')
        self._app = app

    def on_request(self, request):
        """
        Invoked when a request message is received.

        :param request: The request message
        """
        # Handle request
        logger.info("Request received on topic: '%s' with payload: '%s'",
                    request.destination_topic,
                    MessageUtils.decode_payload(request))

        try:
            # Create response
            res = Response(request)

            # Set payload
            # Read DXL request payload into dictionary
            request_dict = MessageUtils.json_payload_to_dict(request)

            dxl_resp = self.transform_dict(self.invoke_service(request_dict))

            # Add web service response to DXL response payload
            MessageUtils.encode_payload(res, dxl_resp)
            # Send response
            self._app.client.send_response(res)

        except Exception as ex:
            logger.exception("Error handling request")
            err_res = ErrorResponse(request, error_code=0,
                                    error_message=MessageUtils.encode(str(ex)))
            self._app.client.send_response(err_res)

    def invoke_service(self, request):
        pass

    def transform_dict(self, dict):
        pass


class IRFlowCreateAlertCallback(IRFlowBaseCallback):
    """
    'irflow_service_create_alert' request handler registered with topic '/syncurity/service/irflow_api/create_alert'
    """

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(IRFlowCreateAlertCallback, self).__init__(app)

    def invoke_service(self, request_dict):
        # http_res = requests.get("http://geoloc.opendxl.io/{0}/{1}".format(
        #     request_dict["format"], request_dict["host"]))
        # Invoke IR-Flow Create Alert web service
        alert_resp = self.irfc.create_alert(alert_fields=request_dict,
                                            description='DXL Testing',
                                            incoming_field_group_name='DXLAlerts',
                                            suppress_missing_field_warning=True)
        return alert_resp.json()

    def transform_dict(self, dict):
        return {
            'alert_num': dict['data']['alert']['alert_num'],
            'fact_group_id': dict['data']['alert']['fact_group_id'],
            'message': dict['message'],
            'score': dict['data']['alert']['score'],
            'success': dict['success']
        }


class IRFlowSomeOtherCallback(IRFlowBaseCallback):

    def __init__(self, app):
        super(IRFlowSomeOtherCallback, self).__init__(app)

    def invoke_service(self, request_dict):
        print(request_dict)
        return {'hello': 'there'}

    def transform_dict(self, dict):
        return {
            'foo': 'bar',
            'hello': dict['hello']
        }
