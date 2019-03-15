# IR-Flow Service
[![OpenDXL Bootstrap](https://img.shields.io/badge/Built%20With-OpenDXL%20Bootstrap-blue.svg)](https://github.com/opendxl/opendxl-bootstrap-python)
[![Latest PyPI Version](https://img.shields.io/badge/pypi-v1.1.0-blue.svg)](https://pypi.python.org/pypi/dxlirflowservice)

## Overview

The Syncurity IR-Flow DXL Python service exposes access to interact with
IR-Flow API via the DXL fabric.

The purpose of this service is to allow users to invoke IR-Flow remote commands via the DXL fabric.

A single IR-Flow service can connect to a single IR-Flow instance to provide access to the remote API endpoints exposed by IR-Flow.

DXL clients can invoke ePO remote commands by sending DXL request messages via the DXL fabric. The IR-Flow DXL service handles incoming request messages and forwards them to the appropriate ePO server via secure HTTP. Responses received from the IR-Flow server are packaged by the IR-Flow DXL service as DXL response messages and sent back to the invoking DXL client.

## Documentation

TODO: Provide documentation information

## Installation

TODO: Provide installation information

## Bugs and Feedback

Open an Issue 

## LICENSE

Copyright 2019

Apache 2.0
