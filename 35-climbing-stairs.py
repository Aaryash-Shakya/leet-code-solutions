def climbing_stairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbing_stairs(n - 1) + climbing_stairs(n - 2)

    # one line with comprehension
    # return 1 if n==0 or n==1 else climbing_stairs(n-1)+climbing_stairs(n-2)


# Examples:
# climbing_stairs(2)  # 2
# climbing_stairs(3)  # 3
# climbing_stairs(4)  # 5
