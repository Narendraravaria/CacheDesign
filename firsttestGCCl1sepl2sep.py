#459519442 = 337375824 + 122143618
#unified l1 and l2 with config
import math;
import os;
num1 =0
assoc1 = '4';
assoc2 = '4';
block_size1 = '64'
block_size2 = '64'
rep_p1 = 'l';
rep_p2 = 'l';
L1_cache_size = 256*1024;
L2_cache_size = 1024*1024;
#1u_sets = int(math.ceil(L1_cache_size/(int(block_size1)*int(assoc1))))
#L2u_sets = int(math.ceil(L2_cache_size/(int(block_size1)*int(assoc2))))
L1u_sets = int(math.ceil(L1_cache_size/(int(block_size1)*int(assoc1))))
L1i_sets = L1u_sets/2;
L1d_sets = L1u_sets/2;
L2u_sets = int(math.ceil(L2_cache_size/(int(block_size2)*int(assoc2))))
L2i_sets = L2u_sets/2;
L2d_sets = L2u_sets/2;
num1 = num1+1
#os.system("echo "+""+'>./output/GCC_L1L2unitest.txt')
os.system("echo " +str(num1)+'  l1 :'+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+'>> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('touch output1_file.txt')
os.system('chmod u=rwx,g=rx,o=r output1_file.txt')
#GCC
#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+" -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i");
								

#GO
#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size2+':'+assoc2+':'+rep_p2 + " -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/go.alpha 50 9 /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/2stone9.in OUT");

#ANAGRAM
os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:il2 il2:"+str(L2i_sets)+':'+block_size2+':'+assoc2+':'+rep_p2 + " -cache:dl2 dl2:"+str(L2d_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+ " -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.alpha  /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/words </home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.in > OUT");


os.system('cat output1_file.txt | grep -a "sim_num_insn" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "il1.accesses" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "il1.miss_rate" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "dl1.accesses" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "dl1.miss_rate" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "il2.accesses" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "il2.miss_rate" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "dl2.accesses" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
os.system('cat output1_file.txt | grep -a "dl2.miss_rate" >> ./output/ANAGRAM_L1_sepL2_septest.txt')
#os.system('rm output1_file.txt')


