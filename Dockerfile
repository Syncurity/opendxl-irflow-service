# Base image from Python 2 (slim)
FROM python:2-slim

VOLUME ["/opt/irflowservice-config"]

# Copy application files
COPY . /tmp/build
WORKDIR /tmp/build

# Clean application
RUN python ./clean.py

# Install application package and its dependencies
RUN pip install .

# Cleanup build
RUN rm -rf /tmp/build

################### INSTALLATION END #######################
#
# Run the application.
#
# NOTE: The configuration files for the application must be
#       mapped to the path: /opt/dxlirflowservice-config
#
# For example, specify a "-v" argument to the run command
# to mount a directory on the host as a data volume:
#
#   -v /host/dir/to/config:/opt/dxlirflowservice-config
#
CMD ["python", "-m", "irflowservice", "/opt/irflowservice-config"]
