file_input = open("input.txt", "r")

last = -1
higher = 0
lower = 0
for line in file_input:

    if last != -1:
        if int(line) > last:
            higher += 1
        elif int(line) < last:
            lower += 1

    last = int(line)

print(higher)
print(lower)