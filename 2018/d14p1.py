input_file = open('inputd14.txt','r')
input_lines = input_file.readlines()

lookup_position = int(input_lines[0].strip())
lookup_length = 10

scoreboard = [3, 7]
number_of_recipes = len(scoreboard)
recipe_indices = [0, 1]

while number_of_recipes < lookup_position + lookup_length:
  current_scores = [scoreboard[x] for x in recipe_indices]
  current_sum = sum(current_scores)
  if current_sum > 9:
    scoreboard.extend([current_sum / 10, current_sum % 10])
    number_of_recipes += 2
  else:
    scoreboard.append(current_sum)
    number_of_recipes += 1

  recipe_indices = [(index + score + 1) % number_of_recipes for index,score in zip(recipe_indices, current_scores)]

print ''.join(map(str, scoreboard[lookup_position : lookup_position + lookup_length]))
