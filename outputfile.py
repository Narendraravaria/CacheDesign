#creat file and save output in that
import re
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GCC_L1L2uni.txt')#windows
#hand = open('/home/narendra/Dropbox/UTD/SEM-II/Computer Architecture/Project/simplescalar/simplesim-3.0/output/GCC_L1L2uni.txt')#linux
count = 1
dic = {'l':1,'f':0.05,'r':0}
L1_cache_size = 75
L2_cache_size = 150
uni= 0
sep_uni = 0.25
sep_sep = 1

handw = open('CPIOpt.txt',"w+")
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^ul1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^ul1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        L2_accesses = (re.findall('[0-9]+',line))
        print '******',int(L2_accesses[1])
        #handw.write((L2_accesses[1])+" ")
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        L2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(L2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) ) + 70 * ( float(L2_MissRate[1]) * ( float(L2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == 1:cpi_GCC_uni=CPI
        elif CPI <= cpi_GCC_uni:
            cpi_GCC_uni =CPI
            cpi_GCC_uni_conf = s
        if count == 1:opt_GCC_uni=cost_CPI
        elif cost <= opt_GCC_uni:
            opt_GCC_uni = cost_CPI
            opt_GCC_uni_conf = s
        handw.write('GCC'+" "+"L1L2Unified"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
 
hand.close()
#GO
c1=count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GO_L1L2uni.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^ul1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^ul1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        L2_accesses = (re.findall('[0-9]+',line))
        print '******',int(L2_accesses[1])
        #handw.write((L2_accesses[1])+" ")
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        L2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(L2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) ) + 70 * ( float(L2_MissRate[1]) * ( float(L2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c1:cpi_GO_uni=CPI
        elif CPI <= cpi_GO_uni:
            cpi_GO_uni = CPI
            cpi_GO_uni_conf = s
        if count == c1:opt_GO_uni=cost_CPI
        elif cost <= opt_GO_uni:
            opt_GO_uni = cost_CPI
            opt_GO_uni_conf = s
        handw.write('GO'+" "+"L1L2Unified"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count

hand.close()
#ANAGRAM
c2 =count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\ANAGRAM_L1L2uni.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^ul1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^ul1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        L2_accesses = (re.findall('[0-9]+',line))
        print '******',int(L2_accesses[1])
        #handw.write((L2_accesses[1])+" ")
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        L2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(L2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) ) + 70 * ( float(L2_MissRate[1]) * ( float(L2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c2:cpi_ANAGRAM_uni=CPI
        elif CPI <= cpi_ANAGRAM_uni:
            cpi_ANAGRAM_uni = CPI
            cpi_ANAGRAM_uni_conf = s
        if count == c2:opt_ANAGRAM_uni=cost_CPI
        elif cost <= opt_ANAGRAM_uni:
            opt_ANAGRAM_uni = cost_CPI
            opt_ANAGRAM_uni_conf = s
        handw.write('ANAGRAM'+" "+"L1L2Unified"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
hand.close()
#L1 Separate L2 unified
#GCC
c3 = count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GCC_L1_sepL2.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        U2_accesses = (re.findall('[0-9]+',line))
        print '******',int(U2_accesses[1])
        #handw.write((U2_accesses[1])+" ")
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        U2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(U2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(U2_MissRate[1]) * ( float(U2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(sep_uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c3:cpi_GCC_sep_uni=CPI
        elif CPI <= cpi_GCC_sep_uni:
            cpi_GCC_sep_uni = CPI
            cpi_GCC_sep_uni_conf = s
        if count == c3:opt_GCC_sep_uni=cost_CPI
        elif cost <= opt_GCC_sep_uni:
            opt_GCC_sep_uni = cost_CPI
            opt_GCC_sep_uni_conf = s
        handw.write('GCC'+" "+"L1SepL2Uni"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
hand.close()
#GO
c4 = count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GO_L1_sepL2.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        U2_accesses = (re.findall('[0-9]+',line))
        print '******',int(U2_accesses[1])
        #handw.write((U2_accesses[1])+" ")
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        U2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(U2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(U2_MissRate[1]) * ( float(U2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(sep_uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c4:cpi_GO_sep_uni=CPI
        elif CPI <= cpi_GO_sep_uni:
            cpi_GO_sep_uni = CPI
            cpi_GO_sep_uni_conf = s
        if count == c4:opt_GO_sep_uni=cost_CPI
        elif cost <= opt_GO_sep_uni:
            opt_GO_sep_uni = cost_CPI
            opt_GO_sep_uni_conf = s
        handw.write('GO'+" "+"L1SepL2Uni"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
hand.close()
#ANAGRAM
c5 = count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\ANAGRAM_L1_sepL2.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
        count = count +1
    elif re.findall('^ul2.accesses',line):
        print "*****",line
        U2_accesses = (re.findall('[0-9]+',line))
        print '******',int(U2_accesses[1])
        #handw.write((U2_accesses[1])+" ")
        
    elif re.findall('^ul2.miss_rate',line):
        print "<<<<<",line
        U2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(U2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(U2_MissRate[1]) * ( float(U2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*(sep_uni)+0.04*(L1_policy)+0.04*(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        print "<<<<<<>>>>..",count
        if count-1 == c5:print c5;cpi_ANAGRAM_sep_uni=CPI
        elif CPI <= cpi_ANAGRAM_sep_uni:
            cpi_ANAGRAM_sep_uni = CPI
            cpi_ANAGRAM_sep_uni_conf = s
        if count-1 == c5:print c5;opt_ANAGRAM_sep_uni=cost_CPI
        elif cost <= opt_ANAGRAM_sep_uni:
            opt_ANAGRAM_sep_uni = cost_CPI
            opt_ANAGRAM_sep_uni_conf = s
        handw.write('ANAGRAM'+" "+"L1SepL2Uni"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        
        print count
hand.close()
#L1 separate L2 separate
#GCC
c6 =count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GCC_L1_sepL2_sep.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
    elif re.findall('^il2.miss_rate',line):
        print ">>>>",line
        I2_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(I2_MissRate[1])
        #handw.write((I2_MissRate[1])+" ")
    elif re.findall('^il2.accesses',line):
        print "++++",line
        I2_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(I2_accesses[1])
        #handw.write((I2_accesses[1])+" ")
    elif re.findall('^dl2.accesses',line):
        print "*****",line
        D2_accesses = (re.findall('[0-9]+',line))
        print '******',int(D2_accesses[1])
        #handw.write((D2_accesses[1])+" ")
    elif re.findall('^dl2.miss_rate',line):
        print "<<<<<",line
        D2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(D2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(D2_MissRate[1]) * ( float(D2_accesses[1])/int(Total_accesses[0])) +float(I2_MissRate[1]) * ( float(I2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*float(L1_cache_size)+0.3*float(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*float(sep_sep)+0.04*float(L1_policy)+0.04*float(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c6:cpi_GCC_sep_sep=CPI
        elif CPI <= cpi_GCC_sep_sep:
            cpi_GCC_sep_sep = CPI
            cpi_GCC_sep_sep_conf = s
        if count == c6:opt_GCC_sep_sep=cost_CPI
        elif cost <= opt_GCC_sep_sep:
            opt_GCC_sep_sep = cost_CPI
            opt_GCC_sep_sep_conf = s
        handw.write('GCC'+" "+"L1SepL2Sep"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
     
hand.close()
#GO
c7 =count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\GO_L1_sepL2_sep.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
    elif re.findall('^il2.miss_rate',line):
        print ">>>>",line
        I2_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(I2_MissRate[1])
        #handw.write((I2_MissRate[1])+" ")
    elif re.findall('^il2.accesses',line):
        print "++++",line
        I2_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(I2_accesses[1])
        #handw.write((I2_accesses[1])+" ")
    elif re.findall('^dl2.accesses',line):
        print "*****",line
        D2_accesses = (re.findall('[0-9]+',line))
        print '******',int(D2_accesses[1])
        #handw.write((D2_accesses[1])+" ")
    elif re.findall('^dl2.miss_rate',line):
        print "<<<<<",line
        D2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(D2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(D2_MissRate[1]) * ( float(D2_accesses[1])/int(Total_accesses[0])) +float(I2_MissRate[1]) * ( float(I2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*float(L1_cache_size)+0.3*float(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*float(sep_sep)+0.04*float(L1_policy)+0.04*float(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c7:cpi_GO_sep_sep=CPI
        elif CPI <= cpi_GO_sep_sep:
            cpi_GO_sep_sep = CPI
            cpi_GO_sep_sep_conf = s
        if count == c7:opt_GO_sep_sep=cost_CPI
        elif cost <= opt_GO_sep_sep:
            opt_GO_sep_sep = cost_CPI
            opt_GO_sep_sep_conf = s
        handw.write('GO'+" "+"L1SepL2Sep"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
     
hand.close()
#ANAGRAM
c8 = count
hand = open('C:\Users\Narendra\Dropbox\UTD\SEM-II\Computer Architecture\Project\simplescalar\simplesim-3.0\output\ANAGRAM_L1_sepL2_sep.txt')#windows
for line in hand:
    line = line.rstrip()
    if re.findall('^[0-9]+',line):
        s = line.split()
        s1 = s[2].split(':')
        s2 = s[3].split(':')
        print s1,'\n',s2
        l1 = s1[1]+":"+s1[2]+":"+s1[3]+":"+s1[4]
        l2 = s2[1]+":"+s2[2]+":"+s2[3]+":"+s2[4]
        for k in dic:
            if s1[4] == k:
                L1_policy = dic[k]
                print "L1_policy",L1_policy
            if s2[4] == k:
                L2_policy = dic[k]
                print "L2_policy",L2_policy
        handw.write(str(count)+" "+l1+" "+l2+' ')
        print '@@@@@',line
    elif re.findall('^sim_num_insn',line):
        print "!!!!!!",line
        Total_accesses = (re.findall('[0-9.]+',line))
        print '!!!!!!',int(Total_accesses[0])
        #handw.write((Total_accesses[0])+" ")
    elif re.findall('^il1.miss_rate',line):
        print ">>>>",line
        L1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(L1_MissRate[1])
        #handw.write((L1_MissRate[1])+" ")
    elif re.findall('^il1.accesses',line):
        print "++++",line
        L1_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(L1_accesses[1])
        #handw.write((L1_accesses[1])+" ")
    elif re.findall('^dl1.miss_rate',line):
        print ">>>><<<<",line
        D1_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>><<<<<',float(D1_MissRate[1])
        #handw.write((D1_MissRate[1])+" ")
    elif re.findall('^dl1.accesses',line):
        print "++++*****",line
        D1_accesses = (re.findall('[0-9]+',line))
        print '+++++*****',int(D1_accesses[1])
        #handw.write((D1_accesses[1])+" ")
    elif re.findall('^il2.miss_rate',line):
        print ">>>>",line
        I2_MissRate = (re.findall('[0-9.]+',line))
        print '>>>>>',float(I2_MissRate[1])
        #handw.write((I2_MissRate[1])+" ")
    elif re.findall('^il2.accesses',line):
        print "++++",line
        I2_accesses = (re.findall('[0-9]+',line))
        print '+++++',int(I2_accesses[1])
        #handw.write((I2_accesses[1])+" ")
    elif re.findall('^dl2.accesses',line):
        print "*****",line
        D2_accesses = (re.findall('[0-9]+',line))
        print '******',int(D2_accesses[1])
        #handw.write((D2_accesses[1])+" ")
    elif re.findall('^dl2.miss_rate',line):
        print "<<<<<",line
        D2_MissRate = (re.findall('[0-9.]+',line))
        print '<<<<<<',float(D2_MissRate[1])
        CPI_ideal =1
        CPI = CPI_ideal + 4 * ( float(L1_MissRate[1]) * (float(L1_accesses[1])/int(Total_accesses[0])) +float(D1_MissRate[1]) * (float(D1_accesses[1])/int(Total_accesses[0]))) + 70 * ( float(D2_MissRate[1]) * ( float(D2_accesses[1])/int(Total_accesses[0])) +float(I2_MissRate[1]) * ( float(I2_accesses[1])/int(Total_accesses[0])))
        print "######CPI##########"
        print CPI
        #cost = 0.35*(L1_cache_size)+0.3*(L2_cache_size)+0.085*(L1_associativity)+0.085*(L2_associativity)+0.1*(Unified/Separate)+0.04*(L1_repalcement_policy)+0.04*(L2_repalcement_policy)+0*(Block_size)
        cost = 0.35*float(L1_cache_size)+0.3*float(L2_cache_size)+0.085*(float(s1[3]))+0.085*(float(s2[3]))+0.1*float(sep_sep)+0.04*float(L1_policy)+0.04*float(L2_policy)
        print 'COST'
        print (cost)
        cost_CPI = cost*CPI
        print cost_CPI
        if count == c8:cpi_ANAGRAM_sep_sep=CPI
        elif CPI <= cpi_ANAGRAM_sep_sep:
            cpi_ANAGRAM_sep_sep = CPI
            cpi_ANAGRAM_sep_sep_conf = s
        if count == c8:opt_ANAGRAM_sep_sep=cost_CPI
        elif cost <= opt_ANAGRAM_sep_sep:
            opt_ANAGRAM_sep_sep = cost_CPI
            opt_ANAGRAM_sep_sep_conf = s
        handw.write('ANAGRAM'+" "+"L1SepL2Sep"+" "+str(CPI)+" "+str(cost)+" "+str(cost_CPI)+"\n")
        count = count +1
        print count
hand.close()
handx = open('OptimumResult.txt',"w+")
print 'OPtimize CPI #################'
print "Optimum value GCC unified ",cpi_GCC_uni
print "Optimum Configuration GCC unified ",cpi_GCC_uni_conf
print "Optimum value GO unified ",cpi_GO_uni
print "Optimum Configuration GO unified ",cpi_GO_uni_conf
print "Optimum value ANAGRAM unified ",cpi_ANAGRAM_uni
print "Optimum Configuration ANAGRAM unified ",cpi_ANAGRAM_uni_conf
print "Optimum value GCC Separate unified ",cpi_GCC_sep_uni
print "Optimum Configuration GCC Separate unified ",cpi_GCC_sep_uni_conf
print "Optimum value GO Separate unified ",cpi_GO_sep_uni
print "Optimum Configuration GO Separate unified ",cpi_GO_sep_uni_conf
print "Optimum value ANAGRAM Separate unified ",cpi_ANAGRAM_sep_uni
print "Optimum Configuration ANAGRAM Separate unified ",cpi_ANAGRAM_sep_uni_conf
print "Optimum value GCC Separate Separate ",cpi_GCC_sep_sep
print "Optimum Configuration GCC Separate Separate ",cpi_GCC_sep_sep_conf
print "Optimum value GO Separate Separate ",cpi_GO_sep_sep
print "Optimum Configuration GO Separate Separate ",cpi_GO_sep_sep_conf
print "Optimum value ANAGRAM Separate Separate ",cpi_ANAGRAM_sep_sep
print "Optimum Configuration ANAGRAM Separate Separate ",cpi_ANAGRAM_sep_sep_conf
handx.write("Optimum value GCC unified "+str(opt_GCC_uni)+"\n")
handx.write("Optimum Configuration GCC unified "+str(opt_GCC_uni_conf)+"\n")
handx.write("Optimum value GO unified "+str(opt_GO_uni)+"\n")
handx.write("Optimum Configuration GO unified "+str(opt_GO_uni_conf)+"\n")
handx.write("Optimum value ANAGRAM unified "+str(opt_ANAGRAM_uni)+"\n")
handx.write("Optimum Configuration ANAGRAM unified "+str(opt_ANAGRAM_uni_conf)+"\n")
handx.write("Optimum value GCC Separate unified "+str(opt_GCC_sep_uni)+"\n")
handx.write("Optimum Configuration GCC Separate unified "+str(opt_GCC_sep_uni_conf)+"\n")
handx.write("Optimum value GO Separate unified "+str(opt_GO_sep_uni)+"\n")
handx.write("Optimum Configuration GO Separate unified "+str(opt_GO_sep_uni_conf)+"\n")
handx.write("Optimum value ANAGRAM Separate unified "+str(opt_ANAGRAM_sep_uni)+"\n")
handx.write("Optimum Configuration ANAGRAM Separate unified "+str(opt_ANAGRAM_sep_uni_conf)+"\n")
handx.write("Optimum value GCC Separate Separate "+str(opt_GCC_sep_sep)+"\n")
handx.write("Optimum Configuration GCC Separate Separate "+str(opt_GCC_sep_sep_conf)+"\n")
handx.write("Optimum value GO Separate Separate "+str(opt_GO_sep_sep)+"\n")
handx.write("Optimum Configuration GO Separate Separate "+str(opt_GO_sep_sep_conf)+"\n")
handx.write("Optimum value ANAGRAM Separate Separate "+str(opt_ANAGRAM_sep_sep)+"\n")
handx.write("Optimum Configuration ANAGRAM Separate Separate "+str(opt_ANAGRAM_sep_sep_conf)+"\n")

handx.close()
handw.close()


