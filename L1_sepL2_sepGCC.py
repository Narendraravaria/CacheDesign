#L1 Separate L2 Separate
#GCC  Benchmark
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
#L2_data = 512KB and L2_instruction = 512KB
L1_cache_size = 256*1024;
L2_cache_size = 1024*1024;
cache_block_size = ["32","64"]; 

excu_termi = "";
for cache_ty in cache_types:
	if cache_ty == "Sep_L1_L2":
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
							L2i_sets = L2u_sets/2;
							L2d_sets = L2u_sets/2;
							#GCC Benchmark								
							num1 = num1 +1
							print '>',num1
							os.system("echo " +str(num1)+'  l1 :'+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+' l2:'+str(L2i_sets)+':'+block_size+':'+assoc2+':'+rep_p2+'>> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('touch output_file.txt')
							os.system('chmod u=rwx,g=rx,o=r output_file.txt')
								
							#os.system("./sim-cache " +"-redir:sim ./output_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size+':'+assoc2+':'+rep_p2 + " -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i");
							#os.system("./sim-cache " +"-redir:sim ./output_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size+':'+assoc2+':'+rep_p2 + " -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/go.alpha 50 9 /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/2stone9.in OUT");	
							os.system("./sim-cache " +"-redir:sim ./output_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size+':'+assoc2+':'+rep_p2 + " -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.alpha  /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/words </home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.in > OUT");	
							os.system('cat output_file.txt | grep -a "sim_num_insn" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "il1.accesses" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "il1.miss_rate" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "dl1.accesses" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "dl1.miss_rate" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "il2.accesses" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "il2.miss_rate" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "dl2.accesses" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							os.system('cat output_file.txt | grep -a "dl2.miss_rate" >> ./output/ANAGRAM_L1_sepL2_sep.txt')
							#os.system('rm output_file.txt')


