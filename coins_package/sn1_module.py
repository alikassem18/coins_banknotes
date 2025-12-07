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



def replacement(a):
  return a.startswith('99')

def super_radar(a):
  return a == a[::-1]

def special_solid(a):
  return a.count(a[0]) == len(a)

def polymer(a):
  return a.startswith('22')



def repeater(a):

  for b in range(2,len(a)//2+1):
    if sub_repeater(a,b):
      return True
  return False

def doubles(a):
  b = ['00','11','22','33','44', '55','66','77','88','99']
  c = 0
  for d in b:
    c += a.count(d)
  return c == len(a)//2

def ladder(a):
  b = a.strip('0')
  c = -1
  d = 0
  for g in range(len(b)-1):
    c = c+1
    d = d+1
    e = int(b[d])
    f = int(b[c])
    if e != f+1 and e != f-1:
      return False
  return True

def binary(a):
  b = '0123456789'
  c = ''
  for d in b:
    if d in a:
      c = c+d
  return len(c) == 2



def low_serial(a):
  return int(a[2:]) < 100000

def radar(a):
    b = a[2:]
    return b == b[::-1]

def solid(a):
  return a[2:].count(a[2]) == len(a[2:])

def mini_solid(a):
  b = '0123456789'
  for c in b:
    if a[2:].count(c) == len(a[2:])-1:
      return True
  return False





A_Functions = {'replacement': replacement, 'super_radar': super_radar, 'special_solid': special_solid, 'polymer': polymer, 'repeater': repeater, 'doubles': doubles, 'ladder': ladder, 'binary': binary}

B_Functions = {'repeater': repeater, 'doubles': doubles, 'ladder': ladder, 'binary': binary}

C_Functions = {'low_serial': low_serial, 'radar': radar, 'solid': solid, 'mini_solid': mini_solid}