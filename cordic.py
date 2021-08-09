from math import *

def arctan_taylor(k):
	r = k
	sym = -1
	for n in range(3,1000,2):
		r += sym*(k**n)/n
		sym *= -1
	return degrees(r)
		
def angle(n):
	return arctan_taylor(1/2**n),1/2**n
	
def c(n):
	return 1.0/(sqrt(1+2**(-2*n)))

cf = 1
for i in range(40):
	cf *= c(i)

req_angle = 50
x0 = 1
y0 = 0
radius_angle = 0
for k in range(40):
	alpha,arc_angle = angle(k)
	if radius_angle < req_angle:
		radius_angle += alpha
		new_x0 = x0 - y0*arc_angle
		new_y0 = y0 + x0*arc_angle
	elif radius_angle > req_angle:
		radius_angle -= alpha
		new_x0 = x0 + y0*arc_angle
		new_y0 = y0 - x0*arc_angle
	y0 = new_y0
	x0 = new_x0
print(f"my_cos={cf*x0},cos={cos(radians(req_angle))}")
print(f"my_sin={cf*y0},sin={sin(radians(req_angle))}")
