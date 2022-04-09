# This program prints Hello, world!

print('Print CSV contetn!')

import sys
import csv
with open('data.csv', newline='') as csvfile:
     csv.field_size_limit(sys.maxsize)
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print(', '.join(row))