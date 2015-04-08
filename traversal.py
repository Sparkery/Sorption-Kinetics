#Aditya Ponukumati
#Ethoxyquin Tracker
#March 25, 2015

#Comapre pictures to see total distance traversed of ethoxyquin

#Find the total distance travelled
#d1 and d2 are position vectors
#output is the magnitude of the change in distance vector
def compareCenter(d1, d2):
	print d1, d2
        dd = [-1, -1]
	dd[0] = d1[0] - d2[0]
	dd[1] = d1[1] - d2[1]
	return (float(dd[0])**2 + float(dd[1])**2)**0.5

#Find the center of the spreaded chemical
#f is a ppm file, SPECIFIC TO ONE PIXEL PER LINE
#output is a position vector for the center
def calculateCenter(f):
	sx = 0 #sum of x-axis
	sy = 0 #sum of y-axis

	px = 600 #pixels across
	py = 400 #pixels vertical

##        f.readline()
##        f.readline()
##        f.readline()
##
##	for X in range(0, px): #pixels across
##		for Y in range(0, py): #pixels vertical
##			s = f.readline().split(" ")
##			if(s[0] == "0" and s[1] == "0" and s[2] == "0"):
##				sx += X
##				sy += Y


        image = f.read().split()
        px = int(image[1])
        py = int(image[2])
        rbg = list(map(int, image[4:]))

        sx = 0
        sy = 0

        found = 0

        for Y in range(0, px*py):
            if(rbg[Y*py + 0] == 0 and rbg[Y*py + 1] == 0 and rbg[Y*py + 2] == 0):
                found += 1
                sx += Y / py + 0.5
                sy += Y % py + 0.5

                p = [-1, -1] #position vector for average

                p[0] = float(sx) / found
                p[1] = float(sy) / found

                return p

#Run the fox
def main():
	f1 = open("frame1.ppm", "r")
	f2 = open("frame2.ppm", "r")

	d1 = calculateCenter(f1)
	d2 = calculateCenter(f2)
        print d1, d2
	dd = compareCenter(d1, d2)

	print "Position 1", d1
	print "Position 2", d2
	print "Delta Position", dd

main()
