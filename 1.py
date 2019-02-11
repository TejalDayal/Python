#program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

n=1500
print("Numbers divisible by 7 and multiples of 5 are:")
while(n<=2700):
  if(n%7==0 and n%5==0):
    print(n,"\t")
  n=n+1
