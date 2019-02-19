from __future__ import print_function
import sys
import commands
import bioblend.galaxy
import time

if len(sys.argv) != 4:
    print("Usage: python "+sys.argv[0]+" <key> <history_id> <dataset_id>")
    sys.exit(1)

key = sys.argv[1]
history = sys.argv[2]
did = sys.argv[3]
galaxy = "http://"+commands.getoutput("cat /root/galaxy")

# Initiating Galaxy connection
gi = bioblend.galaxy.GalaxyInstance(galaxy, key)

run_info = gi.tools.run_tool(history, "read-file-count", tool_inputs = {"URL": "/api/histories/"+history+"/contents/"+did, "URL_method": "get", "data_type": "txt"})

while gi.jobs.get_state(run_info["jobs"][0]["id"]) != "ok":
    time.sleep(1)

print(run_info["outputs"][0]["id"])

