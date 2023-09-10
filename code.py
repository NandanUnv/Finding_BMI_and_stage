#calculation of Bmi and finding categories

wei = float(input("weight: "))
hei = float(input("height in cms:"))

BMI = wei / hei**2
BMI *=10000
BMI = round(BMI,1)
if BMI <=18.5:
    print(f'your BMI is: {BMI}, your are Underweight')
elif BMI>18.5 and BMI<=24.9:
    print(f'your BMI is: {BMI}, your are Normal weight')
elif BMI>25 and BMI<=29.9:
    print(f'your BMI is: {BMI}, your are Overweight')
else:
    print(f'your BMI is: {BMI}, your have Obesity')
