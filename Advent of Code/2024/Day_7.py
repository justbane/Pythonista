'''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).
'''


def main(tests):
	total = 0
	for line in tests.readlines():
		test = line.replace(":", "").strip().split(" ")
		test_result = test.pop(0)
		
		print(test_result, test)
	
	
	return total

if __name__ == "__main__":
	
	calibrations = open('Day_7_input.txt')
	total_results = main(calibrations)
	
	print(total_results)
