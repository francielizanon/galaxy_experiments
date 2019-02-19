from __future__ import print_function
import sys
import commands
import bioblend.galaxy
import time

if len(sys.argv) != 5:
    print("Usage: python "+sys.argv[0]+" <key> <history_id> <dataset_id> <output_path>")
    sys.exit(1)


key = sys.argv[1]
history = sys.argv[2]
did = sys.argv[3]
path = sys.argv[4]
galaxy = "http://"+commands.getoutput("cat /root/galaxy")

# Initiating Galaxy connection
gi = bioblend.galaxy.GalaxyInstance(galaxy, key)

gi.datasets.download_dataset(did, file_path=path, use_default_filename=False)

