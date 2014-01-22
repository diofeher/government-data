import operator
import csv
cities = {}
states = {}
city_state = {}
with open('201311_BolsaFamiliaFolhaPagamento.csv', 'rb') as csvfile:
	for line in csvfile:
		info = line.split('\t')
		state = info[0]
		city = info[2]

		if city not in cities:
			cities[city] = 0
			city_state[city] = state
		else:
			cities[city] += 1
		if state not in states:
			states[state] = 0
		else:
			states[state] += 1

print cities
print states
print city_state
# for line in sorted(states.iteritems(), key=operator.itemgetter(1), reverse=True):
# 	print '%s: %s' % (line[0], line[1])