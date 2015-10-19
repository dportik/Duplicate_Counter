import sys
import shutil
import os
import numpy as np
'''
python duplicate_counter.py [directory with "JMPD002_index1.duplicates.out" files] [directory with "JMPD002_index1_R1.fq" files] [output file directory] [suffix for output file]

The 'Sample_indexXX_R1.fq' files are located in the pre-clean folder resulting from script 1
(1-PreCleanup) of the https://github.com/MVZSEQ/denovoTargetCapturePhylogenomics workflow.
The 'Sample_indexXX.duplicates.out' files are created during script 2 (2-ScrubReads).
This script simply counts the headers that match a certain string to count the number of reads
in both of the files, then calculate a percentage of duplicate reads present.

'Sample_indexXX.duplicates.out' format:
HISEQ05:409:C5VPLACXX:3:1101:9944:4644
HISEQ05:409:C5VPLACXX:3:1101:8925:8621
HISEQ05:409:C5VPLACXX:3:1101:20860:14294
HISEQ05:409:C5VPLACXX:3:1101:9111:27218

This script will search for the 'HISEQ' portion of the above lines.

'Sample_indexXX_R1.fq' format:
@HISEQ05:409:C5VPLACXX:3:1101:2229:2087/1
NTTAGCTAAAGAGAAAGCTGGTCAGGCAAGGTTACCTGATCTTAAAGATCCAGAAGCTGTTCAGAAATTCTTCCTTGAAGAGATTCAGCTTGGAGAAGAG
+
#4BDFFFFHHHHHJJJJJJJJIJJJJJJJJJHIJJJJJIJJJJJJJJJJJJJJJJJJIJIJJJJJJJJIJJJJJJHHHHHHFFFFFFEEDEEDDDDDDDD
@HISEQ05:409:C5VPLACXX:3:1101:2151:2206/1
GGTTGCCCGTGTGGTTGCTCAGAATGGTTTCATTCTTGTGTGGACCTTAATGCTAACACAGTCAATGCTTTGTGTCTTTTAGCTCCTCGACCTGTTCATG
+
CCBFFFFFHHHHHJIJJJJJJJJJJJJHIJJIJJJJJJIJIJJJJJJJJJJJJJJJJIJJJIJJJJJJJHHHHHHFFFFFFEEDEEEDDDDDDDCDDEEC

This script will search for the '@HISEQ' portion of the above lines.

If your lines don't have these headers, edit them below to find a relevant string.

Outputs file 'Duplication_Calculations_SUFFIX.txt' with format:
sample	total_reads	duplicate_reads	perc_duplicates
JMPD002_index10	848077	110014	12.97
JMPD002_index11	2332845	418071	17.92
JMPD002_index12	2844887	466966	16.41
JMPD002_index13	3966318	915663	23.09
JMPD002_index14	2738062	543384	19.85

##############
DEPENDENCIES:
numpy - Numerical Python
##############
------------------------
written for Python 2.7.3
Dan Portik
daniel.portik@berkeley.edu
October 2015
------------------------
'''
dups_directory = sys.argv[1]
os.chdir(dups_directory)

def percent_calc(x,y):
    percentage = float( ( float(x) / float(y)) * float(100))
    percentage = np.around(percentage, decimals = 2)
    return percentage
    
dup_dict = {}

for fl in os.listdir('.'):
    if fl.endswith('duplicates.out'):
        names = fl.split('.')
        sample = names[0]
        print "Counting duplicate reads in {}...".format(fl), '\n'
        fh_temp = open(fl, 'r')
        line_count = int(0)
        for line in fh_temp:
        	##### CHANGE STRING HERE FOR duplicates.out MATCH
            if line.startswith('HISEQ'):
                line_count+=1
        dup_dict[sample] = line_count
        fh_temp.close()
print dup_dict, '\n', '\n'

fq_directory = sys.argv[2]
os.chdir(fq_directory)

dups_list = []

string_list = []
string_list.append("sample,total_reads,duplicate_reads,perc_duplicates")

for fl in os.listdir('.'):
    if fl.endswith('R1.fq'):
        print "Counting all reads in {}...".format(fl)
        names = fl.split('_')
        sample = names[0]+'_'+names[1]
        fh_temp = open(fl, 'r')
        read_count = int(0)
        for line in fh_temp:
        	##### CHANGE STRING HERE FOR R1.fq MATCH
            if line.startswith('@HISEQ'):
                read_count+=1
        if sample in dup_dict:
            perc_dups = percent_calc(dup_dict[sample], read_count)
            print "For sample {0} there are {1}% duplicate reads.".format(sample, perc_dups), '\n'
            string_list.append("{0},{1},{2},{3}".format(sample, read_count, dup_dict[sample], perc_dups))
        fh_temp.close()

out_directory = sys.argv[3]
os.chdir(out_directory)

suffix = sys.argv[4]

out_name = 'Duplication_Calculations_{}.txt'.format(suffix)
fh_out = open(out_name, 'a')

for item in string_list:
    item = item.split(',')
    fh_out.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\n')
fh_out.close()
