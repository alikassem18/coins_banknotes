from coins_package import sn2_module

with open('serial_numbers.txt') as x:
  y = x.read()
  serial_nums_list = y.split('\n')

a = 0
for serial_num in serial_nums_list:
  a += 1
  for b in range(a, len(serial_nums_list)):
    two_sn_list = [func_name for func_name in sn2_module.C_Functions if sn2_module.C_Functions[func_name](serial_num, serial_nums_list[b])]
    if two_sn_list != []:
      print(f'{serial_num}({serial_nums_list.index(serial_num)}), {serial_nums_list[b]}({serial_nums_list.index(serial_nums_list[b])}), {two_sn_list}')









'''

085138869(696), 085138955(1602), ['SBSN']

068790029(1248), 068790994(1576), ['SBSN']
068790029(1248), 068790423(1622), ['SBSN']
069140196(1252), 069140197(1575), ['SBSN']


085217131(1566), 085217850(1609), ['SBSN']
085217131(1566), 085217527(1610), ['SBSN']
068790994(1576), 068790423(1622), ['SBSN']
087580354(1586), 087580517(1615), ['SBSN']
087580354(1586), 087580050(1618), ['SBSN']
085217850(1609), 085217527(1610), ['SBSN']
087580517(1615), 087580050(1618), ['SBSN']

'''
