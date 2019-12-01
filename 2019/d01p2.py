input_file = open('inputd01.txt','r')
input_lines = input_file.readlines()

total_fuel = 0
for line in input_lines:
  module_fuel = int(line.strip())
  while True:
    module_fuel = module_fuel // 3 - 2
    if module_fuel <= 0:
      break
    total_fuel += module_fuel
print(total_fuel)
