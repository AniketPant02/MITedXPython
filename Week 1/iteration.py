x = int(input("Enter an integer:"))
ans = 0
while ans ** 3 < x:
	ans += 1
if ans ** 3 != x:
	print(str(x)+ " is not a perfect cube")
else:
	if x < 0:
		ans = - ans
		print("Cube root of " + str(x) + " is " + str(ans))
# Finds cube root of given integer