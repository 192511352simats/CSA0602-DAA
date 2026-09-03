import heapq


class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def generate_codes(node, code="", codes=None):

    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = code

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes


n = int(input("Enter number of sensor symbols: "))

characters = input("Enter symbols separated by space: ").split()
frequencies = list(map(int, input("Enter frequencies: ").split()))

heap = []

for i in range(n):
    heapq.heappush(
        heap,
        Node(characters[i], frequencies[i])
    )


while len(heap) > 1:

    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    parent = Node(None, left.freq + right.freq)

    parent.left = left
    parent.right = right

    heapq.heappush(heap, parent)


codes = generate_codes(heap[0])

print("\nHuffman Codes:")

for char, code in codes.items():
    print(char + ":", code)
