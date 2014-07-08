number = 0
print type(number)
delta = 1000000000000000000
while delta >= 1:
	while type(number) is int:
		number += delta
		print number

	number=int(number-delta)
	delta /=1000
print number