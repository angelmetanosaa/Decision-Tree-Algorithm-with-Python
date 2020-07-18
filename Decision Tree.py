from random import randint
import csv
from operator import itemgetter
import pandas 
import math
	
#Dekode kromosom
gen = 80
kromosom = 15
individu = []
datalatih =[]
def populasi ():
	biner = []
	for i in range(kromosom) :
			y = randint(0,1)
			biner.append(y)
	individu.append(biner)
	return individu
a = 0
for a in range(gen):
	populasi()
tampung = populasi()

hasil = []
def konversi() :
	for i in range (len(tampung)):
		if (tampung[i][0] == 1 and tampung[i][1] == 1 and tampung[i][2] == 1) :
			suhu = "Tinggi"
		elif (tampung[i][0] == 1 and tampung[i][1] == 1 and tampung[i][2] == 0) or (tampung[i][0] == 1 and tampung[i][1] == 0 and tampung[i][2] == 1) or (tampung[i][0] == 0 and tampung[i][1] == 1 and tampung[i][2] == 1):
			suhu = "Normal"
		elif(tampung[i][0] == 0 and tampung[i][1] == 0 and tampung[i][2] == 0):
			suhu = '-'
		else :
			suhu = "Rendah"

		if (tampung[i][3] == 1 and tampung[i][4] == 1 and tampung[i][5] == 1 and tampung[i][6] == 1) :
			waktu = "Pagi"
		elif (tampung[i][3] == 1 and tampung[i][4] == 1 and tampung[i][5] == 1 and tampung[i][6] == 0 ) or (tampung[i][3] == 1 and tampung[i][4] == 0 and tampung[i][5] == 1 and tampung[i][6] == 1) or (tampung[i][3] == 1 and tampung[i][4] == 1 and tampung[i][5] == 0 and tampung[i][6] == 1) or (tampung[i][3] == 0 and tampung[i][4] == 1 and tampung[5] == 1 and tampung[i][6] == 1):
			waktu = "Siang"
		elif (tampung[i][3] == 0 and tampung[i][4] == 0 and tampung[i][5] == 0 and tampung[i][6] == 1 ) or (tampung[i][3] == 1 and tampung[i][4] == 0 and tampung[i][5] == 0 and tampung[i][6] == 0) or (tampung[i][3] == 0 and tampung[i][4] == 1 and tampung[i][5] == 0 and tampung[i][6] == 0) or (tampung[i][3] == 0 and tampung[i][4] == 0 and tampung[5] == 1 and tampung[i][6] == 0):
			waktu = "Sore"
		elif(tampung[i][3] == 0 and tampung[i][4] == 0 and tampung[i][5] == 0 and tampung[i][6] == 0):
			waktu = '-'
		else:
			waktu = "Malam"
		
		if (tampung[i][7] == 1 and tampung[i][8] == 1 and tampung[i][9] == 1 and tampung[i][10] == 1) :
			langit = "Cerah"
		elif (tampung[i][7] == 1 and tampung[i][8] == 1 and tampung[i][9] == 1 and tampung[i][10] == 0 ) or (tampung[i][7] == 1 and tampung[i][8] == 0 and tampung[i][9] == 1 and tampung[i][10] == 1) or (tampung[i][7] == 1 and tampung[i][8] == 1 and tampung[i][9] == 0 and tampung[i][10] == 1) or (tampung[i][7] == 0 and tampung[i][8] == 1 and tampung[i][9] == 1 and tampung[i][10] == 1):
			langit = "Berawan"
		elif (tampung[i][7] == 0 and tampung[i][8] == 0 and tampung[i][9] == 0 and tampung[i][10] == 1 ) or (tampung[i][7] == 1 and tampung[i][8] == 0 and tampung[i][9] == 0 and tampung[i][10] == 0) or (tampung[i][7] == 0 and tampung[i][8] == 1 and tampung[i][9] == 0 and tampung[i][10] == 0) or (tampung[i][7] == 0 and tampung[i][8] == 0 and tampung[i][9] == 1 and tampung[i][10] == 0):
			langit = "Rintik"
		elif(tampung[i][7] == 0 and tampung[i][8] == 0 and tampung[i][9] == 0 and tampung[i][10] == 0) :
			langit = '-'
		else:
			langit = "Hujan"
		
		if (tampung[i][11] == 1 and tampung[i][12] == 1 and tampung[i][13] == 1 ) :
			kelembapan = "Tinggi"
		elif (tampung[i][11] == 1 and tampung[i][12] == 1 and tampung[i][13] == 0) or (tampung[i][11] == 1 and tampung[i][12] == 0 and tampung[i][13] == 1) or (tampung[i][11] == 0 and tampung[i][12] == 1 and tampung[i][13] == 1):
			kelembapan = "Normal"
		elif (tampung[i][11] == 0 and tampung[i][12] == 0 and tampung[i][13] == 0) :
			kelembapan = '-'
		else :
			kelembapan = "Rendah"

		if (tampung[i][14] == 1) :
			kondisi = "Ya"
		else :
			kondisi = "Tidak"
		
		print("Individu ke - ", i)
		print(tampung[i])
	
		hasil.append([suhu, waktu, langit, kelembapan, kondisi])
		print('Decode ke bahasa manusia  = ', hasil[i])
		print('\n')
konversi()

with open ('data.csv', 'r') as readFile :
	reader = csv.reader(readFile)
	lines = list(reader)
	lines = hasil 
with open('data.csv', 'w') as writeFile : 
	writer = csv.writer(writeFile)
	writer.writerows(lines)

#Perhitungan fitness
with open('bismillah.csv') as File :
	angka = 1
	reader = csv.reader(File, delimiter=',', quotechar = ',', quoting =csv.QUOTE_MINIMAL)
	for row in reader :
		angka = 0
		datalatih.append(row)

kata = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	
for i in range (len(datalatih)):
	#atur suhu
	if (datalatih[i][0] == "Tinggi"): 
		kata[i].extend([1,1,1])
	elif (datalatih[i][0] == "Normal"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,0])
		elif t == 1 : 
			 kata[i].extend([1,0,1])
		else :
			 kata[i].extend([0,1,1])
	elif (datalatih[i][0] == "Rendah"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,1])
		else :
			 kata[i].extend([0,1,0])
	else :
			kata[i].extend([0,0,0])
		
	#atur waktu
	if (datalatih[i][1] == "Pagi"): 
		 kata[i].extend([1,1,1,1])
	elif (datalatih[i][1] == "Siang"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,1,0])
		elif t == 1 : 
			 kata[i].extend([1,1,0,1])
		elif t == 2 : 
			 kata[i].extend([1,0,1,1])
		else :
			 kata[i].extend([0,1,1,1])
	elif (datalatih[i][1] == "Sore"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,1,1])
		elif t == 2 : 
			 kata[i].extend([0,1,0,1])
		else :
			 kata[i].extend([1,0,1,0])
	elif (datalatih[i][1] == "Malam"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,0,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,0,1])
		elif t == 2 : 
			 kata[i].extend([0,1,0,0])
		else :
			 kata[i].extend([0,0,1,0])
	else :
		 kata[i].extend([0,0,0,0])
		
	#atur kondisi langit
	if (datalatih[i][2] == "Cerah"): 
		 kata[i].extend([1,1,1,1])
	elif (datalatih[i][2] == "Berawan"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,1,0])
		elif t == 1 : 
			 kata[i].extend([1,1,0,1])
		elif t == 2 : 
			 kata[i].extend([1,0,1,1])
		else :
			 kata[i].extend([0,1,1,1])
	elif (datalatih[i][2] == "Rintik"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,1,1])
		elif t == 2 : 
			 kata[i].extend([0,1,0,1])
		else :
			 kata[i].extend([1,0,1,0])
	elif (datalatih[i][2] == "Hujan"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,0,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,0,1])
		elif t == 2 : 
			 kata[i].extend([0,1,0,0])
		else :
			 kata[i].extend([0,0,1,0])
	else :
		 kata[i].extend([0,0,0,0])
		
	#atur Kelembapan
	if (datalatih[i][3] == "Tinggi"): 
		 kata[i].extend([1,1,1])
	elif (datalatih[i][3] == "Normal"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,1,0])
		elif t == 1 : 
			 kata[i].extend([1,0,1])
		else :
			 kata[i].extend([0,1,1])
	elif (datalatih[i][3] == "Rendah"):
		t = randint(0,2)
		if t == 0 :
			 kata[i].extend([1,0,0])
		elif t == 1 : 
			 kata[i].extend([0,0,1])
		else :
			 kata[i].extend([0,1,0])
	else :
		 kata[i].extend([0,0,0])
		
	#terbang/tidak
	if (datalatih[i][4] == "Ya"): 
		 kata[i].extend([1])
	elif (datalatih[i][4] == "Tidak"):
		 kata[i].extend([0])
	else :
		pass

for i in range (len(datalatih)) :
	print(datalatih[i])
	print(kata[i])
	print('\n')
	
#cara menyamakannya
fitness = 0
listfitness = []

for i in range (gen) :
	for a in range(14) :
		if (tampung[i][a] == kata[i][a]) : 
			fitness = fitness + 1
		else :
			fitness = 0
	print("Nilai Fitness untuk individu ke - ", i+1, "=", fitness/80)
	listfitness.append(fitness/80)
#print("\nList Fitness = [", listfitness, "]")
	
#Pemilihan orang tua
posisiparent1 = 0
posisiparent2 = 0
binerparent1 = []
binerparent2 = []

#mencari nilai dan posisi parent1
parent1 =  max(listfitness)
for i in range (len(listfitness)) :
	if listfitness[i] == parent1 :
		posisiparent1 = i+1
		binerparent1 = kata[posisiparent1-1]
	if tampung[i] == binerparent1:
		binerparent1 = kata[i]
		
#mencari nilai dan posisi parent2
listfitness.remove(parent1)
parent2 = max(listfitness)
for i in range (len(listfitness)) :
	if listfitness[i] == parent2 :
		posisiparent2 = i+1
		binerparent2 = kata[posisiparent2-1]
	if tampung[i] == binerparent2 :
		binerparent2 = kata[i]

print ("\nFitness Parent 1 = ", parent1)
print ("Posisi Parent 1 ada pada list ke - ", posisiparent1)
print ("Biner Parent 1 = ", binerparent1)
print ("\nFitness Parent 2 = ", parent2)
print ("Posisi Parent 2 ada pada list ke - ", posisiparent2)
print ("Biner Parent 2 = ", binerparent2)

#mencari anak dengan crossover
#displit kemudian ditukar

print('\n')
y = randint(0,14)
print('crossover pada indeks ke - ', y,
'(perhitungan dimulai dari 0)')
print('Hasil crossover = ')

listanak1= []
listanak2= []

anak11 = binerparent1[y:]
anak12 = binerparent1[:y]
anak21 = binerparent2[:y]
anak22 = binerparent2[y:]

listanak1 = anak11+anak21
listanak2 = anak12+anak22

print("Anak 1 = ", listanak1)
print("Anak 1 = ", listanak2)
print('\n')

#mutasi
probmutasi = 1/15
#anak1
for i in range (15) :
	import random
	z = random.random()
	if (z>=0) and (z<=probmutasi):
		if (listanak1[i]) == 0 :
			listanak1[i] = 1
		else :
			listanak1[i] = 1
#anak2
import random
peluangmutasi = 1/15
for i in range (15) :
	z = random.random()
	if (z>=0) and (z<=probmutasi):
		if (listanak2[i]) == 0 :
			listanak2[i] = 1
		else :
			listanak2[i] = 1
		
print("Mutasi yang terjadi pada Child 1 = ", listanak1)
print("Mutasi yang terjadi pada Child 2 = ", listanak2)

#regenerasi
x = int(input("\nMasukkan Jumlah Regenerasi = "))
newgen = []
hasil2 = []
def generasi () :
	for i in range (x) :
		for a in range (15):
			newgen = [max(tampung)] + [listanak1] + [listanak2]
			#print("\nGenerasi Baru = ", newgen)
			genbaru1 =  min(newgen)
			q = newgen.remove(genbaru1)
			genbaru2 = min(newgen)
			p = newgen.remove(genbaru2)
	print("\nGenerasi Terbaik = ", newgen)
	
	for i in range (len(newgen)):
		if (newgen[i][0] == 1 and newgen[i][1] == 1 and newgen[i][2] == 1) :
			suhu = "Tinggi"
		elif (newgen[i][0] == 1 and newgen[i][1] == 1 and newgen[i][2] == 0) or (newgen[i][0] == 1 and newgen[i][1] == 0 and newgen[i][2] == 1) or (newgen[i][0] == 0 and newgen[i][1] == 1 and newgen[i][2] == 1):
			suhu = "Normal"
		elif(newgen[i][0] == 0 and newgen[i][1] == 0 and newgen[i][2] == 0):
			suhu = '-'
		else :
			suhu = "Rendah"

		if (newgen[i][3] == 1 and newgen[i][4] == 1 and newgen[i][5] == 1 and newgen[i][6] == 1) :
			waktu = "Pagi"
		elif (newgen[i][3] == 1 and newgen[i][4] == 1 and newgen[i][5] == 1 and newgen[i][6] == 0 ) or (newgen[i][3] == 1 and newgen[i][4] == 0 and newgen[i][5] == 1 and newgen[i][6] == 1) or (newgen[i][3] == 1 and newgen[i][4] == 1 and newgen[i][5] == 0 and newgen[i][6] == 1) or (newgen[i][3] == 0 and newgen[i][4] == 1 and newgen[5] == 1 and newgen[i][6] == 1):
			waktu = "Siang"
		elif (newgen[i][3] == 0 and newgen[i][4] == 0 and newgen[i][5] == 0 and newgen[i][6] == 1 ) or (newgen[i][3] == 1 and newgen[i][4] == 0 and newgen[i][5] == 0 and newgen[i][6] == 0) or (newgen[i][3] == 0 and newgen[i][4] == 1 and newgen[i][5] == 0 and newgen[i][6] == 0) or (newgen[i][3] == 0 and newgen[i][4] == 0 and newgen[5] == 1 and newgen[i][6] == 0):
			waktu = "Sore"
		elif(newgen[i][3] == 0 and newgen[i][4] == 0 and newgen[i][5] == 0 and newgen[i][6] == 0):
			waktu = '-'
		else:
			waktu = "Malam"
		
		if (newgen[i][7] == 1 and newgen[i][8] == 1 and newgen[i][9] == 1 and newgen[i][10] == 1) :
			langit = "Cerah"
		elif (newgen[i][7] == 1 and newgen[i][8] == 1 and newgen[i][9] == 1 and newgen[i][10] == 0 ) or (newgen[i][7] == 1 and newgen[i][8] == 0 and newgen[i][9] == 1 and newgen[i][10] == 1) or (newgen[i][7] == 1 and newgen[i][8] == 1 and newgen[i][9] == 0 and newgen[i][10] == 1) or (newgen[i][7] == 0 and newgen[i][8] == 1 and newgen[i][9] == 1 and newgen[i][10] == 1):
			langit = "Berawan"
		elif (newgen[i][7] == 0 and newgen[i][8] == 0 and newgen[i][9] == 0 and newgen[i][10] == 1 ) or (newgen[i][7] == 1 and newgen[i][8] == 0 and newgen[i][9] == 0 and newgen[i][10] == 0) or (newgen[i][7] == 0 and newgen[i][8] == 1 and newgen[i][9] == 0 and newgen[i][10] == 0) or (newgen[i][7] == 0 and newgen[i][8] == 0 and newgen[i][9] == 1 and newgen[i][10] == 0):
			langit = "Rintik"
		elif(newgen[i][7] == 0 and newgen[i][8] == 0 and newgen[i][9] == 0 and newgen[i][10] == 0) :
			langit = '-'
		else:
			langit = "Hujan"
		
		if (newgen[i][11] == 1 and newgen[i][12] == 1 and newgen[i][13] == 1 ) :
			kelembapan = "Tinggi"
		elif (newgen[i][11] == 1 and newgen[i][12] == 1 and newgen[i][13] == 0) or (newgen[i][11] == 1 and newgen[i][12] == 0 and newgen[i][13] == 1) or (newgen[i][11] == 0 and newgen[i][12] == 1 and newgen[i][13] == 1):
			kelembapan = "Normal"
		elif (newgen[i][11] == 0 and newgen[i][12] == 0 and newgen[i][13] == 0) :
			kelembapan = '-'
		else :
			kelembapan = "Rendah"

		if (newgen[i][14] == 1) :
			kondisi = "Ya"
		else :
			kondisi = "Tidak"
		hasil2.append([suhu, waktu, langit, kelembapan, kondisi])
		print('Decode ke bahasa manusia  = ', hasil2[i])
generasi()

#isi data uji
datauji = []
with open('datauji.csv') as File :
	angka = 1
	reader = csv.reader(File, delimiter=',', quotechar = ',', quoting =csv.QUOTE_MINIMAL)
	for row in reader :
		angka = 0
		datauji.append(row)
	print("\n")
	#print(datauji)
	
print("========== DECODE DATA UJI ==============")	
word = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	
for i in range (len(datauji)):
	#atur suhu
	if (datauji[i][0] == "Tinggi"): 
		word[i].extend([1,1,1])
	elif (datauji[i][0] == "Normal"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,0])
		elif t == 1 : 
			 word[i].extend([1,0,1])
		else :
			 word[i].extend([0,1,1])
	elif (datauji[i][0] == "Rendah"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,1])
		else :
			 word[i].extend([0,1,0])
	else :
			word[i].extend([0,0,0])
		
	#atur waktu
	if (datauji[i][1] == "Pagi"): 
		 word[i].extend([1,1,1,1])
	elif (datauji[i][1] == "Siang"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,1,0])
		elif t == 1 : 
			 word[i].extend([1,1,0,1])
		elif t == 2 : 
			 word[i].extend([1,0,1,1])
		else :
			 word[i].extend([0,1,1,1])
	elif (datauji[i][1] == "Sore"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,1,1])
		elif t == 2 : 
			 word[i].extend([0,1,0,1])
		else :
			 word[i].extend([1,0,1,0])
	elif (datauji[i][1] == "Malam"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,0,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,0,1])
		elif t == 2 : 
			 word[i].extend([0,1,0,0])
		else :
			 word[i].extend([0,0,1,0])
	else :
		 word[i].extend([0,0,0,0])
		
	#atur kondisi langit
	if (datauji[i][2] == "Cerah"): 
		 word[i].extend([1,1,1,1])
	elif (datauji[i][2] == "Berawan"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,1,0])
		elif t == 1 : 
			 word[i].extend([1,1,0,1])
		elif t == 2 : 
			 word[i].extend([1,0,1,1])
		else :
			 word[i].extend([0,1,1,1])
	elif (datauji[i][2] == "Rintik"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,1,1])
		elif t == 2 : 
			 word[i].extend([0,1,0,1])
		else :
			 word[i].extend([1,0,1,0])
	elif (datauji[i][2] == "Hujan"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,0,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,0,1])
		elif t == 2 : 
			 word[i].extend([0,1,0,0])
		else :
			 word[i].extend([0,0,1,0])
	else :
		 word[i].extend([0,0,0,0])
		
	#atur Kelembapan
	if (datauji[i][3] == "Tinggi"): 
		 word[i].extend([1,1,1])
	elif (datauji[i][3] == "Normal"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,1,0])
		elif t == 1 : 
			 word[i].extend([1,0,1])
		else :
			 word[i].extend([0,1,1])
	elif (datauji[i][3] == "Rendah"):
		t = randint(0,2)
		if t == 0 :
			 word[i].extend([1,0,0])
		elif t == 1 : 
			 word[i].extend([0,0,1])
		else :
			 word[i].extend([0,1,0])
	else :
		 word[i].extend([0,0,0])

for i in range (len(datauji)) :
	print(datauji[i])
	print(word[i])

#menyamakan data uji
print("\n====== HASIL MENGECEKAN DATA UJI =======")
m = 0
n = 0
o = 0
for i in range (len(datauji)) :
		if (datauji[i][n] == hasil2[0][n] or hasil2[0][n] == '-') :
			o = datauji[i].append('Ya')
		else :
			o = datauji[i].append('Tidak')
			
print("\n")
for i in range (len(datauji)):
	print(datauji[i])

#write csv
out = csv.writer(open("datafinal.csv", "w"), delimiter = "\n", quoting=csv.QUOTE_ALL)
out.writerow(datauji)