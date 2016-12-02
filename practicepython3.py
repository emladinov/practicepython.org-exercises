#This code lists an array of numbers that are less than the number given
#by the user.

top = int(input("Please input a number that should cap the list: "))
print(list([x for x in [1,1,2,3,5,8,13,21,34,55,89] if x<top]))
