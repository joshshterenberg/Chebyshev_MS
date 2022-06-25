import math
seq = input('gamma function in terms of k:_')
n = int(input('how many terms in the sum to generate (k=1,2,3,...N?):_'))

def ncr(n,k):
	return math.factorial(n) / ((math.factorial(k))*(math.factorial(n-k)))

def f(k):
	return eval(seq)

total_term = 0
for i in range(1,n+1):
	term = 0.5 * ncr(2*i,i) * f(0)
	total_term += term
	#print(str(total_term),end='+')
	for j in range(1,i+1):
		term = ((-1)**j) * ncr(2*i,i-j) * f(2*j)
		total_term += term
		#print(str(total_term),end='+')
	print('K=' + str(i) + ': ' + str(total_term))
	#print('')
	total_term = 0
