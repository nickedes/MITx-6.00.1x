def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
	s=0
	i=start
	while i<stop:
		s+=f(i)
		i+=step
	
	return (s)*step
radiationExposure(0, 5, 1)
