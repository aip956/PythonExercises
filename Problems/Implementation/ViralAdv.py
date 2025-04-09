
def viralAdvertising(n):
    
    # Write your code here

if __name__ == '__main__':
    n = 5
    viralAdvertising(n)



'''
https://www.hackerrank.com/challenges/strange-advertising/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

Day 1: 
Share: Send to 5
Like: Floor 5/2 = 2
CummulativeLikes = 2
Share: The 2 share with 3
Day 2:
Share: Send to Floor 5/2 * 3 = 6
Like: Floor recipients / 2 = 3
CummulativeLikes = 5
Day 3:
Share with 3 * Likes = 9
Like: Floor recipients / 2 = 9/2 = 4
CummulativeLikes = 5+ 4 = 9
Day 4:
Share: 3 * 4 = 12
Likes = Floor recipients / 2 = 12/2 = 6
CummulativeLikes = 9 + 6 = 15
Day 5:
Share: 3 * Likes(6) = 18
Likes = Floor recipients / 2 = 18/2 = 9
CummulativeLikes = 15 + 9 = 24

Determine how many people like the ad on a given day
n = 5



'''
