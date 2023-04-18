l = int(input("enter lower range: "))
h = int(input("enter upper range: "))
for i in range(l, h+1):
 c=0
 for j in range(2, (i//2)+1):
 if i % j ==0:
 c+=1
 if c == 0:
 print(f"{i}")
