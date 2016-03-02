import hashmap_d

states = hashmap_d.new()
hashmap_d.set(states,'Oregon','OR')


cities = hashmap_d.new()
hashmap_d.set(cities,'CA','San Francisco')

print '-' * 20
print "%s"% hashmap_d.get(cities,'CA')

import hashmap
states = hashmap.new()
hashmap.set(states,'CN','china')
hashmap.set(cities,'china','Beijing')

print '-' * 20
print "%s"% hashmap.get(states,'CN')

hashmap.get_slot(cities,'CN','china')
hashmap.list(states)
hashmap.list(cities)

mystuff = {'apple':'I am apples!'}
print mystuff['apple']

def apple():
	print "i am apples!"

apple()