input_file = open('inputd07.txt','r')
input_lines = input_file.readlines()

import re

modulo = 2**16
ref_expr = {}
for line in input_lines:
  [expr, var] = line.strip().split(' -> ')
  expr_elements = expr.split(' ')
  expr_length = len(expr_elements)
  if expr_length == 1:
    ref_expr[var] = '0 + ' + expr
  elif expr_length == 2:
    ref_expr[var] = str(modulo - 1) + ' - ' + expr_elements[1]
  elif expr_length == 3:
    if expr_elements[1] == 'AND':
      ref_expr[var] = expr_elements[0] + ' & ' + expr_elements[2]
    elif expr_elements[1] == 'OR':
      ref_expr[var] = expr_elements[0] + ' | ' + expr_elements[2]
    elif expr_elements[1] == 'LSHIFT':
      ref_expr[var] = expr_elements[0] + ' << ' + expr_elements[2]
    elif expr_elements[1] == 'RSHIFT':
      ref_expr[var] = expr_elements[0] + ' >> ' + expr_elements[2]

while True:
  for x in ref_expr:
    if re.search('\d+\ \D+\ \d+', ref_expr[x]):
      repl_var = x
      repl_expr = str(eval('('+ref_expr[x]+')%'+str(modulo)))
      break
  if repl_var == 'a':
    print repl_expr
    break
  for x in ref_expr:
    if re.search('(^|\W)'+repl_var+'($|\W)', ref_expr[x]):
      ref_expr[x] = re.sub('(?<!\w)'+repl_var+'(?!\w)',repl_expr,ref_expr[x],2)
  ref_expr.pop(repl_var)
