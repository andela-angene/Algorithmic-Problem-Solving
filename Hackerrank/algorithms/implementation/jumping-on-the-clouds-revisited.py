number_of_clouds, jump = 8, 2
clouds = [0, 0, 1, 0, 0, 1, 1, 0]
energy, position = 100, 0

while energy > 0:
    position = (position + jump) % number_of_clouds
    energy -= 1 if clouds[position] == 0 else 3
    if position == 0:
        break

print(energy)
