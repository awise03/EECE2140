k = 0
sum = 0
print("K\t\tValue")
for x in range(11000):
    series = ((-1)**x)/(2*x + 1)
    sum += series * 4
    print(f"{x}\t\t{sum:<.6f}")

    #3.14 at 118
    #3.141 at 1685
    #3.1415 at 10735