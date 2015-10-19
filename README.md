# Duplicate_Counter

python duplicate_counter.py [directory with "JMPD002_index1.duplicates.out" files] [directory with "JMPD002_index1_R1.fq" files] [output file directory] [suffix for output file]

The 'Sample_indexXX_R1.fq' files are located in the pre-clean folder resulting from script 1
(1-PreCleanup) of the https://github.com/MVZSEQ/denovoTargetCapturePhylogenomics workflow.
The 'Sample_indexXX.duplicates.out' files are created during script 2 (2-ScrubReads).
This script simply counts the headers that match a certain string to count the number of reads
in both of the files, then calculate a percentage of duplicate reads present.

'Sample_indexXX.duplicates.out' format:"
HISEQ05:409:C5VPLACXX:3:1101:9944:4644
HISEQ05:409:C5VPLACXX:3:1101:8925:8621
HISEQ05:409:C5VPLACXX:3:1101:20860:14294
HISEQ05:409:C5VPLACXX:3:1101:9111:27218
"
This script will search for the 'HISEQ' portion of the above lines.

'Sample_indexXX_R1.fq' format:"
@HISEQ05:409:C5VPLACXX:3:1101:2229:2087/1
NTTAGCTAAAGAGAAAGCTGGTCAGGCAAGGTTACCTGATCTTAAAGATCCAGAAGCTGTTCAGAAATTCTTCCTTGAAGAGATTCAGCTTGGAGAAGAG
+
44BDFFFFHHHHHJJJJJJJJIJJJJJJJJJHIJJJJJIJJJJJJJJJJJJJJJJJJIJIJJJJJJJJIJJJJJJHHHHHHFFFFFFEEDEEDDDDDDDD
@HISEQ05:409:C5VPLACXX:3:1101:2151:2206/1
GGTTGCCCGTGTGGTTGCTCAGAATGGTTTCATTCTTGTGTGGACCTTAATGCTAACACAGTCAATGCTTTGTGTCTTTTAGCTCCTCGACCTGTTCATG
+
CCBFFFFFHHHHHJIJJJJJJJJJJJJHIJJIJJJJJJIJIJJJJJJJJJJJJJJJJIJJJIJJJJJJJHHHHHHFFFFFFEEDEEEDDDDDDDCDDEEC
"
This script will search for the '@HISEQ' portion of the above lines.

If your lines don't have these headers, edit them below to find a relevant string.

Outputs file 'Duplication_Calculations_SUFFIX.txt' with format:"
sample	total_reads	duplicate_reads	perc_duplicates
JMPD002_index10	848077	110014	12.97
JMPD002_index11	2332845	418071	17.92
JMPD002_index12	2844887	466966	16.41
JMPD002_index13	3966318	915663	23.09
JMPD002_index14	2738062	543384	19.85
"
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

