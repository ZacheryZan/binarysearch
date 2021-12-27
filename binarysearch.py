import logging

def binarySearch(a, b):
	try:
		low = 0
		mid = len(a) // 2
		high = len(a)
		while mid != low and mid != high:
			if b == a[mid]:
				return "Found. Array[{}]: {}".format(b, a[mid])
			if b < a[mid]:
				high = mid
				mid = low + ((high - low) // 2)
			else:
				low = mid
				mid = high - ((high - low) // 2)
		return "{} Not Found".format(b)
	except:
		logging.basicConfig(filename= 'logfile.log', filemode= 'w', format= '%(name)s - %(levelname)s - %(message)s')
		logging.warning('failure at date time:')
		print("Failure Logged")

