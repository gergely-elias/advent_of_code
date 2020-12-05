input_file = open("inputd04.txt", "r")
input_lines = input_file.readlines()

number_of_valid_phrases = 0
for line in input_lines:
    words = line.strip().split(" ")
    number_of_words = len(words)
    unique_words = set(words)
    number_of_unique_words = len(unique_words)
    if number_of_words == number_of_unique_words:
        number_of_valid_phrases += 1
print(number_of_valid_phrases)
