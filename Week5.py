# Enter the statement to import the math module.
#Calculate the volume of the sphere with radius 10, ( V =4/3piR) 
#Display its value.

from math import pi as PI
Radius = 10
Volume = 4/3*PI*Radius* Radius **2 
print(Volume)
4188.7901999999995
#Exercise2
# //Enter the following statements:
# //from math import pi as PI
# //radius = 10
# //Run the program from within IDLE by choosing the Run > Run Module option.
# //In the interactive shell, display the values of PI and radius.
# //Enter an expression to calculate the area of the circle. and display its value.
# from math import pi as PI

Radius= 10
print(Radius)
10
print(PI)
3.141592653589793
print(Radius)
10
Area = PI*Radius**2
print(Area)
314.1592653589793
#Exercise3
#You run 10 kilometers in 40 minutes 30 seconds. Write program to find out how many miles you can run in an hour. A mile is 1.61 kilometers and display its value.
x=10
distance =x/1.61
print(distance)
minuite =40
second = 30
time=(minuite/60)+ (second/3600)
print(time)
speed=distance/time
print(speed)
#secod idea 
distance_in_miles = 10/1.61
time_taken = 40.5/60
# in hours
speed = distance_in_miles /time_taken
print(speed)

