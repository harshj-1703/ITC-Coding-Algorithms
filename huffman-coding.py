import heapq

class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability

def build_huffman_tree(probabilities):
    # Create a priority queue (min-heap) for the initial nodes
    priority_queue = [Node(symbol, prob) for symbol, prob in probabilities.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        merged_node = Node(None, left_node.probability + right_node.probability)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code
    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def generate_huffman_codes(probabilities):
    root = build_huffman_tree(probabilities)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)
    return huffman_codes

if __name__ == "__main__":
    random_variables = {
        'X1': 0.50,
        'X2': 0.20,
        'X3': 0.15,
        'X4': 0.10,
        'X5': 0.05
    }
    
    huffman_codes = generate_huffman_codes(random_variables)
    for symbol, code in huffman_codes.items():
        print(f"Symbol: {symbol}, Probability: {random_variables[symbol]}, Huffman Code: {code}")
