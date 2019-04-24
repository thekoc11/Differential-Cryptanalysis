def SBox(n):
	val = hex(n)
	
	if val == '0x0':		
		return int(0xe)
	elif val == '0x1':
		return int(0x4)
	elif val == '0x2':
		return int(0xd)
	elif val == '0x3':
		return int(0x1)
	elif val == '0x4':
		return int(0x2)
	elif val == '0x5':
		return int(0xf)
	elif val == '0x6':
		return int(0xb)
	elif val == '0x7':
		return int(0x8)
	elif val == '0x8':
		return int(0x3)
	elif val == '0x9':
		return int(0xa)
	elif val == '0xa':
		return int(0x6)
	elif val == '0xb':
		return int(0xc)
	elif val == '0xc':
		return int(0x5)
	elif val == '0xd':
		return int(0x9)
	elif val == '0xe':
		return int(0x0)
	elif val == '0xf':
		return int(0x7)

def PBox(n): 


	val = n + 1
	retval = 0
	# print("inside pbox n is", n)
	if val == 1:
		
		retval = 1
	elif val == 2:
		retval = 5
	elif val == 3:
		retval = val+6
	elif val == 4:
		retval = (val+9)
	elif val == 5:
		retval = val-3
	elif val == 6:
		retval = val
	elif val == 7:
		retval = val+3
	elif val == 8:
		retval = (val + 6)
	elif val == 9:
		retval = (val-6)
	elif val == 10:
		retval = (val-3)
	elif val == 11:
		retval = val
	elif val == 12:
		retval = (val+3)
	elif val == 13:
		retval = (val-9)
	elif val == 14:
		retval = (val-6)
	elif val == 15:
		retval = (val-3)
	elif val == 16:
		retval = val

	return retval-1

def convertBin(n):
	p = format(n, '#06b')
	p = p[2:]
	p = [int (x) for x in p]
	return p
def BackToInt(l):
	r = 0
	for item in l:
		r = (r<<1)|item
	return r

def DeltaX(xp):
	delX = []
	for i in range(16):
		delX.append(i ^ xp)
		# print("X and Xstar", i, delX[i])
	return delX
class SPN:

	K = []
	Key = [3, 10, 9, 4, 13, 6, 3, 15]
	U = [[], [], [], []]
	V = [[], [], [], []]
	W = [[], [], []]
	Y = []
	_X = []

	def __init__(self, X):
		u = []
		v = []
		w = []
		v_w = []
		self._X = X
		for i in range(5):
			rkey = []
			for j in range(i, i+4):
				rkey.append(self.Key[j])
			# print(rkey)
			self.K.append(rkey)
		for x in X:
			if len(x) != len(self.K[1]):
				print("invalid input")
				pass
			else:
				# W[0] = x
				for i in range(0, 4):
					if i is 0:
						for j in range(4):
							u.append(x[j] ^ self.K[0][j])
							# print("part u0", u[j])
						self.U[i] = u
						u = []
					else:
						for j in range(4):
							u.append(self.W[i-1][j] ^ self.K[i][j])
							# print("part u",i, u[j])
						self.U[i] = u
						u = []

					for j in range(4):
						v.append(SBox(self.U[i][j]))
						v_w.append(convertBin(v[j]))
						# print("part v",i, v[j])

					self.V[i] = v
					v = []

					w_row = []
					# _w_ = 0
					# wmod = 0
					if i != 3:
						for j in range(4):
							# _w_ = v[int(PBox(self.V[i][j])/4)]
					# 		wmod = (int(PBox(self.V[i][j]) % 4))
					# 		print("wmod", wmod)
							k = j*4
							for m in range (k, k+4):
								w_row.append(v_w[int(PBox(m)/4)][PBox(m)%4])
							w.append(w_row)
							w_row = []
						for j in range(4):
							w[j] = BackToInt(w[j])
							# print("part w",i, w[j])

						self.W[i] = w
						w = []
						v_w = []
					else:
						for j in range(4):
							w.append(self.V[i][j] ^ self.K[i+1][j])
							# print("part y", w[j])
						self.Y = w
						w = []
						
	def display(self):
		# W_disp = [bin(_X), bin(W[0]), bin(W[1]), bin(W[2])]
		K0_disp = []
		K1_disp = []
		K2_disp = []
		K3_disp = []
		K4_disp = []
		W_disp = []
		V_disp = []
		U_disp = []
		Y_disp = []

		for i in range(4):
			K0_disp.append(convertBin(self.K[0][i]))
			K1_disp.append(convertBin(self.K[1][i]))
			K2_disp.append(convertBin(self.K[2][i]))
			K3_disp.append(convertBin(self.K[3][i]))
			K4_disp.append(convertBin(self.K[4][i]))

		# for i in range(5):
		for w in self.W:
			w_d = []
			# print(len(w))
			for i in range(len(w)):
				w_d.append(convertBin(w[i]))
			W_disp.append(w_d)
		for u in self.U:
			u_d = []
			# print(len(w))
			for i in range(len(u)):
				u_d.append(convertBin(u[i]))
			U_disp.append(u_d)
		for v in self.V:
			v_d = []
			# print(len(w))
			for i in range(len(v)):
				v_d.append(convertBin(v[i]))
			V_disp.append(v_d)

		y_d = []

		for y in self.Y:
			y_d.append(convertBin(y))
		Y_disp.append(y_d)
		X_disp = []
		for x in self._X:
			x_d = []
			for i in range(len(x)):
				x_d.append(convertBin(x[i]))
			X_disp.append(x_d)

		for w in W_disp:
			print("W is", w)

		for w in U_disp:
			print("U is", w)

		for w in V_disp:
			print("V is", w)

		for w in Y_disp:
			print("Y is", w)

		print("K[0] is ", K0_disp)
		print("K[1] is ", K1_disp)
		print("K[2] is ", K2_disp)
		print("K[3] is ", K3_disp)
		print("K[4] is ", K4_disp)

	def DiffAttack(self, T, Pi_inv):

		count = []
		for l1 in range(0, 16):
			countRow = []
			for l2 in range(0, 16):
				countRow.append(0)
			count.append(countRow)
			# print (countRow)

		for [x, y, x_, y_] in T:
			if y[0] == y_[0] and y[2] == y_[2]:
				for l1 in range(0, 16):
					for l2 in range(0, 16):
						v42 = l1 ^ y[1]
						v44 = l2 ^ y[3]
						u42 = Pi_inv[v42]
						u44 = Pi_inv[v44]
						v42_ = l1 ^ y_[1]
						v44_ = l2 ^ y_[3]
						u42_ = Pi_inv[v42_]
						u44_ = Pi_inv[v44_]
						u42Prime = u42 ^ u42_
						u44Prime = u44 ^ u44_
						# print(u42Prime == 0b0110 and u44Prime == 0b0110)
						if u42Prime == 0b0110 and u44Prime == 0b0110:
							# print(u42Prime)
							count[l1][l2] = count[l1][l2] + 1

		_max = -1
		# maxkey = [0, 0]

		for l1 in range(0, 16):
			for l2 in range(0, 16):
				if count[l1][l2] > _max:
					_max = count[l1][l2]
					maxkey = [l1, l2]

		maxkey_disp = [bin(maxkey[0]), bin(maxkey[1])]
		print (maxkey_disp)
		# print (T)



##################### FINAL Algorithm ################################
X_prime = [] #constant x', change here to get a different key value

for i in range(0, 16):
	X_prime.append(i)

DeltaX_ = []#both x and x* in this dict
# X = [[0, 0, 0, 0]]#this stands for 0000 0000 0000 0000
X =  []
for i in range(0, 16):
	DeltaX_.append(DeltaX(i))

for i in range(0, 16):
	print("DeltaX_ for X' = 11", DeltaX_[i][11])	
		
for i in range(0, 16):
	X.append(i)
		
# print ("\n")
XStar = []
# for i in range(0, 16):
# 	_x = [X_XStar[0][i], X_XStar[1][i], X_XStar[2][i], X_XStar[3][i]]
# 	XStar.append(_x)

for x in X:
	x_starRow = []
	for xp in X_prime:
		x_starRow.append(DeltaX_[x][xp])
	XStar.append(x_starRow)

print(XStar[11])
# for x in X:
# 	print (x[1], "\n")




Y = []
YStar = []

for x_ in X:
	Y.append(SBox(x_))


for x_ in XStar:
	yrow = []
	for j in range(16):
		yrow.append(SBox(x_[j]))
	YStar.append(yrow)

print(YStar[11])

Y_Prime = []

for y in YStar:
	yrow = []
	for j in range(16):
		yrow.append(Y[j] ^ y[j])
	Y_Prime.append(yrow)

print(Y_Prime[11])

b_prime = []

for y in Y_Prime:
	brow = []
	for i in range(16):
		c = y.count(i)
		brow.append(c)
	b_prime.append(brow)

for b in b_prime:
	print(b)

Nd = []
for b in b_prime:
	ndrow = []
	for j in range(16):
		ndrow.append(float(b[j]))
	print(ndrow)
	Nd.append(ndrow)
		
def Rp(i, j):
	return(Nd[i][j]/16)
# for x in Y:
# 	print ("Y", x[1], "\n")
# print(YStar)
Pi_inv = {0:0}

for i in range(0, 16):
	Pi_inv[SBox(i)] = i

T = []

for i in range(len(X)):
	x = X[i]
	x_ = XStar[i]
	y = Y[i]
	y_ = YStar[i]
	t = [x, y, x_, y_]
	T.append(t)

print(len(X))


# print(YStar)
# print(Pi_inv)
# print(yStarbin)
# print(yPrimeBin)

INP = []
for i in range(16):
	# print ("x",[0, i, 0, 0] )
	INP.append([0, i, 0, 0])

sp = []
for i in range(16):
	sp.append(SPN([INP[i]]))
t1 = sp[10].W[0]
print(t1)
INP1 = []
for i in range(16):
	# print ("x*", [0, DeltaX_[11][i], 0, 0] )
	INP1.append([0, DeltaX_[11][i], 0, 0])
sp1 = []
for i in range(16):
	sp1.append(SPN([INP1[i]]))
t2 = sp1[10].W[0]
print(t2)

# print(Y_Prime[8][3])
for i in range(len(t1)):
	print(t1[i] ^ t2[i])

I = [[0, 11, 0, 0]]
sp3 = SPN(I)
t3 = sp3.V[0]
print(t3)
# for i in range(len(sp.U[0])):
	# print(sp.U[0] )#^ sp1.U[0][i])
# sp[3].display()
# DiffAttack(T, Pi_inv)
# ___l = convertBin(15)
# print(___l)
# print(BackToInt(___l))