import re

# only 14 blue cubes, 13 green cubes, and 12 red cubes
with open('puzzle-input.txt', 'r') as file:
    total_sum = 0
    for game_line in file:
        print(game_line.strip())
        game_id = re.search(r"\d+(?=:)", game_line).group()
        # print(game_id)
        blue_cubes = re.findall(r"\d+(?= blue)", game_line)
        blue_cubes_int = [int(number) for number in blue_cubes]
        red_cubes = re.findall(r"\d+(?= red)", game_line)
        red_cubes_int = [int(number) for number in red_cubes]
        green_cubes = re.findall(r"\d+(?= green)", game_line)
        green_cubes_int = [int(number) for number in green_cubes]
        print(blue_cubes_int, red_cubes_int, green_cubes_int)
        blue_cubes_min = max(blue_cubes_int)
        red_cubes_min = max(red_cubes_int)
        green_cubes_min = max(green_cubes_int)
        min_cubes_power = blue_cubes_min * red_cubes_min * green_cubes_min
        print(f"{blue_cubes_min} * {red_cubes_min} * {green_cubes_min} = {min_cubes_power}\n")
        total_sum += min_cubes_power
    print(total_sum)
