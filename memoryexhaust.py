#! python3
#1.3 trillion words generated 1,338,925,209,984‬ = 54^7 combinations
#exhausts available memory to 94% and results MemoryError
import string

chars1= chars2 = chars3 = chars4 = chars5 = chars6 = chars7 = list(string.ascii_letters)

words = [''.join((char1,char2,char3,char4,char5,char6,char7))
	for char1 in chars1
	for char2 in chars2
	for char3 in chars3
	for char4 in chars4
	for char5 in chars5
	for char6 in chars6
	for char7 in chars7]
print(len(words))