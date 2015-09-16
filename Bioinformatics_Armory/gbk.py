import os
from Bio import Entrez

def entrez_search(gene, d_start, d_end):
    Entrez.email = "your_name@your_mail_server.com"
    term = '"%s"[Organism] AND %s:%s[PDAT]' %(gene,d_start,d_end)
    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    return record["Count"]
    
def main():
    os.chdir("D:\\workspace\\python\\Python\\Rosalind\\IBA")
    with open("gbk", "rU") as f:
        gene = f.readline().strip()
        d_start= f.readline().strip()
        d_end= f.readline().strip()
        print entrez_search(gene, d_start, d_end)

if __name__ == '__main__':
    main()