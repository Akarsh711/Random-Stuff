from queue import Queue

graph = {
	0:[1,2],
	1:[2,0,3,4],
	2:[0,1],
	3:[1,5],
	4:[1],
	5:[6,7,8],
	6:[5],
	7:[5,8],
	8:[5,7,9],
	9:[8],
}


g2 = {
	0:[1,2],
	1:[0,3],
	2:[0,3],
	3:[1,2,4,0],
	4:[3],
}

q = Queue()
queue = q.queue
visited_arr = [False]*graph.__len__()

def BFS(graph, vertex):
	queue.append(vertex)
	visited_arr[vertex] = True

	while queue.__len__() != 0:

		s = queue.popleft()
		print(s)
		
		for i in graph[s]:
			if not visited_arr[i]:
				queue.append(i)
				visited_arr[i] = True
				

BFS(g2, 0)