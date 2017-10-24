

 #print error message and quit the program if number> 999999999

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
thousands = ["one thousand", "two thousand", "three thousand", "four thousand", "five thousand", "six thousand", "seven thousand", "eight thousand", "nine thousand"]
def sayDigit(input1):
	if(input1 ==0):
		return "zero"
	else:
		return ones[input1-1]

def sayTeen(input1): 
	
	if input1 < 10:
		return sayDigit(input1)
	elif input1 == 10:
		return("ten")
	elif input1 > 10:
		return teens[input1-11]
def sayTens(input1):
	
	if input1 < 20:
		return sayTeen(input1)
	elif input1 < 100:
		d = input1//10
		e = input1%10
		if e ==0:
			return tens[d-2]
		else:
			return (tens[d-2] + " " + ones[e-1])
def sayHundreds(input1):
	if input1 < 100:
		return sayTens(input1)
	elif 99<input1 < 1000:
		a = input1//100
		b = input1%100
		if b == 00:
			return hundreds[a-1]
		else:
			prev = sayTens(b)
			return (hundreds[a-1] + " " + prev)
def sayThousands(input1):
	if input1 < 1000:
		return sayHundreds(input1)
	elif input1 < 10000:
		a = input1//1000
		b = input1%1000
		if b == 000:
			return thousands[a-1]
		else: 
			prev = sayHundreds(b)
			return (thousands[a-1] + " " +prev)
def sayTenThousands(input1):
	if input1 < 10000:
		return sayThousands(input1)
	elif 9999<input1 < 100000:
		a = input1//10000
		b = input1%10000
		c = input1//1000
		e = input1%1000
		if b == 0 and c > 20:
			calling = sayTens(c)
			return (calling + " thousand")
		elif 9< c < 20:
			calling = sayTeen(c)
			prev = sayHundreds(e)
			return (calling + " thousand " + prev)
		else:
			calling = sayTens(c)
			return (calling + " thousand " + sayHundreds(e))
def sayHundredThousands(input1):
	if input1 < 100000:
		return sayTenThousands(input1)
	elif 99999 < input1 < 1000000:
		a = input1//100000
		b = input1%100000
		c = input1//1000
		e = input1%1000
		if b == 0 :
			calling = sayHundreds(c)
			return (calling + " thousand")	
		else:
			calling = sayHundreds(c)
			return (calling + " thousand " + sayHundreds(e))
def sayMillion(input1):
	if input1 < 1000000:
		return sayHundredThousands(input1)
	elif 999999 < input1 < 10000000:
		a = input1//1000000
		b = input1%1000000
		c = input1//10000
		e = input1%1000000
		if b == 0:
			calling = sayDigit(a)
			return (calling + " million")
		else:
			calling = sayDigit(a)
			return(calling + " million " + sayHundredThousands(e))
def sayTenMillion(input1):
	if input1 < 10000000:
		return sayMillion(input1)
	elif 9999999 < input1 < 100000000:
		a = input1//10000000
		b = input1%10000000
		c = input1//1000000
		e = input1%1000000
		if b == 0 and c > 20:
			calling = sayTens(c)
			return (calling + " million")
		elif 9< c < 20:
			calling = sayTeen(c)
			prev = sayHundredThousands(e)
			return (calling + " million " + prev)
		else:
			calling = sayTens(c)
			return (calling + " million " + sayHundredThousands(e))
def sayHundredMillion(input1):
	if input1 < 100000000:
		return sayTenMillion(input1)
	elif 99999999 < input1 < 1000000000:
		a = input1//10000000
		b = input1%10000000
		c = input1//1000000
		e = input1%1000000
		if b == 0 :
			calling = sayHundreds(c)
			return (calling + " million")	
		else:
			calling = sayHundreds(c)
			return (calling + " million " + sayHundredThousands(e))


n = int(input())
if n > 999999999:
	print("Number exceeds limit")
	exit(0)
	
print(sayHundredMillion(n))

