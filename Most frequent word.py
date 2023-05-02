f = open("text.txt",'w')
f.write("Python provides inbuilt functions for creating, writing, and reading files. Two types of files can be handled in python, normal text files, and binary files (written in binary language,0s and 1s).")
f = open("text.txt",'r')
wr = ""
fr = 0
words = []
for line in f:
	line_word = line.lower().replace(',','').replace('.','').split(" ")
	for w in line_word:
		words.append(w)
for i in range(0, len(words)):
	count = 1
	for j in range(i+1, len(words)):
		if(words[i] == words[j]):
			count = count + 1
	if(count > fr):
		fr = count;
		wr = words[i];
print("Most repeated word: " + wr)
print("Frequency: " + str(fr))
f.close()
