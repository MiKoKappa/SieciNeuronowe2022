import sys
from ast import literal_eval

# Przykład:
# python3 hopfield.py [1,1,1] ((0,-0.666666,0.666666),(-0.666666,0,-0.666666),(0.666666,-0.666666,0))

x = literal_eval(sys.argv[1])
w = literal_eval(sys.argv[2])

for i in range(len(w)):
	if len(w[i]) != len(x):
		print("Błędne wymiary macierzy!")
		exit()
	for j in range(len(w[i])):
		if w[i][i] < 0:
			print("Niespełnione warunki stabilizacji!")
			exit()
		if w[i][j] != w[j][i]:
			print("Niespełnione warunki stabilizacji!")
			exit()

def testOutput(x1,x2):
	for i in range(len(x1)):
		if(x1[i]!=x2[i]):
			return False
	return True

t = 0
print("t:0")
print("x:",x)
print("------------")
xList = list([x.copy()])
matching = False
while(not matching):
	for i in range(len(w)):
		suma = 0
		t = t+1
		print("t:",t)
		for j in range(len(w[i])):
			suma = suma + x[j]*w[i][j]
		print("Suma:",suma)
		if suma>0:
			x[i] = 1
		else:
			x[i] = -1
		xList.append(x.copy())
		print(xList[t])
	matching = testOutput(xList[t-len(w)],xList[t])
print("Stablizacja uzyskana!")