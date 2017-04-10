#Stephanie Shi (stjshi@ucsc.edu)
#Pair programming with: Christian Lam (ctlam@ucsc.edu)
#Pa 6

import math

userin = input("Enter Exam Scores: ")
convertedin = userin.split(',')
print(convertedin)
total = 0
totalIn = 0

for i in convertedin:
	i = int(i)
	total += i


mean = total/len(convertedin)

for i in convertedin:
	i = int(i)
	totalIn += ((i-mean)**2)

insideShit = totalIn/len(convertedin)
standard = math.sqrt(insideShit)
print("Mean: " + str(mean) + " StdDev: " + str(standard))
grades = ['']*len(convertedin)

for i in range(len(convertedin)):
	
	if int(convertedin[i]) > (mean+(1.5*standard)):
		grades[i] = "A"
	elif int(convertedin[i]) > (mean+(0.5*standard)):
		grades[i] = "B"
	elif int(convertedin[i]) > (mean-(0.5*standard)):
		grades[i] = "C"
	elif int(convertedin[i]) > (mean-(1.5*standard)):
		grades[i] = "D"
	elif int(convertedin[i])< (mean-(1.5*standard)):
		grades[i] ="F"
			
print("Grades: " + ", ".join(grades))	
