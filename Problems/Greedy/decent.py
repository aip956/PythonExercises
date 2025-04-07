
def decentNumber(n):
    numThrees = 0
    numFives = n
    while (n - numThrees) % 3 != 0:
        numThrees += 5
    if (numThrees > n):
        print("-1")
    else:
        numFives = n - numThrees
        print(f"5"*numFives + "3"*numThrees)


if __name__ == '__main__':
    n1 = 1
    decentNumber(n1)
    n2 = 3
    decentNumber(n2)
    n3= 5
    decentNumber(n3)
    n4 = 11
    decentNumber(n4)

