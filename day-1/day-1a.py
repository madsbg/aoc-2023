
with open('puzzle-input.txt', 'r') as file:
    total_sum = 0
    for line in file:
        characters = []
        numbers = []
        characters.extend(line.strip())
        for character in characters:
            if character.isnumeric():
                numbers.append(int(character))
        line_sum = int(str(numbers[0]) + str(numbers[-1]))
        print(line.strip())
        print(characters)
        print(line_sum)
        total_sum += line_sum
        print(total_sum)
    print(total_sum)
