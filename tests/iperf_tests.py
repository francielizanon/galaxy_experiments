#we need all nodes for this test
import commands
import os

repetitions = 4

print("Ill run "+str(repetitions)+" repetitions of the iperf tests")
print(commands.getoutput("date"))

#read all nodes
galaxy_node = commands.getoutput("cat ../galaxy_node").split('\n')[0]
nodes = []
arq = open("../nodes", "r")
for line in arq:
    nodes.append(line.split('\n')[0])
nodes.remove(galaxy_node)
arq.close()

print("Ill run "+str(repetitions)+" repetitions of the iperf tests between the galaxy node "+galaxy_node+" and "+str(len(nodes))+" other nodes")
os.system("mkdir iperf_results")

print("Ill start the server in the galaxy node")
os.system("ssh root@"+galaxy_node+" iperf -s &")

for rep in range(repetitions):
    print("starting repetition "+str(rep))
    for no in nodes:
        os.system("ssh root@"+no+" iperf -c "+galaxy_node+" -r -t 10 > iperf_results/iperf_results_server_"+galaxy_node.split('.')[0]+"_with_"+no.split('.')[0]+"_rep"+str(rep)+".txt")
    print("Im done with repetition "+str(rep))
    print(commands.getoutput("date"))

#kill the server-side iperf part on the galaxy server
print("Ill kill iperf on the galaxy node")
line = commands.getoutput("ssh root@"+galaxy_node+" ps aux|grep iperf").split('\n')[0]
print(line)
os.system("ssh root@"+galaxy_node+" kill -9 "+line.split()[1])
