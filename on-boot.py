#!/bin/python3
from gpiozero import LED
import os

router_enabled = os.environ.get("ROUTER_ENABLED")
print(router_enabled)

if router_enabled is None:
    with open(os.path.expanduser("~/.bashrc"), "a") as output:
        output.write("export ROUTER_ENABLED=TRUE")
    router_enabled = True
elif router_enabled == "FALSE":
    router_enabled = False
else:
    router_enabled = True

router = LED(23)
if router_enabled:
    router.on()

while True:
    pass
