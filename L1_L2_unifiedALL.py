#!/usr/bin/python
import os
import math

#cache-type, cache_set, cache_block_size, associativity, replace_poly
global num1;global num2;global num3
num1 =0;num2 =0;num3=0;
cache_types = ("unified", "Sep_L1_only","Sep_L1_L2");
associativity = ["1", "2", "4", "8"]; 

#r- random, f-fifo, l - lru
replace_polys = ["r", "f", "l"];

## Initial cache size L1 = 256KB, L2 = 1MB, Block Size= 64Bytes
L1_cache_size = 256*1024;
L2_cache_size = 1024*1024;
cache_block_size = ["32","64"]; 

excu_termi = "";
for cache_ty in cache_types:
	if cache_ty == "unified":
		for block_size in cache_block_size:#block size for l1
			for rep_p1 in replace_polys:# replacement policy for L1
				for assoc1 in associativity:# Associativity for L1
					L1u_sets = int(math.ceil(L1_cache_size/(int(block_size)*int(assoc1))))
					for rep_p2 in replace_polys:# replacement policy for L2
						#for block_size in cache_block_size:#block size for l2
						for assoc2 in associativity:# Associativity for L2
							L2u_sets = int(math.ceil(L2_cache_size/(int(block_size)*int(assoc2))))
							#GCC Benchmark
							num1 = num1 +1
							os.system("echo " +str(num1)+'  l1 :'+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+'>> ./output/GCC_L1L2uniAll.txt')
							os.system('touch output_file.txt')
							os.system('chmod u=rwx,g=rx,o=r output_file.txt')
								
							os.system("./sim-cache " +"-redir:sim ./output_file.txt " + "-cache:il1 dl1 -cache:dl1 ul1:"+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 none -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i");
								
							os.system('cat output_file.txt | grep -a "sim_num_insn" >> ./output/GCC_L1L2uniAll.txt')
							os.system('cat output_file.txt | grep -a "ul1.accesses" >> ./output/GCC_L1L2uniAll.txt')
							os.system('cat output_file.txt | grep -a "ul1.miss_rate" >> ./output/GCC_L1L2uniAll.txt')
							os.system('cat output_file.txt | grep -a "ul2.accesses" >> ./output/GCC_L1L2uniAll.txt')
							os.system('cat output_file.txt | grep -a "ul2.miss_rate" >> ./output/GCC_L1L2uniAll.txt')
							os.system('rm output_file.txt')
							#GO Benchmark
							num2 =num2 +1
							os.system("echo " +str(num2)+'  l1 :'+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+'>> ./output/GO_L1L2uniAll.txt')
							os.system('touch output2_file.txt')
							os.system('chmod u=rwx,g=rx,o=r output2_file.txt')
								
							os.system("./sim-cache " +"-redir:sim ./output2_file.txt " + "-cache:il1 dl1 -cache:dl1 ul1:"+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 none -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/go.alpha 50 9 /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/2stone9.in OUT");
								
							os.system('cat output2_file.txt | grep -a "sim_num_insn" >> ./output/GO_L1L2uniAll.txt')
							os.system('cat output2_file.txt | grep -a "ul1.accesses" >> ./output/GO_L1L2uniAll.txt')
							os.system('cat output2_file.txt | grep -a "ul1.miss_rate" >> ./output/GO_L1L2uniAll.txt')
							os.system('cat output2_file.txt | grep -a "ul2.accesses" >> ./output/GO_L1L2uniAll.txt')
							os.system('cat output2_file.txt | grep -a "ul2.miss_rate" >> ./output/GO_L1L2uniAll.txt')
							os.system('rm output2_file.txt')
							#ANAGRAM Benchmark
							num3 =num3 +1
							os.system("echo " +str(num3)+'  l1 :'+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+'>> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('touch output3_file.txt')
							os.system('chmod u=rwx,g=rx,o=r output3_file.txt')
								
							os.system("./sim-cache " +"-redir:sim ./output3_file.txt " + "-cache:il1 dl1 -cache:dl1 ul1:"+str(L1u_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 none -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.alpha  /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/words </home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.in > OUT");
								
							os.system('cat output3_file.txt | grep -a "sim_num_insn" >> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('cat output3_file.txt | grep -a "ul1.accesses" >> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('cat output3_file.txt | grep -a "ul1.miss_rate" >> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('cat output3_file.txt | grep -a "ul2.accesses" >> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('cat output3_file.txt | grep -a "ul2.miss_rate" >> ./output/ANAGRAM_L1L2uniAll.txt')
							os.system('rm output3_file.txt')
							






