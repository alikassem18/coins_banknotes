def replacement(a):
  return a.startswith('99')

def super_radar(a):
  b = ""
  for c in range(1,len(a)+1):
    d = a[-c]
    b = b + d
  return b == a

def radar(a):
  b = super_radar(a[2:])
  return b

def special_solid(a):
  b = a.count(a[0])
  return b == len(a)

def solid(a):
  b = special_solid(a[2:])
  return b

def mini_solid(a):
  b = '0123456789'
  for c in b:
    if a[2:].count(c) == len(a[2:])-1:
      return True
  return False

def low_serial(a):
  return int(a[2:]) < 100000

#**********************************

def binary(a):
  b = '0123456789'
  c = ''
  for d in b:
    if d in a:
      c = c+d
  return len(c) == 2

def sub_repeater(a,b):
  if len(a)%b >= 2:
    return False
  if len(a)%b == 0:
    if a.count(a[:b]) == len(a)//b:
      return True
  if len(a)%b == 1:
    c = a.count(a[:b])
    d = a.count(a[1:b+1])
    e = len(a)//b
    if c == e or d == e:
      return True
  return False

def repeater(a):
  for b in range(2,len(a)//2+1):
    if sub_repeater(a,b):
      return True
  return False

def doubles(a):
  b = ['00','11','22','33','44', '55','66','77','88','99']
  c = 0
  for d in b:
    c = c + a.count(d)
  return c == len(a)//2

def inc_ladder(a):
  b = a.strip('0')
  c = -1
  d = 0
  for g in range(len(b)-1):
    c = c+1
    d = d+1
    e = int(b[d])
    f = int(b[c])
    if e != f+1:
      return False
  return True

def dec_ladder(a):
  b = a.strip('0')
  c = -1
  d = 0
  for g in range(len(b)-1):
    c = c+1
    d = d+1
    e = int(b[d])
    f = int(b[c])
    if e != f-1:
      return False
  return True

#**********************************

def SCSN(a,b):
  c = []
  d = []
  for e in b:
    c.append(e)
  for f in a:
    if f in c:
      d.append(True)
      c.remove(f)
  return len(d) == len(a)

def SSN(a,b):
  return a == b or a[2:] == b[2:]

def SBSN(a,b):
  return a[:-3] == b[:-3]

#**********************************

A_Functions = {'replacement': replacement, 'super_radar': super_radar, 'radar': radar, 'special_solid': special_solid, 'solid': solid, 'mini_solid': mini_solid, 'binary': binary, 'low_serial': low_serial, 'repeater': repeater, 'doubles': doubles, 'inc_ladder': inc_ladder, 'dec_ladder': dec_ladder}

B_Functions = {'repeater': repeater, 'doubles': doubles, 'inc_ladder': inc_ladder, 'dec_ladder': dec_ladder}

C_Functions = {'SBSN': SBSN, 'SSN': SSN, 'SCSN': SCSN}