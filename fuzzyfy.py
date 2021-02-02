# Name: Kevin G. Fuentes
# ID No.: 2015-2066

# Problem: Given a fuzzy set, fuzzify a crisp value input.
#
# Membership function: Trapezoidal fuzzy type
#
# Program Description:
#   The following points in the trapezoid are set by default, so the user will
#   have to input only the crisp value. The equation I applied is the two-points
#   slope equation to be able to get the values on the sides of the trapezoid.
#   Below are the following points (fuzzy sets) I set by default.
#
# Points (Fuzzy sets) in the trapezoid:
#   A(15,0)
#   B(22,1)
#   C(30,1)
#   D(42,0)
#
# This are based on the air-conditioner temperature problem.

# Function named mTrapezoidal with parameter crispValue:
def mTrapezoidal(crispValue):

# Points on the x-axis.
    xA = 15  #x1
    xB = 22  #x2
    xC = 30  #x3
    xD = 42  #x4

# IF-ELSEIF-ELSE condition.
    if crispValue <= xA:
        return 0.0
    elif xA < crispValue and crispValue <= xB:
        return float(crispValue - xA)/float(xB - xA)
    elif xB < crispValue and crispValue <= xC:
        return 1.0
    elif xC < crispValue and crispValue <= xD:
        return float(xD - crispValue)/float(xD - xC)
    else:
        return 0.0

# User-Input asking for the temperature.
nTemp = int(input("\nPlease input the temperature: "))
# Displaying the crisp value with its fuzzy value.
print("\nResult:\tThe crisp value of " + str(nTemp) + " with a fuzzy value of " + str(mTrapezoidal(nTemp)))
