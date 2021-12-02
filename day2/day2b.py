file_input = open("input.txt", "r")

horizontal_position = 0
depth = 0
aim = 0

for line in file_input.readlines():
    controls = line.split(" ")
    direction = controls[0]
    units = int(controls[1])

    if direction == "forward":
        horizontal_position += units
        depth += aim * units
    elif direction == "up":
        aim -= units
    elif direction == "down":
        aim += units

    print("{} {}".format(horizontal_position, depth))

print("Final value is {}".format(horizontal_position * depth))