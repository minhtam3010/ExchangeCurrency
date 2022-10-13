class ShortestPath(object):

    def __init__(self):
        self.label = {
            0: "My Home (District 2)",
            1: "Sai Gon Bridge",
            2: "Thu Them Tunnel",
            3: "ATM Van Lang District 1",
            4: "ATM Van Lang Phan Van Tri",
            5: "ATM Van Lang Dang Thuy Tram"
        }

        self.distance = [
            [0, 15, 18, 0, 0, 0],
            [0, 0, 0, 18, 15, 0],
            [0, 0, 0, 10, 0, 0],
            [0, 0, 0, 0, 24, 32],
            [0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0]
        ]
        self.V = len(self.distance)
    
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def printResult(self, res):
        print("Shortest path: ")
        for i in range(len(res[:-1])):
            if (i + 1) == len(res[:-1]):
                print(self.label[res[i]], end=" ==> ")
            else:
                print(self.label[res[i]], end=" ---> ")
        print("Total: " + str(res[-1]))

    def min_index(self, dist, visited):
        min_num = 10000
        min_index = -1
        for i in range(self.V):
            if dist[i] < min_num and visited[i] == False:
                min_num = dist[i]
                min_index = i
        return min_index
    
    def filter(self, res, end):
        filter_res = []
        minPath = 10000
        idx = -1
        values = ()
        for value in range(len(res)):
            if res[value][1] < end:
                filter_res.append(res[value])
            if res[value][1] == end:
                filter_res.append(res[value])
                if minPath > res[value][-1]:
                    minPath = res[value][-1]
                    idx = value
                    values = res[value]
        return filter_res, minPath, idx, values

    def findPath(self, res, start, minPath, values):
        result = [minPath] + [values[1]]
        previous = values[0]
        count = 0
        while previous != start:
            resMinPath = []
            for value in res:
                if value[1] == previous:
                    resMinPath.append(value)
            values = resMinPath[-1]
            previous = values[0]
            result.append(values[1])
            if count == 10:
                break
            count += 1
        result.append(start)
        return result

    def dijkstra(self, start, end):
        dist = [10000] * self.V
        dist[start] = 0
        visited = [False] * self.V
        res = []
        for i in range(self.V):
            u = self.min_index(dist, visited)
            visited[u] = True
            for v in range(self.V):
                if self.distance[u][v] > 0 and visited[v] == False and dist[v] > (dist[u] + self.distance[u][v]):
                    dist[v] = dist[u] + self.distance[u][v]
                    res.append((u, v, dist[v]))
        res, minPath, idx, values = self.filter(res, end)
        if idx == len(res):
            res = res[:idx - 1]
        else:
            res = res[:idx] + res[idx+1:]
        res = self.findPath(res, start, minPath, values)
        res = res[::-1]
        self.printResult(res)

if __name__ == "__main__":
    sp = ShortestPath()
    sp.dijkstra(0, 3)