# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------
import sys
from smssender import SmsSender
from deamon import Daemon
from config import SenderConfig, ScheduleConfig

if __name__ == "__main__":
    config = SenderConfig()
    config.loadConfiguration()
    daemon = SmsSender(config=config)
    usageMessage = f"Usage: {sys.argv[0]} (start|stop|restart|status|reload|version)"

    if len(sys.argv) == 2:
        choice = sys.argv[1]
        if choice == "start":
            daemon.start()
        elif choice == "stop":
            daemon.stop()
        elif choice == "restart":
            daemon.restart()
        elif choice == "status":
            daemon.status()
        elif choice == "reload":
            daemon.reload()
        elif choice == "version":
            daemon.version()
        else:
            print("Unknown command.")
            print(usageMessage)
            sys.exit(1)
        sys.exit(0)
    else:
        print(usageMessage)
        sys.exit(1)
