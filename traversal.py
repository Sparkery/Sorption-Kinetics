#Aditya Ponukumati
#Ethoxyquin Tracker
#March 4, 2015

#Comapre pictures to see total distance traversed of ethoxyquin

#Find the total distance travelled
#d1 and d2 are position vectors
#output is the magnitude of the change in distance vector
def compareCenter(d1, d2):
	dd = []
	dd[0] = d1[0] - d2[0]
	dd[1] = d1[1] - d2[1]
	print (dd[0]**2 + dd[1]**2)**0.5
	
#Find the center of the spreaded chemical
#f is a ppm file
#output is a position vector for the center
def calculateCenter(f):
	sx = 0 #sum of x-axis
	sy = 0 #sum of y-axis
	
	px = 600 #pixels across
	py = 400 #pixels vertical
	
	for X in range(0, px): #pixels across
		for Y in range(0, py) #pixels vertical
			s = f.readline().split(" ")
			if(s[0] == 0 and s[1] == 255 and s[2] == 255)
				sx += X
				sy += Y
	
	p = [] #position vector for average
	p[0] = sx / px
	p[1] = sy / py
	
	return p
		
#Run the fox
def main():
	f1 = open("frame1.ppm", "r")
	f2 = open("frame2.ppm", "r")
	
	d1 = calculateCenter(f1)
	d2 = calculateCenter(f2)
	
	dd = compareCenter(d1, d2)
	
	print "Position 1", d1
	print "Position 2", d2
	print "Delta Position", dd
