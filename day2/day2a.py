file_input = open("input.txt", "r")

horizontal_position = 0
depth = 0

for line in file_input.readlines():
    controls = line.split(" ")
    direction = controls[0]
    units = int(controls[1])

    if direction == "forward":
        horizontal_position += units
    elif direction == "up":
        depth -= units
    elif direction == "down":
        depth += units

    print("{} {}".format(horizontal_position, depth))

print("Final value is {}".format(horizontal_position * depth))