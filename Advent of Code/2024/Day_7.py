import os
from itertools import product

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
	totals = set()
	for line in tests.readlines():
		test_strings = line.replace(":", "").strip().split(" ")
		test = [int(item) for item in test_strings]
		test_result = test.pop(0)
		
		def check(combo):
			equation = test[0]
			for i in range(1, len(test)):
				if combo[i-1] == "+":
					equation += test[i]
				elif combo[i-1] == "|":
					equation = int(f"{equation}{test[i]}")
				else:
					equation *= test[i]
			
			return equation
		
		for combination in product("+*|", repeat=len(test) -1):
			calculated = check(combination)
			if calculated == test_result:
				print(test_result, calculated, ' -- works')
				totals.add(calculated)
				total = sum(totals)
				
	return total



if __name__ == "__main__":
	
	cwd = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(cwd, 'Day_7_input.txt')
	calibrations = open(filename)
	total_results = main(calibrations)
	
	print(total_results)
