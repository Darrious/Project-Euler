
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


answer = 0
mult_range = 20
i = 1
found = False

while i < 999_999_999:
	i+=1
	found = True

	if (i%2==0):
		for j in range(1,mult_range):
			if (i%j!=0):
				found = False

	else:
		found = False

	if (found):
		answer = i
		break
	
print(answer)
