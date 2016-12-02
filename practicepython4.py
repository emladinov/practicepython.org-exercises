#This code will show all divisors of a number input by the user

num = int(input("Please enter a number to see it's divisors: "))

listofdivisors = [x for x in range(1,num) if num%x==0]
print(listofdivisors)
