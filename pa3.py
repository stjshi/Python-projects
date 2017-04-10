# Stephanie Shi
# stjshi@ucsc.edu
# CMPS5P PA3

input1 = input("What is your input1 in pounds?")
input1new = int(input1)
kilograms = (input1new * 0.45)	#conversion given by professor
input2 = input("What is your input2 in inches?")
input2new = int(input2)
meters = input2new/39.37	#conversion given by professor
bodyMassInd = kilograms/(meters ** 2)
if bodyMassInd < 18:
	print("Your bodyMassInd is " + str(bodyMassInd) + ". You are underinput1.")
	print("Eat some more food.")
elif bodyMassInd > 30:
	print("Your bodyMassInd is " + str(bodyMassInd) + ". You are overinput1.")
	print("Eat healthier.")
else:
	print("Your bodyMassInd is " + str(bodyMassInd) + ". You have a normal input1.")
	print("Stay healthy!")