def facto(i):
	if(i==0):
		return 1
	else:
		return i*facto(i-1)
s=facto(5)
print(s)
