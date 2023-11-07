def arithmetic_encode(data, probabilities):
    start, end = 0.0, 1.0
    for symbol in data:
        sym_start, sym_end = start, start
        for prob_symbol, prob in probabilities.items():
            sym_end += prob
            if symbol == prob_symbol:
                break
            sym_start = sym_end

        start, end = sym_start, sym_end

    return start

def arithmetic_decode(encoded_value, probabilities, length):
    result = []
    start, end = 0.0, 1.0
    for _ in range(length):
        for symbol, prob in probabilities.items():
            if start <= encoded_value < start + prob:
                result.append(symbol)
                start, end = start, start + prob
                break
            start = start + prob

    return result

if __name__ == "__main__":
    input_data = "ABBCCCC"
    probabilities = {'A': 0.1, 'B': 0.4, 'C': 0.5}
    
    encoded_value = arithmetic_encode(input_data, probabilities)
    print("Encoded value:", encoded_value)
    
    decoded_data = arithmetic_decode(encoded_value, probabilities, len(input_data))
    print("Decoded data:", ''.join(decoded_data))
