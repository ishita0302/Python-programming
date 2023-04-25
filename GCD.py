a = int(input("enter first no: "))
b = int(input("enter second no: "))
while(a%b!=0):
    s = a%b
    a=b
    b=s
print(b)
