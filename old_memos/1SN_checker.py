from patterns import A_Functions, B_Functions

with open('serial_numbers.txt') as x:
  y = x.read()
z = y.split('\n')
for a in z:
  b = []
  c = []
  for d in A_Functions:
    if A_Functions[d](a):
      b.append(d)
  if b != []:
    print('with prefix:',a,':',b)
  for e in B_Functions:
    if B_Functions[e](a[2:]):
     c.append(e)
  if c != []:
    print('without prefix:',a[2:],':',c,'\n')

