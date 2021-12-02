file_input = open("input.txt", "r")
file_values = file_input.readlines()
file_len = len(file_values)

higher = 0
lower = 0
last = -1

for i in range(0, file_len, 1):
    if i + 2 < file_len:
        measure = int(file_values[i]) + int(file_values[i + 1]) + int(file_values[i + 2])
        if last != -1:
            if measure > last:
                higher += 1
            elif measure < last:
                lower += 1

        last = measure
        print("{} = {} + {} + {}".format(int(file_values[i]) + int(file_values[i + 1])
                                         + int(file_values[i + 2]), int(file_values[i]),
                                         int(file_values[i + 1]), int(file_values[i + 2])))
    else:
        print("Can't do for {}".format(i))

print("Higher {}".format(higher))
print("Lower {}".format(lower))