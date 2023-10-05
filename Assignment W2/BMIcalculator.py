
#Hans Matere SCT 211-0080/2022

import math

bodyWeight = int(input("Please put ur body weight in kgs: "))
bodyHeight = float(input("Please put ur body height in metres: "))

BMI = float(bodyWeight / (math.pow(bodyHeight,2)))

if BMI < 18.5:
    print("Underweight")

elif 18.5 <= BMI < 24.9:
    print ("Normal weight")

else:
    print("Overweight")


