aqiList = [50, 65, 55, 80, 70, 65, 90, 100]

avg_aqi = sum(aqiList) / len(aqiList)
unique_aqi = set(aqiList)

aqiDictionary = {}

for value in aqiList:
    if value in aqiDictionary:  
        aqiDictionary[value] += 1
    else:                           
        aqiDictionary[value] = 1

print("Average: ", avg_aqi)
print("Unique Data: ", unique_aqi)
print("Count: ", aqiDictionary)