from collections import Counter

bloodPressureList = [120, 135, 118, 140, 128, 135, 122, 130]

avg_bloodPressure = sum(bloodPressureList) / len(bloodPressureList)
unique_bloodPressure = set(bloodPressureList)

print("Average: ", avg_bloodPressure)
print("Unique Data: ", unique_bloodPressure)


bloodPressureDictionary = {}

for value in bloodPressureList:
    if value in bloodPressureDictionary:  
        bloodPressureDictionary[value] += 1
    else:                           
        bloodPressureDictionary[value] = 1

print("Count: ", bloodPressureDictionary)
