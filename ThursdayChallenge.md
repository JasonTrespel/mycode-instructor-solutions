# Thursday Challenge!

Start by making a file called `switch_cmds.txt` with the following commands in it:

```
show ver
show hostname
show arp
show history
```

Then write a python script that reads in this file and runs all of these commands against `sw-1`, `sw-2`, and the Cisco-NXOS switch (See lab 30 for connection details). 

Print out the responses.

HInt: This should be your list of network devices.

SW1 = ["arista_eos", "sw-1", "admin", "alta3"]
SW2 = ["arista_eos", "sw-2", "admin", "alta3"]
NXOS = ["cisco_nxos", "sandbox-nxos-1.cisco.com", "admin", "Admin_1234!"]

DEVICES = [SW1, SW2, NXOS]

**Taking it further**: Print the responses out as JSON data.

**More furtherer**: Send the JSON data to a file.
