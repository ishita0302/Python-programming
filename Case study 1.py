#Given a string containing both upper and lower case letters. Write a Python program to count the number of repeated characters and display the maximum count of a character along with the character.
String="ABaBCbGc"
counts = {}
String1=String.upper()
for i in String1:
    counts[i] = String1.count(i)

for k in counts.keys():
    print(str(counts[k]) + k)
