#459519442 = 337375824 + 122143618
#unified l1 and l2 with config
import math;
import os;
num1 =0
assoc1 = '2';
assoc2 = '2';
block_size1 = '64'
block_size2 = '64'
rep_p1 = 'f';
rep_p2 = 'f';
L1_cache_size = 256*1024;
L2_cache_size = 1024*1024;
#1u_sets = int(math.ceil(L1_cache_size/(int(block_size1)*int(assoc1))))
#L2u_sets = int(math.ceil(L2_cache_size/(int(block_size1)*int(assoc2))))
L1u_sets = int(math.ceil(L1_cache_size/(int(block_size1)*int(assoc1))))
L1i_sets = L1u_sets/2;
L1d_sets = L1u_sets/2;
L2u_sets = int(math.ceil(L2_cache_size/(int(block_size2)*int(assoc2))))
num1 = num1+1
#os.system("echo "+""+'>./output/GCC_L1L2unitest.txt')
os.system("echo " +str(num1)+'  l1 :'+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+' l2:'+str(L2u_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+'>> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('touch output1_file.txt')
os.system('chmod u=rwx,g=rx,o=r output1_file.txt')
#GCC
#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:dl1 dl1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:il1 il1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+" -cache:il2 none " +" -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i");
#GO
#os.system("./sim-cache " +"-redir:sim ./output1_file.txt " + "-cache:il1 il1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+" -cache:il2 none " +" -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/go.alpha 50 9 /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/2stone9.in OUT");
#ANAGRAM
os.system("./sim-cache " +"-redir:sim ./output1_file.txt" + " -cache:il1 il1:"+str(L1i_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+" -cache:dl1 dl1:"+str(L1d_sets)+':'+block_size1+':'+assoc1+':'+rep_p1+ " -cache:dl2 ul2:"+str(L2u_sets)+':'+block_size2+':'+assoc2+':'+rep_p2+" -cache:il2 none " +" -tlb:itlb none -tlb:dtlb none" + " /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.alpha  /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/words </home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/anagram.in > OUT");

os.system('cat output1_file.txt | grep -a "sim_num_insn" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "il1.accesses" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "il1.miss_rate" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "dl1.accesses" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "dl1.miss_rate" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "ul2.accesses" >> ./output/ANAGRAM_L1_sepL2test.txt')
os.system('cat output1_file.txt | grep -a "ul2.miss_rate" >> ./output/ANAGRAM_L1_sepL2test.txt')
#os.system('rm output1_file.txt')
#./sim-cache -cache:dl1 dl1:1024:64:2:f -cache:il1 il1:1024:64:2:f -cache:il2 dl2 -cache:dl2 dl2:16384:64:1:f -tlb:itlb none -tlb:dtlb none /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/cc1.alpha -O /home/narendra/Dropbox/UTD/SEM-II/Computer\ Architecture/Project/simplescalar/benchmarks/1stmt.i  

