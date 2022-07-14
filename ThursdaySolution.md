```
#!/usr/bin/env python3

import json
# python3 -m pip install --user netmiko
from netmiko import ConnectHandler

SW1 = ["arista_eos", "sw-1", "admin", "alta3"]
SW2 = ["arista_eos", "sw-2", "admin", "alta3"]
NXOS = ["cisco_nxos", "sandbox-nxos-1.cisco.com", "admin", "Admin_1234!"]

DEVICES = [SW1, SW2, NXOS]

def run_cmd(cmd, dtype, ip, uname, pw):
    open_connection = ConnectHandler(device_type=dtype, ip=ip, username=uname, password=pw)
    return open_connection.send_command(cmd)


def main():
    """run time code"""
    with open("switch_cmds.txt", "r") as f:
        commands = f.readlines()
    device_info = []                                         # Part 2 - 3
    for dev in DEVICES:
        dev_info = {"device": dev[1], "config_data": []}     # Part 2 - 3
        for command in commands:
            output = run_cmd(command, *dev)
            # output = run_cmd(command, dev[0], dev[1], dev[2], dev[3])   <-- same as above line

            # Challenge Part 1
            print(output)

            # Part 2 - 3
            dev_info['config_data'].append({"cmd": command, "output": output})
        device_info.append(dev_info)
    # Part 2
    print(json.dumps(device_info))
    # Part 3
    with open("switch_info_out.json", "w") as f2:
        json.dump(device_info, f2)

main()
```
