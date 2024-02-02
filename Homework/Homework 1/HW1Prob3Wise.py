for c in range(1, 1000):
    x = 1
    for a in range(1, 1000):
        for b in range(x, 1000):
            if a**2 + b**2 == c**2:
                print(f"{a:<}\t{b:<}\t{c:<}", sep = " ")
                x = a + 1