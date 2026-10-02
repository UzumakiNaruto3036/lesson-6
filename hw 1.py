a=int(input("enter the weather in degrees celsius: "))
if a<=0:
    print("freezing weather,wear heavy woolen clothes")
elif a>=1 and a<=15:
    print("cold weather,wear a jacket")
elif a>=15 and a<=30:
    print("moderate weather,wear a sweater,jacket or a hoodie")
elif a>=30 and a<=40:
    print("warm weather,wear light clothing")
else:
    print("hot weather,wear very light clothing and stay hydrated and if possible stay indoors")