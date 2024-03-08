def mySqrt(x):
    for i in range(1,x+1):
        square = i * i
        # if the square is equal to x, return the number
        if square == x: return i
        # if the square is greater than x, return the previous number
        elif square > x:
            return i-1
    return 0


# Examples:
# mySqrt(4)  # 2
# mySqrt(8)  # 2
