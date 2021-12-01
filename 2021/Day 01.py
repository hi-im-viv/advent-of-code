
def day01():
	depths = []
	with open('Day 01 input') as f:
		depths = list(map(int, f.read().split("\n")))

	print(f"Part 1: {measure(depths)}")

	sliding_depths = []
	for i in range(len(depths)-2):
		slide = depths[i] + depths[i+1] + depths[i+2]
		sliding_depths.append(slide)

	print(f"Part 2: {measure(sliding_depths)}")


def measure(depths):
	prev_depth = 0
	dips = 0
	for i, depth in enumerate(depths):
		if i == 0:
			prev_depth = depth
			continue
		dips += 1 if depth > prev_depth else 0
		prev_depth = depth
	return dips


if __name__ == "__main__":
	day01()
