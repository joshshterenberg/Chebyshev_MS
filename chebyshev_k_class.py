import numpy as np
from scipy.integrate import quad
import math
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Chebyshev Basis Tester for Class of K Functions\n')
func = input('type function of x (no spaces):_')
num_of_coeff = int(input('number of cheb coeffs:_'))
gamma_input = input('class of functions for gammas in terms of k (no constant):_')
def gamma_generator(k):
	return eval(gamma_input)

gammas = []
for i in range(0, num_of_coeff):
	current_gamma = gamma_generator(i)
	#current_gamma = float(input('gamma_{0}'.format(i) + ':_'))
	gammas.append(current_gamma)
print('')

def f(x,n):
	multiplier = '*(1-x**2)**(-1/2)*('+func+')'
	lst = [0] * n
	lst[n-1] = 1 #eval('(1-x**2)**(-1/2)*('+func+')')
	tpl = tuple(lst)
	cheb = np.polynomial.chebyshev.Chebyshev(tpl)
	coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)
	#print(coef)
	p1 = '('
	for i in range(len(coef)):
		p1 = p1 + str(coef[i]) + '*x**{0}'.format(i)
		if i != len(coef)-1:
			p1 = p1 + '+'
	p1 = p1 + ')'
	#print(p1)
	p1 = p1 + multiplier
	#print(p1)
	return eval(p1)

print("Coefficients of Chebyshev Polynomial:")
coeffs = []
for i in range(0,num_of_coeff):
	lhs = quad(f, -1, 1, args=(i+1))[0]
	if i == 0: lhs = lhs / math.pi
	else: lhs = 2 * lhs / math.pi
	coeffs.append(lhs)
	print('a_{0}'.format(i) + ': ' + str(lhs))

print('')
print("Reconstruction of polynomials with custom gammas generated from class...")
alt_coeffs = [[0] * len(coeffs) for _ in range(10000)]
for k in range(10000):
	for i in range(len(coeffs)):
		#print(i)
		lst = [0] * (i+1)
		lst[i] = coeffs[i] * (gammas[i] + (k/100))
		tpl = tuple(lst)
		cheb = np.polynomial.chebyshev.Chebyshev(tpl)
		coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)
		for j in range(len(coef)):
			alt_coeffs[k][j] += coef[j]
#for i in range(len(alt_coeffs)):
	#print("f_{0}".format(i) + ": " + str(alt_coeffs[i]))
print('')
print('Generating roots of new polynomials...')
print('First constant in gamma function that generates complex roots: ', end='')
for k in range(10000):
	d = list(reversed(alt_coeffs[k]))
	p1 = np.poly1d(d)
	for i in range(len(p1.r)):
		if isinstance(p1.r[i], complex):
			print((k/100))
			exit()




