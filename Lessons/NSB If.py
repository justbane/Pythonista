"""
An if statement allows you to check on the value of a variable and do something based on that value

Example:
	if first_name is "Nolan":
		do something

"""

secret = "12121"

while (passcode := input("Enter you passcode")) != "q":
	if passcode == secret:
		print("Welcome to the secret chanber!!!")
	else:
		print("Access DENIED!!!!")
