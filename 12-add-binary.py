# converting binary to decimal, adding them, then converting back to binary
def add_binary(a, b):
    # convert binary to decimal
    int_a = int(a, 2)
    int_b = int(b, 2)
    # add the decimals
    int_sum = int_a + int_b
    # convert the sum back to binary
    bin_sum = bin(int_sum)[2:]
    # print the sum as string
    print(str(bin_sum))


# Examples;
add_binary("11", "1")  # "100"
add_binary("1010","1011") # "10101"
