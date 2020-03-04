# Genome wide identification of heat shock elements
This script is designed to identify heat shock elements (HSEs) from the promoter sequence of genes.
## Getting Started
This script runs under Linux.
You need to install bedtools(https://github.com/arq5x/bedtools2/releases) and biopython(https://biopython.org/wiki/Download) before running the script and add them to the environment variables.
### You need to prepare these input files
- Reference genome sequence (*fasta*)
- Coding sequence of genes (*fasta*)
- Genome annotation (*Must be in gff3 format*)
- Genomic chromosome length (*tab delimited*)

An example of a chromosome length file

![blockchain](https://github.com/biozhp/hse/blob/master/images/Fig1.png)

Once you have all the files ready, you can run this script!
     
### Usages
     sh ./run_pipeline.sh cds.fa gene.gff3 genome_chr_length.txt genome.fa output_file

**NOTICE:** The order of the input files cannot be changed!

### Output
This script only outputs one file. Format is as follows:

![blockchain](https://github.com/biozhp/hse/blob/master/images/Fig2.png)

- The first column is the gene ID of the promoter containing HSE.
- The second and third column are the position of HSEs on the promoter.
- The fourth column is the sequence of HSEs.
- The number in the fifth column is the subunits of HSEs. “G” and “C” represent the first subunit sequence with 5’-NGAAN-3’ and 5’-NTTCN-3’, respectively.
- The sixth column is the mismatched nucleotide. “NA” means HSEs do not contain mismatched nucleotide.
- The seventh column is the position of mismatched nucleotide. “1:2” represent the 2nd position in the first subunit.

## Scripts Details
The scripts used for identifying heat shock elements (HSEs) contain the following steps:

1) The script “max_cds_length.py” was used to collect the transcription start sites of each gene according to the genome annotation GFF file.
2) The script “seq_bed.py” was used to create the bed (Browser Extensible Data) file for each promoter which include the chromosome number, starting and ending positions, gene id and strand information.
3) The software “bedtools” was used to extract the promoter sequence.
4) The script “hse_call.py” was used to identify HSEs with regular expressions from promoter sequence.
5) The scripts “hse_result.py”, “hse_mismatch.py” and “hse_pos.py” were used to characterize and classify the identified HSEs.

## Citation
Zhao P, Javed S, Shi X, Wu B, Zhang D, Xu S and Wang X (2020) Varying Architecture of Heat Shock Elements Contributes to Distinct Magnitudes of Target Gene Expression and Diverged Biological Pathways in Heat Stress Response of Bread Wheat. Front. Genet. 11:30. doi: 10.3389/fgene.2020.00030

## Contact
For any bugs/issues/suggestions, please send emails to: Peng Zhao pengzhao@nwafu.edu.cn.
