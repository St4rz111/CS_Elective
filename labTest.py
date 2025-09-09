ages = [23, 25, 22, 30, 28, 23, 26]  #store ages in a list 'ages'
average_age = sum(ages) / len(ages)  #sum of ages divided by the length of the list 'ages'
unique_ages = set(ages)              #remove duplicate in 'age' list, and reorder the list in ascending order

print("Average age:", average_age)   #print average age
print("Unique ages:", unique_ages)   #print 'age' list w/o duplicates, and in order


highest = max(ages)                  #maximum age in the list
lowest = min(ages)                   #minimum age in the list

print("Highest age:", highest)
print("Lowest age:", lowest)