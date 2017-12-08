input_file = open('inputd08.txt','r')
input_lines = input_file.readlines()

registers = {}
for line in input_lines:
  expression = line.split(' ')
  register_to_modify = expression[0]
  increment = int(expression[2])*(1 if expression[1]=="inc" else -1)
  register_in_condition = expression[4]
  condition = 'registers["' + register_in_condition + '"]' + expression[5] + expression[6]
  
  if register_in_condition not in registers:
    registers[register_in_condition] = 0
  if register_to_modify not in registers:
    registers[register_to_modify] = 0
  if eval(condition):
    registers[register_to_modify] += increment
  
maximal_register = float("-inf")
for register in registers:
  if registers[register] > maximal_register:
    maximal_register = registers[register]
print maximal_register
  

