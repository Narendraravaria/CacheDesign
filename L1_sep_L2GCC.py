#L1 Separate L2 unified 
#Gcc Benchmark
#!/usr/bin/python
import os
import math

global num1;
num1 =0;
cache_types = ("unified", "Sep_L1_only","Sep_L1_L2");
associativity = ["1", "2", "4", "8"]; 

#r- random, f-fifo, l - lru
replace_polys = ["r", "f", "l"];

## Initial cache size L1 = 256KB, L2 = 1MB, Block Size= 64Bytes
#L1_data = 128KB and L1_instruction = 128KB
L1_cache_size = 256*1024;
L2_cache_size = 1024*1024;
cache_block_size = ["32","64"]; 

excu_termi = "";
for cache_ty in cache_types:
	if cache_ty == "Sep_L1_only":
		for block_size in cache_block_size:#block size for L1
			for rep_p1 in replace_polys:# replacement policy for L1
				for assoc1 in associativity:# Associativity for L1
					L1u_sets = int(math.ceil(L1_cache_size/(int(block_size)*int(assoc1))))
					L1i_sets = L1u_sets/2;
					L1d_sets = L1u_sets/2;
					for rep_p2 in replace_polys:# replacement policy for L2
						#for block_size in cache_block_size:#block size for L2
						for assoc2 in associativity:# Associativity for L2
							L2u_sets = int(math.ceil(L2_cache_size/(int(block_size)*int(assoc2))))
							#GCC Benchmark								
							num1 = num1 +1
							print num1;
							os.system("echo " +str(num1)+'  l1 :'+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+'>> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('touch output1_file.txt')
							os.system('chmod u=rwx,g=rx,o=r output1_file.txt')
							
							#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + " -cache:dl1 dl1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:il1 il1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+" -cache:il2 none " +" -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i");
							#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+" -cache:il2 none "+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/go.alpha 50 9 /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/2stone9.in OUT");
							os.system("./sim-cache " +"-redir:sim ./output1_file.txt" + " -cache:il1 il1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size+':'+assoc2+':'+rep_p2+" -cache:il2 none " +" -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.alpha  /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/words </home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.in > OUT");
							os.system('cat output1_file.txt | grep -a "sim_num_insn" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "il1.accesses" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "il1.miss_rate" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "dl1.accesses" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "dl1.miss_rate" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "ul2.accesses" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('cat output1_file.txt | grep -a "ul2.miss_rate" >> ./output/ANAGRAM_L1_sepL2.txt')
							os.system('rm output1_file.txt')
							
								
