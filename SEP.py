try:
	def ESP():
		ES=open("SECP.txt" , "a")
		ES1=open("SECP.txt" , "r")
		print("THE FILE WILL SAVE IN TXT SEARCH FILE USING SEARCH IN YOUR SYSTEAM OR IN WINDOWDS IT IS IN C:USER OR WHER YOU RUN FILE")
		print("if you enter 1 instance of name in student name it will exit the program and save the data")
		student=input("enter student  name=")
		sub1=input("enter the sub1 name=")
		sub2=input("enter the sub2 name=")
		sub3=input("enter the sub3 name=")
		mark1=float(input("enter the sub1 marks="))
		mark2=float(input("enter the sub2 marks="))
		mark3=float(input("enter the sub3 marks="))
		total=mark1+mark2+mark3
		sub1marks=(str(mark1)+"you get this marks in "+sub1)
		sub2marks=(str(mark2)+"you get this marks in "+sub2)
		sub3marks=(str(mark3)+"you get this marks in "+sub3)
		passmarks=float(input("enter total passing marks="))
		ESC=[[student],[sub1],[sub2],[sub3],[sub1marks],[sub2marks],[sub3marks],[total]]
		if total>passmarks:
			print("you pass"+student)
			ES.write(str(ESC))
			ES1.read()
			ES.close()
			for es in ESP():
				es	 
		else:
			print("you fail"+student)
			ES.write(str(ESC))
			ES1.read()
			ES.close()
			for es in ESP():
				es	 
except ValueError:
	print("No Number is put at passingmarks")
print("type  enter to add name  and other")
ESP_RUN=input("$")
if ESP_RUN=="add":
	ESP()

else:
	print("invlide command")

