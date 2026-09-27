height=int(input("enter your height in cm: "))
weight=float(input("enter your weight in kg: "))
BMI=weight/(height/100)**2
print("your BMI is: ",BMI)
if BMI<=18.4:
    print("you are underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("you are healthy")
elif BMI>=25 and BMI<=29.9:
    print("you are overweight")
elif BMI>=30 and BMI<=34.9:
    print("you are severely overweight")
else:
    print("you are obese")
