

input1 = input("Enter the initial deposit:")
input2 = input("Enter the annual interest rate in %:")
#input3 = input("How much money do you want to deposit or withdraw?")
intDeposit = float(input1)
intInterest = float(input2)
intInterest = intInterest/100
availBalance = intDeposit 

for (i) in range(12):
	input3 = input("How much money do you want to deposit or withdraw?")
	intModify = int(input3)
	if intDeposit + intModify < 0:
		intModify = 0
		print("The amount exceeds your balance!")
		#print("Your new balance at the end of the month " + str(i+1) + " is " + str(intModify))

	#if intModify > availBalance:
	#availBalance = intModify + availBalance
	intDeposit = intDeposit * (1 + (intInterest/12)) + intModify
	print("Your new balance at the end of the month " + str(i+1) + " is " + str(intDeposit))
	#elif intModify < 0:	

