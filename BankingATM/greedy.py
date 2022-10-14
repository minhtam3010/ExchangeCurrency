class ShortestPath(object):

    def __init__(self, location: str):
        self.label = {
            0: "My Home (District 2)",
            1: "Sài Gòn Bridge",
            2: "Thủ Thêm Tunnel",
            3: "ATM Văn Lang District 1",
            4: "ATM Văn Lang Phan Văn Trị",
            5: "ATM Văn Lang Đặng Thùy Trâm",
            6: "BookStore"
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
        self.place = {"ATM": [3, 4, 5], "BookStore": [5]}
        self.location = location
    
    # def printSolution(self, dist) -> None:
    #     print("Vertex \tDistance from Source")
    #     for node in range(self.V):
    #         print(node, "\t\t", dist[node])

    def printResult(self, res):
        print("Shortest path: ")
        for i in range(len(res[:-1])):
            if (i + 1) == len(res[:-1]):
                print(self.label[res[i]], end=" ==> ")
            else:
                print(self.label[res[i]], end=" ---> ")
        print("Total: " + str(res[-1]))

    def min_index(self, dist: list[int], visited: list[bool]) -> int:
        min_num = 10000
        min_index = -1
        for i in range(self.V):
            if dist[i] < min_num and visited[i] == False:
                min_num = dist[i]
                min_index = i
        return min_index
    
    def filter(self, res: list[int], end: int):
        """
            filter array to give the minPath of end value
        """
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
        while previous != start:
            resMinPath = []
            for value in res:
                if value[1] == previous:
                    resMinPath.append(value)
            values = resMinPath[-1]
            previous = values[0]
            result.append(values[1])
        result.append(start)
        return result

    def dijkstra(self, start):
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
        return res

    def FindShortestPathAtm(self, start: int) -> list[int]:
        getShortestPath = []
        self.place[self.location] = list(filter(lambda x: x != start, self.place[self.location]))
        for end in self.place[self.location]:
            res = self.dijkstra(start)
            res, minPath, idx, values = self.filter(res, end)
            if idx == len(res):
                res = res[:idx - 1]
            else:
                res = res[:idx] + res[idx+1:]
            res = self.findPath(res, start, minPath, values)
            res = res[::-1]
            getShortestPath.append(res)
        
        min_values_path = getShortestPath[0][-1]
        final_res = getShortestPath[0]
        for i in range(1, len(getShortestPath)):
            if min_values_path > getShortestPath[i][-1]:
                min_values_path = getShortestPath[i][-1]
                final_res.append(getShortestPath[i])
        self.printResult(final_res[-1] if len(final_res) == 1 else final_res)
        return final_res[-1] if len(final_res) == 1 else final_res


if __name__ == "__main__":
    sp = ShortestPath("ATM")
    res = sp.FindShortestPathAtm(0)
    res = sp.FindShortestPathAtm(3)
    print(res)