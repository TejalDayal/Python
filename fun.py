def fun(a,b,c):
  if c=='+':
    print(a+b)
  if c=='-':
    print(a-b)
  if c=='*':
    print(a*b)
  if c=='/':
    print(a/b)
a=int(input('Enter First No:'))
b=int(input('Enter Second No:'))
c=str(input('Enter Operation:'))
fun(a,b,c)
