def SCSN(a,b):
  a = list(a)
  a.sort()
  b = list(b)
  b.sort() 
  return a == b

def SSN(a,b):
  return a == b or a[2:] == b[2:]

def SBSN(a,b):
  return a[:-3] == b[:-3]

def RSN(a,b):
  return a == b[::-1]

#C_Functions = {'SBSN': SBSN, 'SSN': SSN, 'RSN': RSN}

C_Functions = {'SBSN': SBSN, 'SSN': SSN, 'SCSN': SCSN, 'RSN': RSN}