#!/usr/bin/python
import os
import json
import re


if __name__ == "__main__":
    # Iterate over all block devices, but ignore them if they are in the
    # skippable set
    skippable = (r'^(sr|loop|ram|fd|dm)', r'^(sd\w|hd\w|nvme\d+n\d+p|xvd\w|vd\w)\d+$')
    devices = (device for device in os.listdir("/sys/class/block")
               if not any(re.search(ignore, device) for ignore in skippable))
    data = [{"{#DEVICENAME}": device} for device in devices]
    print(json.dumps({"data": data}, indent=4))
