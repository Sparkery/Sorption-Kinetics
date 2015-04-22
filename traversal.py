1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
#Aditya Ponukumati
#Ethoxyquin Tracker
#March 25, 2015
 
#Comapre pictures to see total distance traversed of ethoxyquin
 
#Find the total distance travelled
#d1 and d2 are position vectors
#output is the magnitude of the change in distance vector
def compareCenter(d1, d2):
    dd = [-1, -1] #Initialize difference vector
    dd[0] = d1[0] - d2[0] #Fill difference vector x
    dd[1] = d1[1] - d2[1] #Fill difference vector y
    return (float(dd[0])**2 + float(dd[1])**2)**0.5 #Return the magnitude
 
#Find the geometric center of the spreaded chemical
#f is a ppm file, SPECIFIC TO ONE PIXEL PER LINE (deprecated, now takes all)
#uses human-constructed black/white replecated files
#output is a position vector for the center
def calculateCenter(f):
    sx = 0 #sum of x-axis, initialized
    sy = 0 #sum of y-axis, initialized
 
    image = f.read().split() #Read the entire picture file into a list
    px = int(image[1]) #Gather data containing rows
    py = int(image[2]) #Gather data containing columns
    rgb = list(map(int, image[4:])) # Gather individual pixel data, congregated
 
    #print len(rgb)
 
    found = 0 #number of black squares found
 
    #print px*py
 
    for Y in range(0, px*py, 3): #look through all possible pixels
        #print Y, rgb[Y*py], rgb[Y*py+1], rgb[Y*py+2]
 
        if(rgb[Y + 0] == 0 and rgb[Y + 1] == 0 and rgb[Y + 2] == 0):
            found += 1 #if all three RGB values lead to blackness, found one
            sx += Y / py + 0.5 #formula to calculate contribution to rows
            sy += Y % py + 0.5 #formula to calculate contribution to columns1
 
    p = [-1, -1] #position vector for average
 
    p[0] = float(sx) / found #take the arithmetic average to find mean position
    p[1] = float(sy) / found #take the arithmetic average to find mean position
 
    return p #return a position vector with average black position
 
#Run the fox
def main():
    f1 = open("testframe1.ppm", "r")
    f2 = open("testframe2.ppm", "r")
 
    t = float(raw_input("Time traversed (s): "))
 
    d1 = calculateCenter(f1)
    d2 = calculateCenter(f2)
    print "Position Vectors 1 and 2: ", d1, d2
    dd = compareCenter(d1, d2)
 
    ave = dd/t
     
    print "Position frame 1", d1
    print "Position frame 2", d2
    print "Delta Position", dd
    print
    print "Average speed (pix/s) ", ave
     
main()
