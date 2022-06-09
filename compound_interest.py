def comp(principle,time,rate):
	if (time==0):
		return principle
	else:
		s=(principle*rate)/100
		return comp(principle+s,time-1,rate)
z=comp(10000,4,2)
print(z)
