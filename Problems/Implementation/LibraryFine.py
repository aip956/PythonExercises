

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine = 0
    if (y1 > y2):
        return 10000
    if (y1 == y2 and m1 > m2):
        return (m1 - m2) * 500
    if (y1 == y2 and m1 == m2 and d1 > d2):
        return (d1 - d2) * 15
    return 0

if __name__ == '__main__':
    # Return date
    d1 = 9
    m1 = 6
    y1 = 2015
    # Due Date
    d2 = 6
    m2 = 6
    y2 = 2015
print(libraryFine(d1, m1, y1, d2, m2, y2))