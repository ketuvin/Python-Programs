# Name: Kevin G. Fuentes
# ID No.: 2015-2066 (TH-08)
#
# Problem: Backward Chaining
#
# Variable Values:
#   A = Has atleast Php 10,000
#   B = Younger than 30
#   C = Education at college level
#   D = Annual income of at least Php 40,000
#   E = Invest in securities
#   F = Invest in growth stocks
#   G = Invest in IBM stocks


print("\n*****************************************************************")
print("*\t\t\t\t\t\t\t\t*")
print("*PERSONAL INVESTMENT ADVISER USING BACKWARD CHAINING INFERENCING*")
print("* \t\t\tVersion 1.0\t\t\t\t*")
print("*\t\t\t\t\t\t\t\t*")
print("*****************************************************************")

name = input("\nPlease enter your name: ")

print("\n\nSimplified Knowledge Base rules:")
print("  R1: IF A AND C, THEN E")
print("  R2: IF D AND C, THEN F")
print("  R3: IF B AND E, THEN F")
print("  R4: IF B, THEN C")
print("  R5: IF F, THEN G")

#Pre-defined Variables
A = 10000
B = 30
C = "Degree"
D = 40000
E = "Invest in securities"
F = "Invest in growth stocks"
G = "Invest in IBM stocks"

goalPrinter = ""

#Default Boolean Values of Pre-defined Variables
Avalue = False
Bvalue = False
Cvalue = False
Dvalue = False
Evalue = False
Fvalue = False
Gvalue = False
findGoal1 = False
findGoal2 = False
achieved = False


#Rule-Fired placeholder
R1fired1 = False
R2fired1 = False
R3fired1 = False
R4fired1 = False
R5fired1 = False


print("\nPre-defined variables:")
print("  A. Has atleast Php 10,000")
print("  B. Younger than 30")
print("  C. Education at college level")
print("  D. Annual income of atleast Php 40,000")
print("\nAvailable Goals:")
print("  E. Invest in securities")
print("  F. Invest in growth stocks")
print("  G. Invest in IBM stocks")

#Function for Rules using Backtracking logic
def R1(var1, var2, g, visit, achieve):
        global goal
        if g == "E" and visit == False:
                print("\n[R1] You can invest in securities if you have atleast Php 10,000 and Education at college level or greater")
                global R1fired1
                global findGoal1
                if var1 == True and var2 == True:
                        print("\n[R1] Good news! You can invest in securities!")
                        findGoal1 = True
                        goal = main
                        R1fired1 = True
                elif var1 == True:
                        print("\n[R1] You have atleast Php 10,000! But what's your education level?")
                        goal = "C"
                        if goalVerifier(goal):
                                print("\n[R1] Your education is college level or greater if you are younger than 30.")
                                R1fired1 = True
                        else:
                                print("\n[R1] Sorry, your goal is unachievable")
                                goal = "E"
                                R1fired1 = True
                else:
                        print("\n[R1] Your education is at college level or greater! But do you have atleast Php 10,000?")
                        goal = "A"
                        if goalVerifier(goal):
                                print("\nYou might have atleast Php 10,000! R1")
                                R1fired1 = True

def R2(var1, var2, g, visit, achieve):
        global goal
        if g == "F" and visit == False:
                print("\n[R2] You can invest in growth stocks if your annual income is atleast Php 40,000 and Eduaction at college level or greater")
                global R2fired1
                global findGoal1
                if var1 == True and var2 == True:
                        print("\n[R2] Good news! You can invest in growth stocks!")
                        findGoal1 = True
                        goal = main
                        R2fired1 = True
                elif var1 == True:
                        print("\n[R2] You have an annual income of atleast Php 40,000! But what's your education level?")
                        goal = "C"
                        if goalVerifier(goal):
                                print("\n[R2] Your education might be in college level or greater if you're younger than 30")
                                R2fired1 = True
                else:
                        print("\n[R2] Your education is in college level or greater! But what's your annual income?")
                        goal = "D"
                        isExist = goalVerifier(goal)
                        if isExist == True:
                                print("\n[R2] You can have an annual income of atleast Php 40,000")
                                R2fired1 = True
                        else:
                                print("\n[R2] Sorry you don't have an annual income of atleast Php 40,000")
                                goal = "F"
                                R2fired1 = True

def R3(var1, var2, g, visit, achieve):
        global goal
        if g == "F" and visit == False:
                print("\n[R3] You can invest in growth stocks if you're younger than 30 and you have an investment in securities")
                global R3fired1
                global findGoal1
                if var1 == True and var2 == True:
                        print("\n[R3] Good news! You can invest in growth stocks!")
                        findGoal1 = True
                        goal = main
                        R3fired1 = True
                elif var1 == True:
                        print("\n[R3] You're younger than 30! But have you invested in securities?")
                        goal = "E"
                        if goalVerifier(goal):
                                print("\n[R3] You can invest in securities if you have atleast Php 10,000 and Education at college level or greater")
                                R3fired1 = True
                        else:
                                print("\n[R3] Sorry goal is unachievable")
                                goal = "F"
                                R3fired1 = True
                else:
                        print("\n[R3] You have invested in securites!")
                        goal = "B"
                        if goalVerifier(goal):
                                print("\n[R3] You might be younger than 30!")
                                R3fired1 = True
                        else:
                                print("\n[R3] Sorry goal is unachievable")
                                goal = "F"
                                R3fired1 = True

def R4(var, g, visit, achieve):
        global goal
        if g == "C" and visit == False:
                if var == True:
                        print("\n[R4] Your education is at college level or greater!")
                        global R4fired1
                        global findGoal1
                        findGoal1 = True
                        R4fired1 = True
                        goal = main
                else:
                        goal = "B"
                        if goalVerifier(goal):
                                print("\n[R4] Your education is at college level if you're younger than 30")
                                R4fired1 = True
                        else:
                                print("\n[R4] Sorry goal is unachievable")
                                R4fired1 = True

def R5(var, g, visit, achieve):
        global goal
        if g == "G" and visit == False:
                if var == True:
                        print("\n[R5] Good news! You can invest in IBM stocks!")
                        global findGoal1
                        global R5fired1
                        R5fired1 = True
                        findGoal1 = True
                        goal = main
                else:
                        goal = "F"
                        isExist = goalVerifier(goal)
                        if isExist == True:
                                print("\n[R5] You can invest in IBM stocks if you have invested in growth stocks")
                                R5fired1 = True
                        else:
                                print("\n[R5] Sorry goal is unachievable")
                                R5fired1 = True

def goalVerifier(g):
        if g == "E":
                return True
        elif g == "F":
                return True
        elif g == "C":
                return True
        elif g == "G":
                return True
        else:
                return False

while True:
        num = int(input("\nHow many facts would you want? [Range: 1 - 4]\nAnswer: "))
        if num <= 4:
                if num > -1:
                        mylist = []
                        print("Choose", num, "from Pre-defined variables: ")
                        for i in range(num):
                                choice = input()
                                mylist.insert(i, choice)

                        goalE = input("Do you want to invest in securities?[yes/no]: ").lower().strip()
                        if goalE == "no":
                                goalF = input("Do you want to invest in growth stocks?[yes/no]: ").lower().strip()
                                if goalF == "no":
                                        goalG = input("Do you want to invest in IBM stocks?[yes/no]: ").lower().strip()
                        if goalE == "yes":
                                goalF = "no"
                                goalG = "no"
                                goal = "E"
                        elif goalF == "yes":
                                goalG = "no"
                                goal = "F"
                        else:
                                goal = "G"
                                
                        main = goal
                        
                        print("\nPlease wait while backward chaining is being applied: ")
                        for i in range(len(mylist)):
                                if mylist[i] == "A":
                                        Avalue = True
                                elif mylist[i] == "B":
                                        Bvalue = True
                                elif mylist[i] == "C":
                                        Cvalue = True
                                else:
                                        Dvalue = True

                        if goal == "E":
                                Evalue = True
                                goalPrinter = E
                        elif goal == "F":
                                Fvalue = True
                                goalPrinter = F
                        else:
                                Gvalue = True
                                goalPrinter = G
                        
                        for i in range(500):
                                print("Analyzing data...")
                        print("Analysis Complete!")
                        print("\n\nThe current information available for Mr/Ms.",name)
                        print("  Want to invest in securities: ",goalE)
                        print("  Want to invest in growth stocks: ",goalF)
                        print("  Want to invest in IBM stocks: ",goalG)
                        print("\nResult:")
                        while findGoal1 != True:
                                R1(Avalue, Cvalue, goal, R1fired1, achieved)
                                R2(Dvalue, Cvalue, goal, R2fired1, achieved)
                                R3(Bvalue, Evalue, goal, R3fired1, achieved)
                                R4(Bvalue, goal, R4fired1, achieved)
                                R5(Fvalue, goal, R5fired1, achieved)

                        print("\nSir/Madam",name,", Congratulations! you can",goalPrinter,"!")

                else:
                        print("\nThe value you entered is negative! Please try again!")
                break;
        else:
                print("\nThe value you entered is higher than 5! Please try again!")

