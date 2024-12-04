import re

# only 14 blue cubes, 13 green cubes, and 12 red cubes
with open('puzzle-input.txt', 'r') as file:
    total_sum = 0
    for line in file:
        # print(line)
        game_id = re.search(r"\d+(?=:)", line).group()
        # print(game_id)
        total_blue_cubes = re.findall(r"\d+(?= blue)", line)
        total_red_cubes = re.findall(r"\d+(?= red)", line)
        total_green_cubes = re.findall(r"\d+(?= green)", line)
        possible_game = True
        for blue_cubes in total_blue_cubes:
            if int(blue_cubes) > 14:
                possible_game = False
        for red_cubes in total_red_cubes:
            if int(red_cubes) > 12:
                possible_game = False
        for green_cubes in total_green_cubes:
            if int(green_cubes) > 13:
                possible_game = False
        pass
        print(possible_game, line.strip())
        if possible_game:
            total_sum += int(game_id)
            print(game_id, total_sum)
        pass
        print()
    print(total_sum)
