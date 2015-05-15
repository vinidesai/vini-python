#!/usr/bin/python

#Calculator
#addition function
def add(num1, num2):
	return(num1 + num2)

#Subtration Function
def sub(num1, num2):
	return(num1 - num2)

#Multiplication Function
def mul(num1, num2):
	return(num1 * num2)

#Divison Function
def div(num1, num2):
	return(num1 / num2)

#exponential Function
def exp(num1, num2):
	power = num2
	mid_value = 1;

	if(power == 0):
	    return mid_value;

	while(power):
	    mid_value = mid_value * num1
	    power = power-1

	return mid_value

def main():
	print("Welcome,")
	operation = input("For operation press '+(add)','-(subtraction)','*(multiplication','/(divison)','^(exponential)'")
	if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '^'):
		print ("operation is wrong")
	else:
		num1 = int(input ("Enter first number:"))
		num2 = int(input ("Enter second number:"))

		if(operation == '+'):
			#dummy = add(num1, num2)
			print ("Answer is ", add(num1, num2))
		elif(operation == '-'):
			print("Answer is ", sub(num1, num2))
		elif(operation == '*'):
			print("Answer is ", mul(num1, num2))
		elif(operation == '/'):
			print("Answer is ", div(num1, num2))
		elif(operation == '^'):
			print("Answer is ",exp(num1, num2))

main()
