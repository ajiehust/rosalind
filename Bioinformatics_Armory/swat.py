import os,urllib
from Bio import SeqIO
os.chdir("D:\\workspace\\python\\Python\\Rosalind\\IBA")
gene = open("swat").readline().strip().split(" ")
uri = "http://www.uniprot.org/uniprot/%s.fasta"
p1 = SeqIO.read(urllib.urlopen(uri %gene[0]),"fasta")
p2 = SeqIO.read(urllib.urlopen(uri %gene[1]),"fasta")
print p1.format("fasta")
print p2.format("fasta")