def find_cycles(graph, path, cycles, n):

    if len(path) == n:

        if graph[path[-1]][path[0]] == 1:

            cycles.append(path[:] + [path[0]])

        return

    for vertex in range(1, n):

        if vertex not in path and graph[path[-1]][vertex] == 1:

            path.append(vertex)

            find_cycles(graph, path, cycles, n)

            path.pop()


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


cycles = []

find_cycles(graph, [0], cycles, n)

# Remove reverse duplicate cycles
unique_cycles = []

for cycle in cycles:

    reverse_cycle = [0] + list(reversed(cycle[1:-1])) + [0]

    if reverse_cycle not in unique_cycles:
        unique_cycles.append(cycle)


print("\nHamiltonian Cycles:")

for cycle in unique_cycles:
    print(" → ".join(map(str, cycle)))

print("\nTotal Cycles =", len(unique_cycles))
