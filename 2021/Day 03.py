
def day03():
	report, length = open_file()

	part_1(report, length)

	part_2(report, length)


def part_1(report, length):
	gamma = 0b0
	epsilon = 0b0
	for i in range(length):
		i = length-1-i
		bit = common_bit(report, 2**i)
		gamma += bit * (2**i)
		epsilon += 2 ** i
	epsilon = gamma ^ epsilon
	power = epsilon * gamma
	print(f"Part 1: Power consumption is {power}")


def part_2(report, length):
	oxy, co2 = report[:], report[:]
	oxy = bit_criteria(length, oxy, "oxy")
	co2 = bit_criteria(length, co2, "co2")
	print(f"Part 2: Life Support Rating is {oxy * co2}")


def bit_criteria(length, report, criteria):
	for i in range(length):
		i = length - i - 1
		bit = 2 ** i
		removal = []
		search = common_bit(report, bit) * bit
		search = search if criteria == "oxy" else search ^ bit
		for j in range(len(report)):
			if report[j] & bit != search:
				removal.append(j)
		for j in range(len(removal)):
			j = len(removal) - j - 1
			report.pop(removal[j])
		if len(report) == 1:
			return report[0]


def common_bit(report, bit):
	ones, zeroes = 0, 0
	for i in report:
		if i & bit == bit:
			ones += 1
		else:
			zeroes += 1
	if ones > zeroes:
		return 1
	elif zeroes > ones:
		return 0
	elif zeroes == ones:
		return 1


def open_file():
	with open('Day 03 input') as f:
		report = f.read().split("\n")
	length = len(report[0])
	for i in range(len(report)):
		report[i] = int(report[i], 2)
	return report, length


if __name__ == "__main__":
	day03()
