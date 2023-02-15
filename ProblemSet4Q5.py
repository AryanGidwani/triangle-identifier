# Aryan Gidwani
# November 12, 2021
# ICS3UO - A
# The purpose of this program is to check whether a triangle is either
# equilateral, isosceles, or scalene using the user-inputted side lengths.

name = input("Hello! What is your name? ")
# asks the user for their name

print("Hello " + name + "! With this program, you will input lengths for the three different " + "\n" + "sides of the triangle, and we will tell you if it is equilateral, isosceles, or " + "\n" + "scalene! All measurements will automatically be in centimetres, and if any negative value is inputted, the number will be changed into it's positive version. For instance, -2 will become 2.")
# introductory message
flag = True
# a flag variable which stores the value of true

while flag:
    try:
        firstSide = abs(float(input("Enter in the length of the first side of the triangle: ")))
        # asks for the length of the side and makes sure its positive
        secondSide = abs(float(input("Enter in the length of the second side of the triangle: ")))
        # asks for the length of the side and makes sure its positive
        thirdSide = abs(float(input("Enter in the length of the third side of the triangle: ")))
        # asks for the length of the side and makes sure its positive

        if (firstSide == secondSide == thirdSide):
            print("The triangle is equilateral! " + "\n")
            # prints that it is equilateral if all sides are equal

        elif (firstSide == secondSide) or (firstSide == thirdSide) or (secondSide == thirdSide):
            print("The triangle is isosceles! " + "\n")
            # prints that it is isosceles if two of the sides are equal

        else:
            print("The triangle is scalene! " + "\n")
            # informs the user that the triangle is scalene, as none of the sides
            # are equal
    except :
        print("Enter in a valid value please!" + "\n")
        # if the user inputs an invalid value, the program tells the user
