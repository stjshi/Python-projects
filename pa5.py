

#take in 3 inputs (A, B, C)
a = input("DNA Sequence A:")
b = input("DNA Sequence B:")
c = input("DNA Sequence C:")
if len(a) != len(b) or len(a) != len(c):
	print("DNA sequences do not have the same length!") 
	exit()
#if sequences contain characters other than a, c, g, and t
	#print("DNA sequences contain invalid characters!")
	#exit()

distanceAB  = 0
distanceAC = 0
distanceBC = 0

for i in range(len(a)): 
	if a[i] == b[i]:
		distanceAB  += 0
	elif a[i] != b[i]:
		distanceAB += 1

for i in range(len(a)):
	if a[i] == c[i]:
		distanceAC  += 0
	elif a[i] != c[i]:
		distanceAC += 1

for i in range(len(b)):
	if b[i] == c[i]:
		distanceBC  += 0
	elif b[i] != c[i]:
		distanceBC += 1
#print(distanceAB)
#print(distanceAC)
#print(distanceBC)

if distanceAB < distanceAC <= distanceBC:
	print("Species A and B have the most recent common ancestor.")
elif distanceAC < distanceAB <= distanceBC:
	print("Species A and C have the most recent common ancestor.")
elif distanceBC < distanceAB and distanceAB<= distanceAC:
	print("Species B and C have the most recent common ancestor.")
elif distanceAB == distanceAC == distanceBC:
	print("Species A and B have the most recent common ancestor.")
