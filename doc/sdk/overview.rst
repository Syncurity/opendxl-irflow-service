Overview
========

The `Syncurity IR-Flow <https://www.syncurity.net>`_  DXL Python service exposes access to interact with
IR-Flow via the DXL fabric.

The purpose of this service is to allow users to invoke IR-Flow remote commands via the DXL fabric.

A single IR-Flow service can connect to a single IR-Flow instance to provide access to the remote API endpoints exposed by IR-Flow.

DXL clients can invoke ePO remote commands by sending DXL request messages via the DXL fabric. The IR-Flow DXL service handles incoming request messages and forwards them to the appropriate ePO server via secure HTTP. Responses received from the IR-Flow server are packaged by the IR-Flow DXL service as DXL response messages and sent back to the invoking DXL client.
