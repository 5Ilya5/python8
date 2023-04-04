import json
import os
 
files=os.listdir('Data/')
for i in files:
    fout = open('Out/' + i, 'w')
    with open('Data/' + i, 'r') as f:
        for r in json.reader(f):
            if float(r[5]) <= 0.5:
                fout.write(f'{r[2]},{r[5]}\n')
    fout.close()
