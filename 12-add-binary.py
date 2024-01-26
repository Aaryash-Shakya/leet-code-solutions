# converting binary to decimal, adding them, then converting back to binary
def add_binary(a, b):
    # convert binary to decimal
    dec_a = int(a, 2)
    dec_b = int(b, 2)
    # add the decimals
    dec_sum = dec_a + dec_b
    # convert the sum back to binary
    bin_sum = bin(dec_sum)[2:]
    # print the sum as string
    print(str(bin_sum))


# Examples;
add_binary("11", "1")  # "100"
add_binary("1010", "1011")  # "10101"
