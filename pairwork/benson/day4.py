import matplotlib.pyplot as plt

sum_values = [(num, sum([(value - num)**2 for value in [2, 7, 1, 5, 10]])) for num in
				[x/10.0 for x in range(0, 101)]]

values = [item[0] for item in sum_values]
sums = [item[1] for item in sum_values]

print("min: {}".format(min(sum_values, key = lambda x: x[1])))

plt.plot(values, sums)
plt.show()

'''
def summation(num):
	data = [2, 7, 1, 5, 10]
	sumlist = []
	for integer in data:
		sumlist.append((integer-num)**2)
	return sum(sumlist)
​
def run_problem():
	steps = [x/10.0 for x in range(0, 101)]
	results = [(num, summation(num)) for num in steps]
	yvalues = [summation(num) for num in steps]
	lowest = min(results, key=lambda x: x[1])
	print(lowest)
	plt.plot(steps, yvalues)
	plt.show()
​'''

#if __name__ == "__main__":
#	run_problem()
