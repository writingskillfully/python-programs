f = open("example.txt", "r")
g = open("example_output.txt", "w")
#These lines of code open an input file to read from and creates a file to store ouput in.

count = 1
for i in f:
# this for statement makes the program read the first line so readline function is not necessary
	if count%2 == 0: #double equal sign has the program check if the left side is equal to the right side. 
					 #single equal sign will just assign the left side the right side value.
		g.write(i) #the print function will not write the output text to the file
	count += 1 #the count needs to be in the for loop or the value of count will not change because iteration is not invoked

f.close()
g.close()

	
