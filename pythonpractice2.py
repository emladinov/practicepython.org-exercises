def mainfunction():
	print("If you would like to see if a number is even, enter 1")
	print("\nIf you would like to check a result with your own number to divide by, press 2")
	#User picks if they want divisible by 2 or their own divisor
	choice =int(input())
	if choice == 1:
		firstfunction()
	elif choice == 2:
		secondfunction()
	else:
		print("Please enter a valid input\n")
		mainfunction()
#function for divisible by 2
def firstfunction():
	try:
		number = int(input("Please enter a number"))	
		if number % 2==0:
			print("The number is even.")
			if number % 4 == 0:
				print("It is also divisible by 4.")
		if number % 2==1:
			print("The number is odd")
		
#		else:
#			print("Please enter a valid input!")
#			firstfunction()
	except ValueError:
		print("Invalid number. Try again...")
		firstfunction()

#function for quotient check of two custom numbers
def secondfunction():
	num = int(input("Please enter a number to check: "))
	check = int(input("Please enter a number to divide by: "))
	if num%check == 0:
		print("The first number is divisible by the second.")
	else:
		print("That number is not divisible by the second.")
mainfunction()
