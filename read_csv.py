"""
read a CSV file and return the rows from 
"""
import sys
import csv
from csv import Dialect,QUOTE_MINIMAL,Sniffer

class Msexcel(Dialect):
    """Describe the usual properties of MSExcel-generated CSV files. with a ; delimeter"""
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = QUOTE_MINIMAL
csv.register_dialect("msexcel", Msexcel)

def readCSV(filename='data.csv',jumpheader=True):
	rows=[]
	with open(filename,'r') as file:
		reader = csv.reader(file,dialect='msexcel')
		if jumpheader:
			next(reader) #skip header if exists
		for row in reader:
			rows.append(row)
	return rows
if __name__ == '__main__':
	print(readCSV(sys.argv[1],False))
	print(csv.list_dialects())

