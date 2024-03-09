def hammingWeight(n):
    # Convert the number to binary string
    bin_str = str(bin(n)) 

    # Count the number of '1' bits in the binary string
    return bin_str.count("1")


# Examples:
# hammingWeight(0b00000000000000000000000000001011)  # 3
# hammingWeight(0b00000000000000000000000010000000)  # 1
# hammingWeight(0b11111111111111111111111111111101)  # 31