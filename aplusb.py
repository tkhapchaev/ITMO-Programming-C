filein = open("aplusbb.in")
fileout = open("aplusbb.out", "w")
a, b = map(int, filein.readline().split())
print(a + b * b, file = fileout)
fileout.close()