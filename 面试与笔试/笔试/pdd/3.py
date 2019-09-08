
def func(tasks, graph_inputs):
    import queue
    n = len(tasks)
    graph = {}
    count = [0]*(n+1)
    to_visit = queue.PriorityQueue()
    for g in graph_inputs:
        a, b=g
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        count[b] += 1
    for i in range(1, n+1):
        if count[i] == 0:
            to_visit.put((tasks[i-1], i, i))
    res = []
    # print(count)
    # print(graph)
    while not to_visit.empty():
        temp = to_visit.get()
        _,_,cur = temp
        # print(temp, cur)
        res.append(cur)
        if cur in graph:
            # print(cur)
            for b in graph[cur]:
                count[b] -= 1
                # print('count', b)
                if count[b] == 0:
                    to_visit.put((tasks[b-1], b, b))
    return res



res = func(tasks, graph_inputs)
print(res)

