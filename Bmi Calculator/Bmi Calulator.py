
# Purpose:    BMI
#BMI = ( kilograms / meters^2)
#n = bmi formula

a = int(input("input weight in pounds:"))
x = int(input("input height in feet: "))
y = int(input("input height in inches: "))

h = (((x * 12)+y))
BMI = ((a*.4536)/((h*.0254)**2))

print (BMI)
     
