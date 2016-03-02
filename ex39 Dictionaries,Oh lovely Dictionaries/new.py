def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0,num_buckets):
		aMap.append([])
	return  aMap

states = new()
states = {'CN':'china'}
states['gz'] = "guangzhou"

print ' '.join(states.keys())
