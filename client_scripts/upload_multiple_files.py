from __future__ import print_function
import sys
import commands
import bioblend.galaxy
import time

if len(sys.argv) < 2:
    print("Usage: python upload_file.py <files>")
    sys.exit(1)

galaxy = "http://"+commands.getoutput("cat /root/galaxy")
key = commands.getoutput("cat /root/key")
history = commands.getoutput("cat /root/history")
user = commands.getoutput("cat /root/user")

# Initiating Galaxy connection
gi = bioblend.galaxy.GalaxyInstance(galaxy, key)

jobs = []
for path in sys.argv[1:]:
    file_info = gi.tools.upload_file(path, history, file_type="txt") 
    jobs.append(file_info["jobs"][0]["id"])

arq = open("/root/created_datasets.csv", "a")
while len(jobs) > 0:
    ready = []
    for job in jobs:
        state = gi.jobs.get_state(job)
        if state == "ok":
            ready.append(job)
    for job in ready:
        arq.write(user+";"+str(job))
        jobs.remove(job)
    time.sleep(1)
arq.close()


