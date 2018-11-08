file = open(“Hero Journey Story.txt”,”w”) 

file.write(“Hello World”) 
file.write(“This is my guide to the heros journey”) 

file.close()

file = open(“Hero Journey Story.text”, “r”) 
print file.read() #shown everything but $ Cat
print file.readline(2)

for line in file:
	print(line)

	