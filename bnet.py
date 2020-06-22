import sys
import copy
class Bayesian:
	def __init__(self):      
		self.pb = 0.001
		self.pe = 0.002
		self.pb1e1 = 0.95
		self.pb1e0 = 0.94
		self.pb0e1 = 0.29
		self.pb0e0 = 0.001
		self.pja1 = 0.90
		self.pja0 = 0.05
		self.pma1 = 0.70
		self.pma0 = 0.01
	def computeProbability(self,b,e,a,j,m):   #COMPUTE PROBABILITY FUNCTION
		temp = 1.0
		if(b==True):
			temp = temp * self.pb
		elif(b==False):
			temp = temp*(1-self.pb)
			# print(temp)
		if(e==True):
			temp = temp * self.pe
		elif(e==False):
			temp = temp*(1-self.pe)
			# print(temp)
		if(a==True):
			if(b==True and e==True):
				temp = temp * self.pb1e1
			elif(b==False and e==True):
				temp = temp * self.pb0e1
			elif(b==True and e==False):
				temp = temp * self.pb1e0
			elif(b==False and e==False):
				temp = temp * self.pb0e0
				# print(temp)
		elif(a==False):
			if(b==True and e==True):
				temp = temp * (1-self.pb1e1)
			elif(b==False and e==True):
				temp = temp * (1-self.pb0e1)
			elif(b==True and e==False):
				temp = temp * (1-self.pb1e0)
			elif(b==False and e==False):
				temp = temp * (1-self.pb0e0)
		if(j==True):
			if(a==True):
				temp = temp * self.pja1
				# print(temp)
			elif(a==False):
				temp = temp * self.pja0
		elif(j==False):
			if(a==True):
				temp = temp * (1-self.pja1)
			elif(a==False):
				temp = temp * (1-self.pja0)
			# temp = temp*(1-self.pb)
		if(m==True):
			if(a==True):
				temp = temp * self.pma1
				# print(temp)
			elif(a==False):
				temp = temp * self.pma0
			# temp = temp * self.pb
		elif(m==False):
			if(a==True):
				temp = temp * (1-self.pma1)
			elif(a==False):
				temp = temp * (1-self.pma0)
		return temp





arguments =  len(sys.argv)
if(arguments<2 or arguments >7):
	print("enter a valid arguments only 6 arguments including given no more or less than 6")
	sys.exit()
a = False
c1 = []
c2 = []
for i in range(1,arguments):
	if(sys.argv[i]=="given"):
		a = True
		if(len(sys.argv[i+1:])>4):
			print("enter 4 or less arguments after given statement")
			sys.exit()
	else:
		if(a==False):
			c1.append(sys.argv[i])
		else:
			c2.append(sys.argv[i])


# READING BEFORE GIVEN ARGUMNETS (NUMERAOTR)
temp = [] 		
for i in range(len(c1)):
	w  = c1[i]
	if(w[0]=="B"):
		temp.append("B")
		if(w[1]=="t"):
			B = True
		else:
			B = False
	elif(w[0]=="E"):
		temp.append("E")
		if(w[1]=="t"):
			E = True
		else:
			E = False
	elif(w[0]=="A"):
		temp.append("A")
		if(w[1]=="t"):
			A = True
		else:
			A = False
	elif(w[0]=="J"):
		temp.append("J")
		if(w[1]=="t"):
			J = True
		else:
			J = False
	elif(w[0]=="M"):
		temp.append("M")
		if(w[1]=="t"):
			M = True
		else:
			M = False	
#ARGUMENTS AFTER "GIVEN" STRING (DENOMINATOR)	
temp1 = []
for i in range(len(c2)):
	w  = c2[i]
	if(w[0]=="B"):
		temp1.append("B")
		if(w[1]=="t"):
			B = True
		else:
			B = False
	elif(w[0]=="E"):
		temp1.append("E")
		if(w[1]=="t"):
			E = True
		else:
			E = False
	elif(w[0]=="A"):
		temp1.append("A")
		if(w[1]=="t"):
			A = True
		else:
			A = False
	elif(w[0]=="J"):
		temp1.append("J")
		if(w[1]=="t"):
			J = True
		else:
			J = False
	elif(w[0]=="M"):
		temp1.append("M")
		if(w[1]=="t"):
			M = True
		else:
			M = False
temp = temp + temp1

#FINDING NUMERATOR'S PARENTS AND CHILD IN JOIN PROBABILITIES WHICH ARE NOT DEFINE IN COMMAND LINE ARGUMENTS 
z =  False
z1 = False
z2 = False
z3 = False
t1 = []
for i in temp:
	# print(i)
	if(i=='J'):
		for j in temp:
			if(j=='A'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t1.append('A')
		if(z1==False):
			t1.append('B')
		if(z2==False):
			t1.append('E')
		if(z3==False):
			t1.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False
	if(i=='M'):
		for j in temp:
			if(j=='A'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='J'):
				z3 = True
		if(z==False):
			t1.append('A')
		if(z1==False):
			t1.append('B')
		if(z2==False):
			t1.append('E')
		if(z3==False):
			t1.append('J')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False						  # m a b e
	if(i=='A'):
		for j in temp:
			if(j=='J'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t1.append('J')
		if(z1==False):
			t1.append('B')
		if(z2==False):
			t1.append('E')
		if(z3==False):
			t1.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False						  # m a b e

	if(i=='B'):
		for j in temp:
			if(j=='J'):
				z = True
			if(j=='A'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t1.append('J')
		if(z1==False):
			t1.append('A')
		if(z2==False):
			t1.append('E')
		if(z3==False):
			t1.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False					

	if(i=='E'):
		for j in temp:
			if(j=='J'):
				z = True
			if(j=='A'):
				z1 = True
			if(j=='B'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t1.append('J')
		if(z1==False):
			t1.append('A')
		if(z2==False):
			t1.append('B')
		if(z3==False):
			t1.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False	
	
s1 = set(t1)
d1 = list(s1)


#FOR DENOMINATOR FIND PARENTS AND CHILDEREN IN  JOIN PROBABILITIES WHICH ARE NOT DEFINE IN COMMAND LINE ARGUMENTS
z =  False
z1 = False
z2 = False
z3 = False
t2 = []
for i in temp1:
	#print(i)
	if(i=='J'):
		for j in temp1:
			if(j=='A'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t2.append('A')
		if(z1==False):
			t2.append('B')
		if(z2==False):
			t2.append('E')
		if(z3==False):
			t2.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False
	if(i=='M'):
		for j in temp1:
			if(j=='A'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='J'):
				z3 = True
		if(z==False):
			t2.append('A')
		if(z1==False):
			t2.append('B')
		if(z2==False):
			t2.append('E')
		if(z3==False):
			t2.append('J')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False						  # m a b e
	if(i=='A'):
		for j in temp1:
			if(j=='J'):
				z = True
			if(j=='B'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t2.append('J')
		if(z1==False):
			t2.append('B')
		if(z2==False):
			t2.append('E')
		if(z3==False):
			t2.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False						  # m a b e

	if(i=='B'):
		for j in temp1:
			if(j=='J'):
				z = True
			if(j=='A'):
				z1 = True
			if(j=='E'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t2.append('J')
		if(z1==False):
			t2.append('A')
		if(z2==False):
			t2.append('E')
		if(z3==False):
			t2.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False					

	if(i=='E'):
		for j in temp1:
			if(j=='J'):
				z = True
			if(j=='A'):
				z1 = True
			if(j=='B'):
				z2 = True
			if(j=='M'):
				z3 = True
		if(z==False):
			t2.append('J')
		if(z1==False):
			t2.append('A')
		if(z2==False):
			t2.append('B')
		if(z3==False):
			t2.append('M')
		z = False
		z1 = False                                # j a b e   a 
		z2 = False	
		z3 = False	
s2 = set(t2)
d2 = list(s2)
#print("d2",d2)

# COMPUTING DIFFERENT COMBINATION OF PROBABILITES
g = Bayesian()  #CLASS OBJECT
model = {}
for i in temp:
	if(i=='B'):
		model['kb'] = B
	if(i=='E'):
		model['ke'] = E
	if(i=='A'):
		model['ka'] = A
	if(i=='J'):
		model['kj'] = J
	if(i=='M'):
		model['km'] = M


model1 = {}
# g = Bayesian()
for i in temp1:
	if(i=='B'):
		model1['kb'] = B
	if(i=='E'):
		model1['ke'] = E
	if(i=='A'):
		model1['ka'] = A
	if(i=='J'):
		model1['kj'] = J
	if(i=='M'):
		model1['km'] = M



def a(d1,model):   #FUNCTION FOR RECUSIVE CALL
	if(len(d1)==0):
		# print("terminal")
		# print(model)
		return g.computeProbability(model['kb'],model['ke'],model['ka'],model['kj'],model['km'])
	else:
		p = d1[0]
		rest = d1[1:]
		truea = a(rest,extend(model,p,True))
		falsea = a(rest,extend(model,p,False))
		return truea+falsea
		

def extend(model, p, value):
	model_new = copy.deepcopy(model) 
	if(p=='B'):
		model_new['kb'] = value
	if(p=='E'):
		model_new['ke'] = value
	if(p=='A'):
		model_new['ka'] = value
	if(p=='J'):
		model_new['kj'] = value
	if(p=='M'):
		model_new['km'] = value
        
	# model_new[p] = value
	return model_new

p1 = a(d1,model)
if(len(c2)!=0):
	#print(d2)
	#print(model1)
	p2 = a(d2,model1)
	print(p1/p2)
else:
	print(p1)	


