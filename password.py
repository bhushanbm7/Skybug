password=input("Enter password :- ")
uppercase=False
lowercase=False
digit=False
if(len(password)>=8):
	for letter in password:
		if(letter.isupper()):
			uppercase=True
		if(letter.islower()):
			lowercase=True
		if(letter.isdigit()):
			digit=True
	if(lowercase):
		if(uppercase):
			if(digit):
				print("You have entered valid password")
			else:
				print("You have entered invalid passsword")
				print("Your password must contain atleast one digit")
		else:
			print("You have entered invalid passsword")
			print("Your password must contain atleast one uppercase")
	else:
		print("You have entered invalid passsword")
		print("Your password must contain atleast one lowercase")
else:
	print("You have entered invalid password")
	print("Your password must contain atleast 8 letters")