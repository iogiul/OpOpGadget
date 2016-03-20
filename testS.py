from OpOp.Model import Sersic,Plummer, GeneralModel
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma,gammaincc

'''
m=0.71
p=0.2496389605237055
x=m*(3-p)

def d(r,m):
    x=2*m
    return (1-gammaincc(x,r**(1/m)))


def dd(r,m):
    n=1/m
    p=1-0.6097*n+0.05463*n*n
    x=m*(3-p)
    return (1-gammaincc(x,(r/rc)**(1/m)))

a=Sersic(0.71,1,5e7)

r=np.linspace(0,100,10000)

plt.plot(r,dd(r,m))
plt.plot(r,d(r,m))
plt.ylim(0.00001,1)
plt.yscale('log')
plt.xscale('log')
plt.show()
'''

a=Sersic(0.71,0.581,5e7)
b=Plummer(0.581,5e7)
r=np.linspace(0.0001,100,10000)

rr=np.logspace(np.log10(0.000003),np.log10(300),512)
print(rr)
dens=a.dens(rr*0.581)



c=GeneralModel(rr,dens/np.max(dens),0.581,5e7)
#print(c._evaluatedens(0.5))
#print(a.dens([0.5,]))

#plt.plot(r,a.dens(r))
#plt.plot(r,a.sdens(r))
plt.plot(r,a.pot(r),c='black')
#plt.plot(r,b.pot(r),c='blue')
plt.plot(r,c.pot(r),c='red')
#plt.plot(r,c.pot(r))
#plt.xlim(0.000001,10)
plt.ylim(100,1000)
plt.xscale('log')
plt.yscale('log')
plt.show()
