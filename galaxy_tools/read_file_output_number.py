import tempfile
import os
import sys

#get parameters
if len(sys.argv) != 3:
	print("Usage: python "+sys.argv[0]+" input.txt output.txt")
        sys.exit(1)
inputfile = sys.argv[1]
outputfile = sys.argv[2]

#make a temp file to write output, otherwise galaxy may think we are done before we are done
(fd, tn_file) = tempfile.mkstemp(suffix=".txt")
os.close(fd)

#read input file and do stupid computation (count the number of 'a's)
arq = open(inputfile, "r")

over = 0
count = 0
while over == 0:
	data = arq.read(1048576) #read in 1MB blocks
	if len(data) < 1048576:
		over = 1
	count += data.count('a')
arq.close()

#write output
arq = open(tn_file, "w")
arq.write(str(count)+"\n")
arq.close()
os.system("mv "+tn_file+" "+outputfile)
