import sys
from ast import literal_eval

# Przykład:
# python3 bupa.py ((1,0,0),(1,0,1),(1,1,0),(1,1,1)) (1,0,1) (0,0,1,0) 1

x = literal_eval(sys.argv[1])
w = list(literal_eval(sys.argv[2]))
d = literal_eval(sys.argv[3])
o = int(sys.argv[4])

y = list(0 for i in range(len(d)))
xw = list(0 for i in range(len(d)))

for a in x:
	if(len(a)!=len(w)):
		print("Mismatch of array lengths!")
		exit()
if(len(x)!=len(d)):
	print("Mismatch of array lengths!")
	exit()

def testOutput(d,y):
	for i in range(len(d)):
		if(d[i]!=y[i]):
			return False
	return True
print("x:",x)
matching = False;
while(not matching):
	print("w:",w)
	for i in range(len(x)):
		for p in range(len(x[i])):
			xw[i] = xw[i] + x[i][p]*w[p]
	print("xw:",xw)
	for i in range(len(x)):
		y[i] = 1 if xw[i] > 0 else 0
		if(y[i] != d[i]):
			for z in range(len(x[i])):
				if(y[i] > d[i]):
					w[z] = w[z] - o*x[i][z]
				else:
					w[z] = w[z] + o*x[i][z]
	matching = testOutput(d,y)
	print("Y:",y)
	print("d:",d)
	print("-----------------------")
	pass
print("w:",w)