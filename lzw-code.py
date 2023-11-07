def compress(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current_code = ""
    
    for symbol in data:
        current_code += symbol
        if current_code not in dictionary:
            dictionary[current_code] = next_code
            next_code += 1
            current_code = current_code[:-1]
            result.append(dictionary[current_code])
            current_code = symbol

    if current_code in dictionary:
        result.append(dictionary[current_code])

    return result

def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []
    previous_code = compressed_data[0]
    decompressed_data = dictionary[previous_code]

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = decompressed_data + decompressed_data[0]
        else:
            raise ValueError("Corrupted data")

        result.append(entry)
        dictionary[next_code] = decompressed_data + entry[0]
        next_code += 1
        decompressed_data = entry

    return "".join(result)

if __name__ == "__main__":
    input_data = "ABABABABA"
    
    compressed_data = compress(input_data)
    print("Compressed data:", compressed_data)
    
    decompressed_data = decompress(compressed_data)
    print("Decompressed data:", decompressed_data)