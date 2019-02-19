#we only need the galaxy node for this test, no need to have all other nodes (or even the whole cluster)
nfsdir="/nfs-data"
master_node=`cat ../galaxy_node`
repetitions=4
testsize=52428800

echo "IOzone test of the nfs server ${master_node} with $repetitions repetitions"
date
ssh root@${master_node} mkdir ${nfsdir}/iozonetest/
mkdir results_iozone_${master_node}
scp aux_scripts/drop_caches.sh root@${master_node}:~/

for i in $(seq 1 ${repetitions}); do 
	echo "repetition ${i} of ${repetitions}, write and read $testsize KB"
	date
	ssh root@$master_node iozone -f ${nfsdir}/iozonetest/tmpfile${i} -w -i 0 -s $testsize -+n -r 1024 > results_iozone_${master_node}/repetition${i}_write.out
	#drop cache before read test
	ssh root@$master_node bash /root/drop_caches.sh
	ssh root@$master_node iozone -f ${nfsdir}/iozonetest/tmpfile${i} -i 1 -s $testsize -+n -r 1024 > results_iozone_${master_node}/repetition${i}_read.out
	#erase temporary file
	ssh root@$master_node rm ${nfsdir}/iozonetest/tmpfile${i}
done
ssh root@$master_node rm -rf ${nfsdir}/iozonetest


