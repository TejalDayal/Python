#program to convert temperatures to and from celsius, fahrenheit. Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
b=int(input("Enter the temperature format: 1.Degree: 2.Fahrenheit:"))
a=float(input("Enter the temperature:"))
if (b==1):
  d=((a*1.8)+32)
  print(a,"Degree Celsius is" ,d, "Fahrenheit")
if (b==2):
  d=((5/9)*(a-32))
  print(a,"Fahrenheit is" ,d, "Degree Celsius")
