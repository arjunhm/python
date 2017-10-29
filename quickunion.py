"""
This algorithm makes use of tree stucture where connected nodes hold the
value of the root node.

When a two nodes are connected, say p to q, the root of p is connected
to the root of q.

A weighted quick union is more efficient.
Here the smaller tree is connected to the larger tree.
This is done by comparing the sizes of the tree using the size array.
"""

#INITIALISING THE ARRAY
array = [x  for x in range(10)]
size = [1 for x in array]


#RETURNS THE ROOT OF THE NODE
def root(i):

	while(i != array[i]):
		array[i] = array[array[i]]
		i = array[i]
	return i


#CHECKS IF TWO NODES ARE CONNECTED
def connected(p, q):
	return root(p) == root(q)


#CONNECTS TWO NODES (p to q)
def union(p, q):
	i = root(p)
	j = root(q)
	#print("i: {}, j:{}".format(size[i], size[j]))

	if(size[i] < size[j]):
		array[i] = j
		size[j] += size[i]

	else:
		array[j] = i
		size[i] += size[j]

query = ''

print('Type "Done" to quit')
while 1:
	query = input('Enter the two nodes: ')

	if query == 'done':
		break

	query_list = [int(x) for x in query.strip().split()]
	union(query_list[0], query_list[1])
	print(array)

print("\nFinal array is")
print(array)
