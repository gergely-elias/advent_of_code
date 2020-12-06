import fileinput

input_lines = list(fileinput.input())

number_of_valid_phrases = 0
for line in input_lines:
    words = line.strip().split(" ")
    number_of_words = len(words)
    unique_anagrams = set()
    for word in words:
        anagram = "".join(sorted(word))
        unique_anagrams.add(anagram)
    number_of_unique_anagrams = len(unique_anagrams)
    if number_of_words == number_of_unique_anagrams:
        number_of_valid_phrases += 1
print(number_of_valid_phrases)
