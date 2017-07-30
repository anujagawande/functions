#q1.determines if f is a function with domain A and target B.

def isFunction(A,B,f):
	for i in range(len(f)):
		# Starting range from i+1, don't compare to self
		for j in range(i+1, len(f)):
			if f[i][0] == f[j][0]:#compare 1st element from 1st list of f to second element in 2nd list n so on...
				return False
	return True

A = [1,2,3]
B = [4,5,]
f = [ [1,4], [2,5], [3,4] ]
f2 = [ [1,4], [1,5], [3,4] ]

print "-------------q1------------------"
print f, ": ", isFunction(A,B,f)#true case: is a function
print f2, ": ", isFunction(A,B,f2)#false case: not a function
print "---------------------------------\n"

#------------------------------------------------------------

#q2.returns the image/target of a function

def image(f):
	I = []
	temp = []
	for i in range(len(f)):
		if f[i][1] not in I:#if the image value doesnt exist already... add to image
			I.append(f[i][1])

	I = sorted(I)#sorting in ascending order
	return I



f = [ [1,4],
      [2,5],
      [3,4]]

print "-------------q2------------------"
print image(f)
print "---------------------------------\n"
#-----------------------------------------------------------


#q3. determines if a function is a one-to-one function

def isOneToOne(A,B,f):

	#getting the domain of f 
	I = []
	for i in range(len(f)):
		#if the domain value doesnt exist already... add to domain
		if f[i][0] not in I:
			I.append(f[i][0])
	I = sorted(I)#sorting in ascending order
	A = sorted(A)

	if A != I:#if all elements of domain are not linked...its not ontoone
		return False 

	for i in range(len(f)):
		# Starting range from i+1, don't compare to self
		for j in range(i+1, len(f)):
			#compare 1st element from domain to 2nd element and 1st element of range to 2nd element and so on...
			if f[i][0] == f[j][0] or f[i][1] == f[j][1]:
				return False
	return True


A = [1,2,3]
B = [4,5]
f = [ [1,4],
      [2,5],
      [3,4] ]

print "-------------q3------------------"
print isOneToOne(A,B,f)
print "---------------------------------\n"

#------------------------------------------------------------


#q4. determines if a function is onto function
def isOnto(A,B,f):

#getting the range of f 
	I = []
	temp = []
	for i in range(len(f)):
		if f[i][1] not in I:#if the image value doesnt exist already... add to image
			I.append(f[i][1])
	I = sorted(I)#sorting in ascending order
	
	

	B = sorted(B)#sorting target in ascending order
	#compraring target and range...if they are same it is onto otherwise it's not
	if I == B:
		return True
	return False

A = [1,2,3]
B = [4,5]
f = [ [1,4],
      [2,5],
      [3,4] ]

print "-------------q4------------------"
print isOnto(A,B,f)
print "---------------------------------\n"

#------------------------------------------------------------


#q5. returns the inverse of the function

def inverse(A,B,f):
	
	if isFunction(A,B,f)== True and isOneToOne(A,B,f)== True and isOnto(A,B,f)==True: #check if it is a function and both onetoone and onto(bijective),
	#then its has an inverse...
		temp = ''
		for i in range(len(f)):
			for j in range(len(f)):
				temp = f[i][j]#swapping the positions of domain and range.
				f[i][j] = f[i][1]
				f[i][1] = temp

				i=i+1
				temp = f[i][j]#swapping the positions of domain and range.
				f[i][j] = f[i][1]
				f[i][1] = temp

				i=i+1
				temp = f[i][j]#swapping the positions of domain and range.
				f[i][j] = f[i][1]
				f[i][1] = temp
				
		
				return f
	return None

A = [1,2,3]
B = [4,5,6]
f = [ [1,4],
      [2,5],
      [3,6] ]

print "-------------q5------------------"
print inverse(A,B,f)
print "---------------------------------\n"








			
			
