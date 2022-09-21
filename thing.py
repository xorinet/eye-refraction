import matplotlib.pyplot as plt
from math import *

def solve_intersection(m1, c1, m2, c2):
    # solves for intersection of y = m1x + c1 and y = m2x + c2
    # uses cramer's rule
    return ((c1 - c2)/(m1 - m2), (m1*c2 - c1*m2)/(m1 - m2))

# variables
intv = pi/100   # interval in radians between consecutive theta_1s
start = 2*intv  # start      (radians)
stop = pi/2     # stop       (radians)

n2 = 2          # refractive indices (?)
n1 = 1

thetarange = [start + i*intv for i in range(int((stop - start) // intv))] # will calculate from (intv) to (pi/2) with interval intv

# code
pointsx = []
pointsy = []

i = intv
m1 = sqrt(1-sin(i))/sin(i)
c1 = -(sin(i)/sqrt((n2/n1)**2-sin(i)**2))*m1
for i in thetarange:
    m2 = sqrt(1-sin(i))/sin(i)
    c2 = -(sin(i)/sqrt((n2/n1)**2-sin(i)**2))*m2
    res = solve_intersection(m1, c1, m2, c2)
    pointsx.append(res[0])
    pointsy.append(res[1])
    m1 = m2
    c1 = c2

plt.plot(pointsx, pointsy, marker="+")
plt.show()

# pointsx and pointsy are the x and y lists of the points
# use them to your own advantage if you need to :)


