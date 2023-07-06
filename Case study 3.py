'''	Write a Python program to accept a string and display the resultant string in reverse order . 
The resultant string should contain all characters at the even position of accepted string ignoring blank spaces.
Accepted string: Anappleadaykeepsthedoctoraway
Resultant string: Aapedyepteotrwy
Expected_output: ywrtoetpeydepaA'''
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Aapedyepteotrwy"

print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))
