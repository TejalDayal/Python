#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and 
#write a program that prints out all the elements of the list that are less than N(User input number).
#Extras:Instead of printing the elements one by one, make a new list that has all the elements less than N
#(User input number) from this list in it and print out this new list.

a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n=int(input("Enter the No.: "))
b=[]
for i in range (len(a)):
    if(a[i]<n):
        b.append(a[i])
print(b)