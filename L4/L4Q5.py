def printer(secret, opened):
    for n in range(0, len(secret)):
        if n in opened:
            print(secret[n], end="")
        else:
            print("_", end="")
    print("\n")
     
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___


