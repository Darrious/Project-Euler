
# Darrious Barger
# Problem: Find the sum of all the multiples of 3 or 5 below 1000.

i=0
sum = 0

while i < 1000:
	if (i % 3 == 0 or i % 5 == 0):
		sum += i
	i += 1

print("Sum:", sum)