def reverse(num):
    rev = 0
    while num > 0:
        rev *= 10
        mod = num % 10
        rev += mod
        num //= 10
    return rev
    
def beautiful_days(i, j, k):
    count = 0
    for a in range(i, j + 1):
        rev = reverse(a)
        if abs(a - rev) % k == 0:
            count += 1
    print (f"count: {count}")
    return count

if __name__ == "__main__":
    i = 20
    j = 23
    k = 6
    beautiful_days(i, j, k)