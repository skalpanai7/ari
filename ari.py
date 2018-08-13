def sumOfAP(n,a,d) :
	sum=0
	x=0
	while(x<n):
		sum=sum+a
		a=a+d
		x=x+1
	return sum
n,a,d=map(int,raw_input().split())
print(sumOfAP(n,a,d))
