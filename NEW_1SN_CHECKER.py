from coins_package import sn1_module

with open('serial_numbers.txt') as x:
  y = x.read()
  serial_nums_list = y.split('\n')

for serial_num in serial_nums_list:
  
  with_prefix = [func_name for func_name in sn1_module.A_Functions if sn1_module.A_Functions[func_name](serial_num)]
  if with_prefix != []:
    print(f'With Prefix: {serial_num}({serial_nums_list.index(serial_num)}) ----------> {with_prefix}')
  
  with_or_without = [func_name for func_name in sn1_module.B_Functions if sn1_module.B_Functions[func_name](serial_num[2:])]
  if with_or_without != []:
    print(f'Without Prefix: {serial_num[2:]}({serial_nums_list.index(serial_num)}) ----------> {with_or_without}')
  
  without_prefix = [func_name for func_name in sn1_module.C_Functions if sn1_module.C_Functions[func_name](serial_num)]
  if without_prefix != []:
    print(f'Without Prefix: {serial_num}({serial_nums_list.index(serial_num)}) ----------> {without_prefix}')