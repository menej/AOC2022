import copy

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

covered_areas = set()

for line in lines:
    sensor, beacon = line.split(": closest beacon is at ")
    sx, sy = [int(x.split("=")[1]) for x in sensor.split("at ")[1].split(", ")]
    beacon = (int(x.split("=")[1]) for x in beacon.split(", "))
    beacon_hit = False
    loading_sensing = []
    current_sensing = [(sx, sy)]
    covered_areas.add((sx, sy))
    while not beacon_hit:
        while current_sensing:
            current = current_sensing.pop(0)
            covered_areas.add(current)
            cov_up = (current[0], current[1] - 1)
            cov_right = (current[0] + 1, current[1])
            cov_down = (current[0], current[1] + 1)
            cov_left = (current[0], current[1] - 1)

            if cov_up not in covered_areas:
                loading_sensing.append(cov_up)
            if cov_right not in covered_areas:
                loading_sensing.append(cov_right)
            if cov_down not in covered_areas:
                loading_sensing.append(cov_down)
            if cov_left not in covered_areas:
                loading_sensing.append(cov_left)

            if beacon in [cov_up, cov_right, cov_down, cov_left]:
                beacon_hit = True
        current_sensing = copy.copy(loading_sensing)
        loading_sensing = []



