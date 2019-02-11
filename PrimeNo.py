n=int(input("Enter The No: "))
i=2
if (n==0 or n==1):
    print(n," is not prime number.")
else:
    while i<n:
        if(n%i==0):
            print(n," is not prime number.")      
            break
        else:
            print(n," is prime number.")
        i+=1