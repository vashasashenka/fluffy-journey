class DynamicArray:
    def __init__(self):
        self.data = []
        self.length = 0

    def append(self, item):
        self.data = self.data + [item]
        self.length += 1

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return
        new_data = []
        for i in range(self.length + 1):
            if i == index:
                new_data.append(data)
            if i < self.length:
                new_data.append(self.data[i])
        self.data = new_data
        self.length += 1

    def delete(self, index):
        if index >= self.length or index < 0:
            return
        new_data = []
        for i in range(self.length):
            if i != index:
                new_data.append(self.data[i])
        self.data = new_data
        self.length -= 1

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

def merge(array, left, middle, right):
    left_array = array[left:middle+1]
    right_array = array[middle+1:right+1]

    i = j = 0
    k = left
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        k += 1
        i += 1

    while j < len(right_array):
        array[k] = right_array[j]
        k += 1
        j += 1

def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def timsort(array):
    min_run = get_minrun(len(array))
    for i in range(0, len(array), min_run):
        insertion_sort(array, i, min(i + min_run - 1, len(array) - 1))
    size = min_run
    while size < len(array):
        for start in range(0, len(array), size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (len(array) - 1))
            merge(array, start, mid, end)
        size *= 2
    return array


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = DynamicArray()

        for i in range(vertices):
            temp_list = DynamicArray()
            for i in range(vertices):
                temp_list.append(0)
            self.graph.append(temp_list)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def print_result(result_edges, total_weight):
    for edge in result_edges:
        edge_labels = [chr(ord('A') + idx) for idx in edge]
        edge_labels_str = ' '.join(edge_labels)
        print(edge_labels_str)
    print(total_weight)


def kruskal(graph):
    edges = DynamicArray()
    for i in range(graph.V):
        for j in range(i + 1, graph.V):
            if graph.graph[i][j] != 0:
                edges.append((graph.graph[i][j], i, j))
    edges = timsort(edges)
    parent = [i for i in range(graph.V)]
    rank = [0] * graph.V
    result = DynamicArray()
    total_weight = 0
    for edge in edges:
        weight, u, v = edge
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            result.append((u, v))
            total_weight += weight
            union(parent, rank, root_u, root_v)
    return result, total_weight

if __name__ == "__main__":
    input_value = open("input.txt", "r")
    lines = input_value.readlines()

    num_vertices = len(lines[0].split())
    graph = Graph(num_vertices)

    for i in range(num_vertices):
        edge_values = list(map(int, lines[i + 1].split()))
        for j in range(num_vertices):
            graph.add_edge(i, j, edge_values[j])

    result, total_weight = kruskal(graph)
    print_result(result, total_weight)
