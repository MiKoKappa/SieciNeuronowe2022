import sys
from ast import literal_eval

# Przykład:
# python3 perceptron.py ((1,0,0),(1,0,1),(1,1,0),(1,1,1)) [1,0,1] (0,0,0,1) 1

x = literal_eval(sys.argv[1])
w = literal_eval(sys.argv[2])
d = literal_eval(sys.argv[3])
o = int(sys.argv[4])
y = list(0 for i in range(len(d)))
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
matching = testOutput(d,y)
while(not matching):
	suma = 0
	for i in range(len(x)):
		for p in range(len(x[i])):
			suma = suma + x[i][p]*w[p]
		y[i] = 1 if suma > 0 else 0
		print("w:",w)
		for p in range(len(x[i])):
			w[p] = float(w[p]) + o*(float(d[i])-float(y[i]))*float(x[i][p])
	matching = testOutput(d,y)
	print("d:",d)
	print("Y:",y)
	print("-----------------------")
	pass
print(w)