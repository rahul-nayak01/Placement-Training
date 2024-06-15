#binary to hexa decimal
def binary_to_hex(binary):
    hex_decimal = hex(int(binary, 2))[2:]
    return hex_decimal

# Example usage
binary_number = "10101010"
hexadecimal_number = binary_to_hex(binary_number)
print(hexadecimal_number)  
