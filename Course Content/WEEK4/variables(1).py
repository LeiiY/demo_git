# Global Vs. Local Variables
# total1 = 0

# def sum(arg1, arg2):
# 	global total2 
# 	total2 = arg1 + arg2
# 	print("Inside the function total: ", total2)

# sum(10, 20)
# print("Outside the function total: ", total2)

# Recursion
# def myRecursion(remaining):
# 	if remaining == 0:
# 		return

# 	print("Hi")
# 	myRecursion(remaining - 1)	

# myRecursion(12)	


# Lambda
# test = lambda a : a + 2
# print(test(3))

# test = lambda a, b : a * b
# print(test(2, 7))

def my_function(num):
	return lambda a : a * num

doubles = my_function(2)

print(doubles(20))	













