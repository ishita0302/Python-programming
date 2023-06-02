import sys
print(sys.argv)
sum = 0
print(len(sys.argv))
for num in range(1,len(sys.argv)):
    sum = sum + int(sys.argv[num])
print("sum: ", sum)
