
def day02():
	commands, units = open_file()

	part_1(commands, units)

	part_2(commands, units)


def part_1(commands, units):
	distance = 0
	depth = 0
	for i in range(len(commands)):
		if commands[i] == "forward":
			distance += units[i]
		elif commands[i] == "down":
			depth += units[i]
		elif commands[i] == "up":
			depth -= units[i]
	print(f"Part 1\n"
		f"Distance: {distance}  Depth: {depth}  Answer: {depth * distance}")


def part_2(commands,units):
	aim = 0
	distance = 0
	depth= 0

	for i in range(len(commands)):
		if commands[i] == "forward":
			distance += units[i]
			depth += units[i] * aim
		elif commands[i] == "down":
			aim += units[i]
		elif commands[i] == "up":
			aim -= units[i]
	print(f"Part 2\n"
		f"Distance: {distance}  Depth: {depth}  Answer: {depth * distance}")


def open_file():
	commands, units = [], []
	with open('Day 02 input') as f:
		instructions = f.read().split("\n")
	for instruction in instructions:
		command, unit = instruction.split(" ")
		commands.append(command)
		units.append(int(unit))
	return commands, units


if __name__ == "__main__":
	day02()
