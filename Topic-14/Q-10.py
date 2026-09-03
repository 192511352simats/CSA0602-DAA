def is_safe(vertex, graph, path, position):

    # Check connection
    if graph[path[position - 1]][vertex] == 0:
        return False

    # Check already included
    if vertex in path:
        return False

    return True


def hamiltonian_cycle(graph, path, position, n):

    if position == n:

        if graph[path[position - 1]][path[0]] == 1:
            return True

        return False

    for vertex in range(1, n):

        if is_safe(vertex, graph, path, position):

            path[position] = vertex

            if hamiltonian_cycle(graph, path, position + 1, n):
                return True

            path[position] = -1

    return False


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


path = [-1] * n
path[0] = 0


if hamiltonian_cycle(graph, path, 1, n):

    print("\nHamiltonian Cycle Exists:")

    cycle = path + [path[0]]

    print(" → ".join(map(str, cycle)))

else:
    print("Hamiltonian Cycle Does Not Exist")
