import sys
a = sys.argv[1]
# h1 = 0.10
# h2 = 0.20
# h3 = 0.40
# h4 = 0.20
# h5 = 0.10
f = open('result.txt','w')
f.write("Observation sequence Q: "+str(a))
f.write("\n")
f.write("Length of Q: "+str(len(a)))
f.write("\n\n")

h = [0.10,0.20,0.40,0.20,0.10]

c1h1 = 1 
l1h1 = 0 
c2h2 = 0.75 
l2h2 = 0.25
c3h3 = 0.50 
l3h3 = 0.50
c4h4 = 0.25
l4h4 = 0.75
c5h5 = 0
l5h5 = 1

q1 = (c1h1*h[0])+(c2h2*h[1])+(c3h3*h[2])+(c4h4*h[3])+(c5h5*h[4])
q2 = (l1h1*h[0])+(l2h2*h[1])+(l3h3*h[2])+(l4h4*h[3])+(l5h5*h[4])



q = 0.0
for i in range(0,len(a)):
	# print(str(i-1))
	# print(a[i-1])
	if(a[i]=='C'):		
		h[0] = ((c1h1) * h[0])/q1
		h[1] = ((c2h2) * h[1])/q1
		h[2] = ((c3h3) * h[2])/q1
		h[3] = ((c4h4) * h[3])/q1
		h[4] = ((c5h5) * h[4])/q1
		if(i!=(len(a)-1)):
			if(a[i+1]=='C'):
				q1 = (c1h1*h[0])+(c2h2*h[1])+(c3h3*h[2])+(c4h4*h[3])+(c5h5*h[4])
				q2 = 1-q1
			if(a[i+1]=='L'):
				q2 = (l1h1*h[0])+(l2h2*h[1])+(l3h3*h[2])+(l4h4*h[3])+(l5h5*h[4])
				q1 = 1-q2
		else:
			q1 = (c1h1*h[0])+(c2h2*h[1])+(c3h3*h[2])+(c4h4*h[3])+(c5h5*h[4])
			q2 = 1-q1

	else:
		h[0] = ((l1h1) * h[0])/q2
		h[1] = ((l2h2) * h[1])/q2
		h[2] = ((l3h3) * h[2])/q2
		h[3] = ((l4h4) * h[3])/q2
		h[4] = ((l5h5) * h[4])/q2
		if(i!=(len(a)-1)):
			if(a[i+1]=='C'):
				q1 = (c1h1*h[0])+(c2h2*h[1])+(c3h3*h[2])+(c4h4*h[3])+(c5h5*h[4])
				q2 = 1-q1
			if(a[i+1]=='L'):
				q2 = (l1h1*h[0])+(l2h2*h[1])+(l3h3*h[2])+(l4h4*h[3])+(l5h5*h[4])
				q1 = 1-q2
		else:
			q2 = (l1h1*h[0])+(l2h2*h[1])+(l3h3*h[2])+(l4h4*h[3])+(l5h5*h[4])
			q1 = 1-q2


	f.write("After Observation "+str(i+1)+" = "+str(a[:i+1])+" :")
	f.write("\n\n")

	f.write("P(h1 | Q) = "+str(h[0]))
	f.write("\n")
	f.write("P(h2 | Q) = "+str(h[1]))
	f.write("\n")
	f.write("P(h3 | Q) = "+str(h[2]))
	f.write("\n")
	f.write("P(h4 | Q) = "+str(h[3]))
	f.write("\n")
	f.write("P(h5 | Q) = "+str(h[4]))
	f.write("\n\n")
	f.write("Probability that the next candy we pick will be C, given Q:"+str(q1))
	f.write("\n")
	f.write("Probability that the next candy we pick will be L, given Q:"+str(q2))
	f.write("\n\n")
f.close()
	# f.write("Length of Q: "+str(len()))
	# print("after observation sequence"+str(a[:i]))
	# for i in range(5):
	# 	print(h[i])
	# print("q1"+str(q1))
	# print("q2"+str(1-q1))