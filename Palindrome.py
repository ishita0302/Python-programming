a = int(input("enter a number: "))
b = a
c = 0
while(a>0):
    s=a%10
    c=c*10 + s
    a=a//10
if c==b:
    print("it is palindrome")
else:
    print("it is not a palindrome")
