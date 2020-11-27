import numpy as np
from scipy import interpolate


def spline(x,y,point,deg):

    tck,u = interpolate.splprep([x,y],k=deg,s=0) 
    u = np.linspace(0,1,num=point,endpoint=True) 
    spline = interpolate.splev(u,tck)
    return spline[0],spline[1]

def make_curve2(x, y):

	if len(x) <= 5:
		a3,b3 = spline(x,y,100,len(x)-1)
	elif len(x) > 5:
		a3,b3 = spline(x,y,100,5)


	return a3, b3


def main():
	x = [1, 2, 3, 4, 5, 6]
	y = [1, 1, 3, 4, 5, 6]
	print(x,y)
	x2, y2 = make_curve2(x,y)


if __name__ == "__main__":
	main()
