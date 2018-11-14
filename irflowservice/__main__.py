from __future__ import absolute_import
from __future__ import print_function
import logging
from logging.config import fileConfig

import sys
import os
import signal
import threading

from .app import IRFlowService

# Whether the application is running
running = False

# Condition used to notify that the application should exit
run_condition = threading.Condition()


def signal_handler(signum, frame):
    """
    Signal handler invoked when registered signals are triggered

    :param signum: The signal number
    :param frame: The frame
    """
    del signum, frame
    global running, run_condition
    with run_condition:
        if running:
            # Stop the application
            running = False
            run_condition.notify()
        else:
            exit(1)


# Signals to register for
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# Validate command line
if len(sys.argv) != 2:
    print("Usage: irflowservice <configuration files directory>")
    sys.exit(1)

#
# Configure Logging
#

config_dir = sys.argv[1]
logging_config_path = os.path.join(config_dir, IRFlowService.LOGGING_CONFIG_FILE)
if os.access(logging_config_path, os.R_OK):
    # Log configuration via configuration file
    fileConfig(logging_config_path, disable_existing_loggers=False)
    logger = logging.getLogger()
else:
    # Default log configuration (no configuration file)
    log_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)

    logger = logging.getLogger()
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

# Create the application
with IRFlowService(sys.argv[1]) as app:
    try:
        # Run the application
        app.run()
        running = True

        with run_condition:
            # Wait until notified to exit
            while running:
                run_condition.wait(60)

    except KeyboardInterrupt:
        pass
    except Exception:
        logger.exception("Error occurred, exiting")
        sys.exit(1)
