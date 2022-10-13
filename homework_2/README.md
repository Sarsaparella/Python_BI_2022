# Homework 2 - FastQ Filtrator

This script allows you to filter data from .fastq files by several parameters:

- Length of a sequence
- GC content
- Quality of read

After filtration sequences saved into output files. 

FastQ filtrator core function - ‘main’ recives following parameters:

- input_fastq - path to file in format of string
- output_file_prefix - prefix of output files
- save_filtered - creates ‘{output_file_prefix}_failed.fastq” file and saves sequences that did not passed filtration in it if save_filtered = True
- length_bound - allowed length of a sequence, given a as tuple or as one upper bound
- gc_bound - allowed GC-percent given as a tuple or as one upper bound
- quality_threshold - reads with quality below this threshold will be filtered