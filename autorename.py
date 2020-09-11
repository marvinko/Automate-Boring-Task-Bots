import os 
import sys
def main(p,pp): 
	i = 0
	user = ''
	path = 'C:/Users/'+user+'/Desktop/Folder/page '+ pp +'/'
	for filename in os.listdir(path):
		dst ="v" + str(i+p) + ".jpg"
		print(filename+" -> "+dst)
		src = path + filename 
		dst = path + dst
		 
		os.rename(src, dst) 
		i += 1
if __name__ == '__main__': 
	main(int(sys.argv[1]),sys.argv[2]) 
