from patterns import C_Functions

with open('serial_numbers.txt') as x:
  a = x.read()
c = a.split('\n')
e = 0
for d in c:
  e = e+1
  for f in range(e, len(c)):
    b = []
    for g in C_Functions:
      if C_Functions[g](d[1:],c[f][1:]):
        b.append(g)
    if b != []:
      print(d,c[f],b,'\n')
