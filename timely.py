def n_no_of_fibonacci_series(number_of_series):
	"""OK fibonacci it is"""
	print("These are %d fibonacci numbers: Actually I've returned it to you..." % number_of_series)

	for i in range(number_of_series):
		# fibonacci
		p = ((((1 + 5 ** .5) ** (i + 1) - (1 - 5 ** .5) ** (i + 1)) / ((2 ** (i + 1)) * 5 ** .5)))
		yield int(round(p,0))  # remember though this is slower than the counter part of logic and
		# also this can't process more than 1200 or more results because the calculation parameter is just
		# to to to to to to to to to to large............. whereas I can do it with logic indefinitely


def n_no_of_prime_numbers(k):
	n = 2
	l = []
	while len(l) <= k:
		for i in range(2, n):
			d = n % i
			if d == 0:
				break
		else:
			yield n
		n += 1

if __name__ == "__main__":
	import time
	print(a := time.time())
	genf = n_no_of_fibonacci_series(50)
	genp = n_no_of_prime_numbers(50)
	for unnecessary_number in range(50):
		print(genf.__next__(), "--->>>>", genp.__next__())
	print(b := time.time(), b - a)
