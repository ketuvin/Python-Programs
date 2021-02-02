# Name: Kevin G. Fuentes
# ID No.: 2015-2066

# Problem: Defuzzification process.
#
# Membership function: Trapezoidal fuzzy type
# Method used in Defuzzification: Center of Sums
#
# Two Fuzzy Sets F1 and F2 are defined below:
#	F1:
#	P1 (11,0)
#	P2 (13,User-Input)
#	P3 (17,User-Input)
#	P4 (18,0)
#
#	F2:
#	P1 (13,0)
#	P2 (14,[User-Input])
#	P3 (18,[User-Input])
#	P4 (19,0)


#Defuzzification code
while True:
	firstTrapezoidal_height = float(input("\nPlease enter F1's Trapezoidal Height [0 - 1 only]:"))
	secondTrapezoidal_height = float(input("Please enter F2's Trapezoidal Height [0 - 1 only]:"))

	#The Variabes
	f1_xA = 11
	f1_yA = 0
	f1_xB = 13
	f1_yB = firstTrapezoidal_height
	f1_xC = 17
	f1_yC = firstTrapezoidal_height
	f1_xD = 18
	f1_yD = 0

	f2_xA = 13
	f2_yA = 0
	f2_xB = 14
	f2_yB = secondTrapezoidal_height
	f2_xC = 18
	f2_yC = secondTrapezoidal_height
	f2_xD = 19
	f2_yD = 0

	if firstTrapezoidal_height <= 1 and secondTrapezoidal_height <= 1:
		if firstTrapezoidal_height > -1 and secondTrapezoidal_height > -1:
			#Computation of the Area of each fuzzy sets:
			Area1 = (1/2) * ((f1_xD - (f2_xD - f1_xD)) + (f1_xC - (f1_xC - f2_xB))) * firstTrapezoidal_height
			Area2 = (1/2) * ((f2_xD - (f2_xD - (f1_xC - 1))) + (f2_xC - (f1_xD - f2_xB))) * secondTrapezoidal_height

			#Computation of the center of the area of each fuzzy sets:
			x1Bar = (f1_xC + (f2_xD - (f1_xC - 1)))/2
			x2Bar = (f2_xC + (f1_xD - f2_xB))/2

			#Computation for the defuzzified value:
			xAsterisk = (Area1 * x1Bar + Area2 * x2Bar)/(Area1 + Area2)
		else:
			print("\nError, the fuzzy value you entered is negative! Please try again!")
		break;
	else:
		print("\nError, the fuzzy value you entered is greater than 1! Please try again!")

#Printing the Output
print("\nThe Area of fuzzy set F1: ", Area1)
print("The Area of fuzzy set F2: ", Area2)

print("\nThe Center of Area for fuzzy set F1: ", x1Bar)
print("The Center of Area for fuzzy set F2: ", x2Bar)

print("\nDefuzzified Value: ", xAsterisk)
