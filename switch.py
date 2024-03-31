#!/bin/python3
import os

rc_file = os.path.expanduser("~/.bashrc")
enabled_text = "ROUTER_ENABLED=TRUE"
disabled_text = "ROUTER_ENABLED=FALSE"

with open(rc_file, "r") as incoming:
    output = incoming.read()

if enabled_text in output:
    print("Disabling router.")
    output = output.replace(enabled_text, disabled_text)
elif disabled_text in output:
    print("Enabling router.")
    output = output.replace(disabled_text, enabled_text)
else:
    print("No config previously set, enabling router.")
    output += f"\nexport {enabled_text}"

with open(rc_file, "w") as outgoing:
    outgoing.write(output)

print("Please reboot the system to enable changes.")

