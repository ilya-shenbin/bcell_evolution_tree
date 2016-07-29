# takes migmap output filename
# then extracts CDR3 regions from it
# and saves them into FASTA file format
import numpy as np
import pandas as pd
from collections import defaultdict

migmap_filename = "/home/vuvarov/Desktop/project/out_migmap_daudi.csv"
out_filename = "/home/vuvarov/bioinf2016/project/out_migmap_daudi.fasta"

migmap_df = pd.read_csv(migmap_filename, sep='\t')

multidict = defaultdict(list)

for i in range(len(migmap_df.index)):
    #print migmap_df['cdr3nt'][i]
    multidict[migmap_df['cdr3nt'][i]].append(i)

out_file = open(out_filename, 'w')

for key, value in multidict.items():
    out_file.write('> ')
    for id in value:
        out_file.write(str(id) + ' ')
    out_file.write('\n')
    out_file.write(key)
    out_file.write('\n')

#print df

#print migmap_dataframe['cdr3nt'][0]
#print type(migmap_dataframe['cdr3nt'][1])

#migmap_dataframe

#print multidict