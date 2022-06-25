import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def f(a):
	t5 = 16*(125+a)
	t4 = -8*(64+a)
	t3 = 40*(59+4*a)
	t2 = -8*(176+29*a)
	t1 = 10*(-281+8*a)
	t0 = 896+245*a
	beef = [t5,t4,t3,t2,t1,t0]
	return [(1/16) * geef for geef in beef]

x = []
real_rs = []
for i in range(11):
	real_rs.append([])
	x.append(i/10)
	coeff = f(i/10)
	rs = np.roots(coeff)
	for r in rs:
		if r.imag == 0:
			real_rs[i].append(r.real)
	#print("a=" + str(i/10) + ", roots:" + str(real_rs[i]))

for i in range(3):
	y = [j[i] for j in real_rs]
	x_new = np.linspace(0, 1,500)
	f = interp1d(x,y,kind='quadratic')
	y_smooth = f(x_new)
	plt.plot(x_new,y_smooth)
	plt.scatter(x,y)
plt.xlabel("a")
plt.ylabel("x-axis")
plt.title("Bifurcation Diagram of Specified Quintic on the Range [0,1]")
plt.savefig('blurg.pdf')
