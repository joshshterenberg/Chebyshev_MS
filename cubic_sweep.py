import math
import numpy
print('A fully generalized cubic equation sweeper')
s = int(input('largest bound of space to sweep:_'))

def ncr(n,k):
	return math.factorial(n) / ((math.factorial(k))*(math.factorial(n-k)))

def f(k,b,c,d):
	return k**3+b*k**2+c*k+d
for b in range(-s,s):
	for c in range(-s,s):
		for d in range(-s,s):
			total_terms = []
			for i in range(1,3):
				total_term = 0
				term = 0.5 * ncr(2*i,i) * f(0,b,c,d)
				total_term += term
				#print(str(total_term),end='+')
				for j in range(1,i+1):
					term = ((-1)**j) * ncr(2*i,i-j) * f(2*j,b,c,d)
					total_term += term
					#print(str(total_term),end='+')
				#print('K=' + str(i) + ': ' + str(total_term))
				total_terms.append(total_term)
			if numpy.sign(total_terms[0]) == numpy.sign(total_terms[1]):
				print("Hit case where signs equal each other")
				print("K=1: " + str(total_terms[0]) + ", K=2: " + str(total_terms[1]))
				print("Located at: b=" + str(b) + ",c=" + str(c) + ",d=" + str(d))
				exit()
			total_terms = []
