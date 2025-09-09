from collections import Counter
speedList = [4, 6, 5, 7, 5, 6, 4, 8]
highestSpeed = max(speedList)
lowestSpeed = min(speedList)
removeDupes = set(speedList)

print("Max: ", highestSpeed)
print("Min: ", lowestSpeed)
print("Unique Data: ", removeDupes)

speedDictionary = {}

for value in speedList:
    if value in speedDictionary:  
        speedDictionary[value] += 1
    else:                           
        speedDictionary[value] = 1

print("Count: ", speedDictionary)

