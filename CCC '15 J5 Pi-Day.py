import sys
input = sys.stdin.readline
memo = {}
pies = int(input())
people = int(input())

def find(pies_left, people_left, smallest):
    count = 0
    #print(l)
    if pies_left == 0 and people_left == 0:
        return 1

    if pies_left <= 0 and people_left != 0:
        return 0

    if people_left == 0 and pies_left != 0:
        return 0

    if memo.get((pies_left, people_left, smallest)) != None :
        return memo[(pies_left, people_left, smallest)]

    b = pies_left // people_left + 1
    for i in range(smallest, b):
        
        count += (find(pies_left - i, people_left - 1, max(smallest, i)))
        memo[pies_left, people_left, smallest] = count

    return count  
    
print(find(pies, people, 1))
#print(memo)





    

    
