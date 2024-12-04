with open('puzzle-input.txt', 'r') as file:
    total_sum = 0
    words_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in file:
        characters = []
        numbers = []
        print(line.strip())
        for position in range(len(line)):
            for word, number in words_numbers.items():
                if line[position:].startswith(word):
                    line = line[:position] + number + line[position+1:]
        print(line.strip())
        characters.extend(line.strip())
        for character in characters:
            if character.isnumeric():
                numbers.append(int(character))
        print(numbers)
        line_sum = int(str(numbers[0]) + str(numbers[-1]))
        print(line_sum)
        total_sum += line_sum
        print(total_sum, "\n")
    print(total_sum)
