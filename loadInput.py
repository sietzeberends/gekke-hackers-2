f = open('e_high_bonus.txt')
i = 0

for line in f.readlines():

    if i == 0:
        meta = line.split()
        rides = []

    else:
        ride = line.split()
        rides.append(ride)
    i += 1

print("meta")
print(meta)

print("rides")
for ride in rides:
    print(ride)
