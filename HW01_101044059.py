# Adnan EROL
# 101044059
#
# Bu program arguman olarak bir directory alir ve icindeki dosyalarin hash 
# kodlarini cikarir. Ayni hash koda sahip iki dosyanin isimlerini ve hash
# kodlarini ekranda gosterir.
import os.path
import sys
import hashlib

dizinIsmi = sys.argv[1]
hashCodes = []
fileNames = []

#dizin icerisindeki dosya listesini alir
dosyalar = os.listdir(dizinIsmi)
#listeyi dolasma 
for file in dosyalar:
	#dosya ismini uygun sekilde ayarlar
	dosyaIsmi = dizinIsmi+"/"+file
	#print dosyaIsmi
	fileNames.append(dosyaIsmi)
	
	#eger dosya ise
	if os.path.isfile(dosyaIsmi):
		#bilgisini ekrana yazar
		imageFile = open(dosyaIsmi).read()
		#print hashlib.md5(imageFile).hexdigest()
		hashCodes.append(hashlib.md5(imageFile).hexdigest())


#Dosyalar ve hash kodlari ekranda gosterilir
hashLenght = len(hashCodes)
print hashLenght
for i in range(0, hashLenght):
    print hashCodes[i]
    print fileNames[i]
    print '\n'
    
 
#ayni hash koda sahip dosyalar bulunur   
i = 1
while (i < hashLenght):
	j = i + 1
	while(j < hashLenght):
		if hashCodes[i] == hashCodes[j]:
			print '----------------------------------'
			print 'Bu dosyalarin hash kodlari aynidir'
			print fileNames[i]
			print fileNames[j]
			print hashCodes[i]
			print '----------------------------------'
		j = j + 1
	i = i + 1
